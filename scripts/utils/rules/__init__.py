#!/usr/bin/env python
# encoding: utf-8
from utils import PREPOSITIONS, MAIN_PREPOSITIONS

class Rules(object):
    
    @classmethod
    def get(self, word):
        if "-" in word:
            return self.__hifen_rules( word, sep="-" ) or self.__get( word )
        elif " " in word:
            return self.__hifen_rules( word, sep=" " ) or self.__get( word ) 
        return self.__composite( word ) or self.__get( word )
    
    @classmethod
    def __hifen_rules(self, word, sep):
        splited = word.split( sep )
        if len(splited) == 2 and splited[0] in PREPOSITIONS:
            return sep.join( [splited[0], self.__get(splited[1])] )
        elif len(splited) >= 3 and splited[1] in PREPOSITIONS:
            return sep.join( [self.__get(splited[0])]+splited[1:] )
        return self.__get( word )
        
    @classmethod
    def __composite(self, word):
        for preposition in MAIN_PREPOSITIONS:
            if word.startswith( preposition ):
                subword = word[len(preposition):]
                if subword[0] == subword[1]:
                    return preposition + subword[0] + self.__get( subword[1:] )
                return preposition + self.__get( subword )

    @classmethod
    def __get(self, word):
        if self.__name__ == 'Feminine':
            return self._Feminine__get( word )
        return self._Plural__get( word )
    