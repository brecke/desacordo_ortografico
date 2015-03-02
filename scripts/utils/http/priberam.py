#!/usr/bin/env python
# encoding: utf-8
from utils.exceptions import *
from utils.consts     import PREPOSITIONS, PREFIXOS
from utils.settings   import Settings
from utils.consts     import PLURAL_REGEXES
from utils.words.word import Word
from .base import HTTP
from lxml import html
import re


class Priberam(object):
    
    class API(HTTP):
        
        @classmethod
        def word_exists(cls, word):
            return Word.get(word, cls).exists()
        
        @classmethod
        def get_word_page(cls, word):
            url = "http://priberam.pt/DLPO/"
            return cls.get( url+word, cookies=cls.cookies )
        
        @classmethod
        def get_verb_page(cls, verb):
            url = "http://www.priberam.pt/dlpo/Conjugar/"
            return cls.get( url+verb, cookies=cls.cookies )
        
        @classmethod
        def get_plural(cls, word):
            content = cls.get_word_page( word )
            if "Plural:" not in content:
                raise PluralUnknown()
            for regex in PLURAL_REGEXES:
                result = re.findall( regex, content )
                if result:
                    return result[0].split('.')[0]
            raise PluralNotFound()
                    
        @classmethod
        def get_conjugations(cls, word):            
            page = cls.get_verb_page( word )
            if "não está disponível" in page:
                raise VerbNotFound(word)
            tree = html.fromstring(page)
            
            def get(xpath):
                return [each.strip() for each in tree.xpath( xpath ) if each.strip()]
            
            conjugations = []
            conjugations = get('//div[@class="clearfix"]/text()')
            conjugations += get('//span[@class="Imperativo"]/text()')
            conjugations += get('//span[@class="ImperativoNegativo"]/text()')
            
            def indexes_to_pop():
                persons = get('//div[@class="ConjugaNumeroPessoa smallText"]/text()')
                for i in range(len(persons)-1, 0, -1):
                    if persons[i] == persons[i-1]:
                        yield i
            
            for i in indexes_to_pop():
                # print 'poping: ', conjugations[i]
                conjugations = conjugations[:i] + conjugations[i+1:]
            return conjugations
    

    class AAO(API):
        cookies = {
            'DLPO_LanguageID': '2070',
            'DLPO_AntesAcordo': 'True',
            'DLPO_UsaAcordo': 'True',
            'aAO': '0',
            'varpt': '0',
        }
        
    class DAO(API):
        cookies = {
            'DLPO_LanguageID': '2070',
            'DLPO_AntesAcordo': 'False',
            'DLPO_UsaAcordo': 'True',
            'aAO': '1',
            'varpt': '0',
        }

