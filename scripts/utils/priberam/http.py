#!/usr/bin/env python
# encoding: utf-8
from utils.exceptions import *
from utils.settings   import Settings
from utils.regexes    import PLURAL_REGEXES, VERB_REGEX
import requests, time, re


class PriberamRequests(object):
    
    def __init__(self, content):
        self.content = content
    
    
    @classmethod
    def get(self, url, cookies={}, whitespaces=False):        
        clean = lambda x: " ".join( x.replace( '\n', '' ).split() )
        if Settings.LAZY:
            time.sleep(1)
        response = requests.get( url, cookies=cookies ).content
        return self( response if whitespaces else clean(response) )
        
        
    def check_content(self):
        if "Palavra reconhecida pelo FLiP mas sem definição no dicionário." in self.content:
            raise WordNotRecognized()
        if "Palavra não encontrada." in self.content:
            raise WordUnknown()
        return self
            
            
    def check_plural(self):
        if "Plural:" not in self.content:
            raise PluralUnknown()
        return self


    def check_conjugations(self):
        if "não foi encontrado" in self.content:
            raise VerbNotFound()
        return self


    def get_conjugations(self):
        conjugations = []
        for i in re.findall( VERB_REGEX, self.content ):
            words = i.split('<br>')
            conjugations += words[:4]+words[5:] if len(words)==7 else words
        return conjugations


    def get_plural(self):
        for regex in PLURAL_REGEXES:
            result = re.findall( regex, self.content )
            if result:
                return result[0].split('.')[0]
        raise PluralNotFound()

