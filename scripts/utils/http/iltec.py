#!/usr/bin/env python
# encoding: utf-8
from utils.settings import Settings
from .base          import HTTP
from lxml import html
        

class PortalLinguaPortuguesa(HTTP):
    host = "http://www.portaldalinguaportuguesa.org"
    
    words_to_ignore = {
        'tracto': 'trato',
        'péla': 'pela',
        'pêlo': 'pelo',
    }
    
    words_to_add = {
        'facturado': 'faturado',
        'egipto': 'egito',
        'sector': 'setor',
    }
    
    @classmethod
    def get_words_starting_with(cls, char):
        if Settings.VERBOSE:
            print "\n>> Getting words starting with '%s'" %char.upper()
        
        def get_page():
            url = cls.host + "/?action=novoacordo&act=list&letter=%s&version=pe"
            return cls.get(url%char)
            
        def get_words_from_page(page):
            tree  = html.fromstring( page )
            table = tree.xpath('//table[@id="body_tabela"]')[0]
            table = html.fromstring( html.tostring(table) )
            return table.xpath('//td/text()')
        
        items = get_words_from_page( get_page() )
        for i in range(0, len(items), 3):
            aao = items[i].strip()
            if not aao or aao in cls.words_to_ignore.keys():
                continue  
            for dao in items[i+1].strip().split(','):
                if dao and dao != aao:
                    yield dao, aao
    
    @classmethod
    def get_words(cls):
        alphabet = [chr(i) for i in range(97, 123)]
        for char in alphabet:
            for each in cls.get_words_starting_with(char):
                yield each
        for aao,dao in cls.words_to_add.iteritems():
            yield dao, aao
