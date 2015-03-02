#!/usr/bin/env python
# encoding: utf-8
from utils.exceptions import MultipleOptions, PluralUnknown, PluralNotFound
from utils.http.base  import HTTP
from utils.settings   import Settings
from utils.consts     import PREPOSITIONS, PREFIXOS
from utils.functions  import user_input, verbosity
from .rules           import Feminine, Plural
from lxml import html
import re


class Word(str):
    
    @classmethod
    def get(cls, word, priberam):
        instance = cls(word.strip())
        instance.priberam = priberam
        return instance
    
    def create(self, word):
        return self.get(word, self.priberam)
    
    @property
    def page(self):
        if not hasattr(self, '_page'):
            self._page = self.priberam.get_word_page(self)
        return self._page

    def exists(self):
        # if "Palavra reconhecida pelo FLiP mas sem definição no dicionário." in self.page:
        #     return True
        return "Palavra não encontrada." not in self.page

    def is_feminine(self):
        tree = html.fromstring(self.page)
        content = tree.xpath('//div[@id="resultados"]')[0].text_content()
        
        if "substantivo feminino" in content:
            return True
        if "derivação fem" in content:
            return True
        if "substantivo masculino" in content:
            return False

        splitted = re.split( r'-|\s', self )        
        if len(splitted) == 2:# and splitted[0] in PREPOSITIONS:
            return self.create( splitted[1] ).is_feminine()
        elif len(splitted) == 3 and splitted[1] in PREPOSITIONS:
            return self.create( splitted[0] ).is_feminine()
                
        for each in PREFIXOS:
            if self.startswith( each ):
                subword = self[len(each):]
                if subword[0] == subword[1]:
                    return self.create( subword[1:] ).is_feminine()
                return self.create( subword ).is_feminine()
        return False
        
    def is_verb(self):
        return "Conjugar" in self.page
    
    @verbosity()    
    def conjugate_verb(self):
        return self.priberam.get_conjugations(self)
    
    def _get_plural(self):
        try:
            if Settings.NO_PRIBERAM:
                return Plural.get( self )
            try:
                return self.priberam.get_plural( self )
            except (PluralUnknown, PluralNotFound):
                return Plural.get( self )
        except MultipleOptions as e:
            return e.ask_priberam( self.priberam ) or user_input( e.parent_options )
    
    @verbosity()            
    def get_plural(self):
        return self.create( self._get_plural() )
     
    def _get_feminine(self):
        try:
            return Feminine.get( self )
        except MultipleOptions as e:
            return e.ask_priberam( self.priberam ) or user_input( e.parent_options )
    
    @verbosity()   
    def get_feminine(self):  
        if not self.is_feminine():
            return self.create( self._get_feminine() )    
        return self
    