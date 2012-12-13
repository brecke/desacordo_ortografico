#!/usr/bin/env python
# encoding: utf-8
from utils.priberam.exceptions import *
from utils.priberam            import Priberam
from utils.feminine            import Feminine
from utils.plural              import Plural

class Grammar(object):
    
    class API(object):
        
        @classmethod
        def get_plural(self, word):
            try:
                return self.priberam_plural( word )
            except (WordNotRecognized, WordUnknown, PluralUnknown, PluralNotFound) as e:
                return Plural.get( word )

        @classmethod
        def get_feminine(self, word):
            # don't asks priberam. Caos!
            return Feminine.get( word )
    
    class AAO(API):
        priberam_plural = Priberam.AAO.get_plural
        
    class DAO(API):
        priberam_plural = Priberam.DAO.get_plural
        