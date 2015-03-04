#!/usr/bin/env python
# encoding: utf-8
from utils.settings      import Settings
from utils.exceptions    import WordFormUnknown, VerbNotFound, NotVerb, AlreadyFeminine
from utils.http.priberam import Priberam
from utils.words.word    import Word


class Dictionary(dict):     
    def __init__(self, dao, aao):
        self.dao = Word.get(dao, Priberam.DAO)
        self.aao = Word.get(aao, Priberam.AAO)
        self.update({self.dao: self.aao})

    def include_variations(self):
        self.add_feminines()
        self.add_plurals()
        self.add_conjugations()
        self.remove_redundancy()
        return self

    def add_feminines(self):
        try:
            self[ self.dao.get_feminine() ] = self.aao.get_feminine()
        except (WordFormUnknown, AlreadyFeminine):
            return

    def add_plurals(self):
        for dao,aao in self.items():
            try:
                self[ dao.get_plural() ] = aao.get_plural()
            except WordFormUnknown:
                continue

    def add_conjugations(self):
        try:
            conjugations = []
            dao_conjugations = self.dao.conjugate_verb()
            aao_conjugations = self.aao.conjugate_verb()
            if len(dao_conjugations) == len(aao_conjugations):
                conjugations.append( zip(dao_conjugations, aao_conjugations) )
            elif Settings.VERBOSE:
                message = "\tWARNING: could not conjugate '%s' and '%s' properly."
                print message % (self.dao, self.aao)
        except VerbNotFound as e:
            if Settings.VERBOSE:
                print '\tWARNING: verb "%s" not found' % e.word
        except NotVerb:
            return
        else:
            if conjugations:
                mapping = dict( reduce(lambda a,b: a+b, conjugations) )
                self.update( mapping )                

    def remove_redundancy(self):
        for dao,aao in self.items():
            if dao == aao or not dao or not aao:
                self.pop( dao )

