#!/usr/bin/env python
# encoding: utf-8
from utils.settings   import Settings
from utils.exceptions import WordFormUnknown, VerbNotFound
from utils.functions  import verbosity
import re


class Words(dict):     
    def __init__(self, dic):
        self.update( dic )
        self.original = dic.items()

    def with_variants(self):
        self.add_feminines()
        self.add_plurals()
        self.add_conjugations()
        self.remove_redundancy()
        return self

    @verbosity('> adding plural form')
    def add_plurals(self):
        for dao,aao in self.items():
            try:
                self[ dao.get_plural() ] = aao.get_plural()
            except WordFormUnknown:
                continue

    @verbosity('> adding feminine form')
    def add_feminines(self):
        for dao,aao in self.items():
            if dao.is_feminine() or aao.is_feminine():
                continue
            try:
                self[ dao.get_feminine() ] = aao.get_feminine()
            except WordFormUnknown:
                continue

    @verbosity('> adding verb conjugations')
    def add_conjugations(self):
        words = []
        for dao,aao in self.original:
            try:
                if dao.is_verb() and aao.is_verb():
                    dao_conjugations = dao.conjugate_verb()
                    aao_conjugations = aao.conjugate_verb()
                    if len(dao_conjugations) == len(aao_conjugations):
                        words.append( zip(dao_conjugations, aao_conjugations) )
                    elif Settings.VERBOSE:
                        print "\tWARNING: could not conjugate '%s' and '%s' properly." %(dao, aao)
            except VerbNotFound as e:
                if Settings.VERBOSE:
                    print '\tWARNING: verb "%s" not found' % e.word
                continue
        if words:
            self.update( dict( reduce(lambda a,b: a+b, words) ) )                

    @verbosity('> removing redundancy')
    def remove_redundancy(self):
        for dao,aao in self.items():
            if dao==aao or not dao or not aao:
                self.pop( dao )

