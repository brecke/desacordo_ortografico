#!/usr/bin/env python
# encoding: utf-8
from utils.exceptions    import MultipleOptions, WordFormUnknown, NotVerb, AlreadyFeminine
from utils.settings      import Settings
from utils.consts        import PREPOSITIONS, PREFIXES
from utils.decorators    import attribute
from utils.words.grammar import Feminine, Plural
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

    @attribute
    def page_content(self):
        return self.priberam.get_word_page(self)
    
    @attribute
    def results_content(self):
        if self.exists:
            element = self.tree.xpath('//div[@id="resultados"]')[0]
            return element.text_content()
        return ''
    
    @attribute
    def tree(self):
        return html.fromstring(self.page_content)
    
    @attribute
    def exists(self):
        return "Palavra não encontrada." not in self.page_content

    def is_feminine(self):
        
        def basic_method():        
            if "substantivo feminino" in self.results_content:
                return True
            if "derivação fem" in self.results_content:
                return True
            if "derivação masc. e fem." in self.results_content:
                return True
            if "substantivo masculino" in self.results_content:
                return False
            if "derivação masc" in self.results_content:
                return False

        def split_word_method():
            splitted = re.split( r'-|\s', self )        
            if len(splitted) == 2:
                return self.create( splitted[1] ).is_feminine()
            elif len(splitted) == 3 and splitted[1] in PREPOSITIONS:
                return self.create( splitted[0] ).is_feminine()
        
        def prefix_method():
            for each in PREFIXES:
                if self.startswith( each ):
                    subword = self[len(each):]
                    if subword[0] == subword[1]:
                        return self.create( subword[1:] ).is_feminine()
                    return self.create( subword ).is_feminine()
        
        for each in [basic_method, split_word_method, prefix_method]:
            answer = each()
            if answer != None:
                return answer
        return False

    def conjugate_verb(self):
        
        def xpath(code, tree=None):
            tree = self.tree if tree == None else tree
            for each in tree.xpath( code ):
                yield html.fromstring( html.tostring(each) )
        
        if "Conjugar" not in self.results_content:
            raise NotVerb
        code = '//span[@class="%s"]' % self.priberam.class_name
        for span in xpath(code):
            for anchor in xpath('//a', tree=span):
                items = anchor.items()[0]
                if items[0] == 'href' and anchor.text == 'Conjugar':
                    word = items[1].split('/')[-1].strip()
                    return self.priberam.get_conjugations(word)        

    def get_plural(self):
        try:
            new_word = Plural.get(self)
        except MultipleOptions as e:
            new_word = e.ask_priberam( self.priberam )
        return self.create( new_word )

    def get_feminine(self):  
        if not self.is_feminine():
            try:
                new_word = self.create( Feminine.get(self) )
            except MultipleOptions as e:
                new_word = e.ask_priberam( self.priberam )
            return self.create( new_word )
        raise AlreadyFeminine
    