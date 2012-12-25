#!/usr/bin/env python
# encoding: utf-8
from utils.exceptions    import *
from utils.priberam.http import PriberamRequests
from utils               import PREPOSITIONS, MAIN_PREPOSITIONS
import re


class Priberam(object):
    
    class API(object):
        url = "http://priberam.pt/DLPO/default.aspx?pal=%s"
        
        @classmethod
        def __get(self, url, whitespaces=False):
            return PriberamRequests.get( 
                url         = url,
                cookies     = self.cookies,
                whitespaces = whitespaces
            ).check_content()


        @classmethod
        def word_exists(self, word):
            try:
                return True if self.__get( self.url%word ) else False
            except (WordNotRecognized, WordUnknown):
                return False


        @classmethod
        def get_plural(self, word):
            return self.__get( self.url%word ).check_plural().get_plural()
            
            
        @classmethod
        def get_conjugations(self, word):
            url = "http://www.priberam.pt/dlpo/Conjugar.aspx?pal=%s"
            response = self.__get( url%word, whitespaces=True )
            return response.check_conjugations().get_conjugations()
            
        
        @classmethod
        def is_feminine(self, word):
            def hifens():
                splitted = re.split( r'-|\s', word )
                if len(splitted) == 2 and splitted[0] in PREPOSITIONS:
                    return self.is_feminine( splitted[1] )
                elif len(splitted) == 3 and splitted[1] in PREPOSITIONS:
                    return self.is_feminine( splitted[0] )
                    
            def composite():
                for preposition in MAIN_PREPOSITIONS:
                    if word.startswith( preposition ):
                        subword = word[len(preposition):]
                        if subword[0] == subword[1]:
                            return self.is_feminine( subword[1:] ) 
                        return self.is_feminine( subword )
                            
            try:
                return "<em>s. f.</em>" in self.__get( self.url%word ).content
            except (WordNotRecognized, WordUnknown):
                return hifens() or composite()   
         

    class AAO(API):
        cookies = {
            'DLPO_UsaAcordo': 'False',
            'aAO': '0',
            'varpt': '0',
        }
        
    class DAO(API):
        cookies = {
            'DLPO_UsaAcordo': 'True',
            'aAO': '1',
            'varpt': '0',
        }

