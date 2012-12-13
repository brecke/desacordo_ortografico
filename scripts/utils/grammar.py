#!/usr/bin/env python
# encoding: utf-8

from utils.priberam import Priberam, WordNotRecognized, WordUnknown, PluralUnknown, PluralNotFound
from utils.plural   import Plural

class Grammar(object):

    @staticmethod
    def get_plural(word, aao=True):
        try:
            return Priberam.AAO.get_plural( word ) if aao else Priberam.DAO.get_plural( word ) 
        except (WordNotRecognized, WordUnknown, PluralUnknown, PluralNotFound) as e:
            return Plural.get( word )
        
    @staticmethod
    def get_feminine(word):
        pass
        