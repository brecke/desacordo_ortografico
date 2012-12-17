#!/usr/bin/env python
# encoding: utf-8
from utils.exceptions import *
from utils.priberam   import Priberam
from utils.feminine   import Feminine
from utils.plural     import Plural
from utils.settings   import Settings
from utils            import verbosity


class Grammar(object):
    
    class API(object):
        
        @classmethod
        @verbosity()
        def get_plural(self, word):
            try:
                return self.priberam_plural( word ) if Settings.PRIBERAM else Plural.get( word )
            except (WordNotRecognized, WordUnknown, PluralUnknown, PluralNotFound):
                return Plural.get( word )

        @classmethod
        @verbosity()
        def get_feminine(self, word):
            # don't asks priberam. Caos!
            return Feminine.get( word )
            
        @classmethod
        @verbosity()
        def get_conjugations(self, word):
            try:
                return self.priberam_conjugations( word )
            except VerbNotFound:
                return []
    
    class AAO(API):
        priberam_plural       = Priberam.AAO.get_plural
        priberam_conjugations = Priberam.AAO.get_conjugations
        
    class DAO(API):
        priberam_plural       = Priberam.DAO.get_plural
        priberam_conjugations = Priberam.DAO.get_conjugations
        