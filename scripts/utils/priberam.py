#!/usr/bin/env python
# encoding: utf-8
from utils.exceptions import *
from utils.regexes    import PLURAL_REGEXES, VERB_REGEX
from utils.settings   import Settings
import requests, re, time


class Priberam(object):
    
    class API(object):
        cookies = {}
        
        @classmethod
        def get(self, url, whitespaces=False):
            clean = lambda x: " ".join( x.replace( '\n', '' ).split() )
            if Settings.LAZY:
                time.sleep(0.5)
            response = requests.get( url, cookies=self.cookies ).content
            return response if whitespaces else clean( response )
        
        @classmethod
        def get_plural(self, word):
            response = self.get( "http://priberam.pt/DLPO/default.aspx?pal=%s"%word )
            if "Palavra reconhecida pelo FLiP mas sem definição no dicionário." in response:
                raise WordNotRecognized( word )
            if "Palavra não encontrada." in response:
                raise WordUnknown( word )
            if "Plural:" not in response:
                raise PluralUnknown( word )
            for regex in PLURAL_REGEXES:
                result = re.findall( regex, response )
                if result:
                    return result[0].strip('.')[0]
            raise PluralNotFound( word )
            
        @classmethod
        def get_conjugations(self, word):
            response = self.get( "http://www.priberam.pt/dlpo/Conjugar.aspx?pal=%s"%word, True )
            if "não foi encontrado" in response:
                raise VerbNotFound( word )
            conjugations = re.findall( VERB_REGEX, response )
            all_words = []
            for conj in conjugations:
                words = conj.split('<br>')
                all_words += words[:4]+words[5:] if len(words)==7 else words
            return all_words
            

    class AAO(API):
        cookies = {
            'DLPO_UsaAcordo': False,
            'aAO': 0,
            'varpt': 0,
        }
        
    class DAO(API):
        cookies = {
            'DLPO_UsaAcordo': True,
            'aAO': 1,
            'varpt': 0,
        }

