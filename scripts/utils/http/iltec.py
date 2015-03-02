#!/usr/bin/env python
# encoding: utf-8
from utils.settings   import Settings
from utils.words.word import Word
from .priberam        import Priberam
from .base            import HTTP
from lxml import html
import re
        

class PortalLinguaPortuguesa(HTTP):
    host = "http://www.portaldalinguaportuguesa.org"
    
    class NoWordsInRow(Exception):
        pass
    
    @classmethod
    def get_words_starting_with_char(cls, char):
        
        def get_page():
            url = cls.host + "/?action=novoacordo&act=list&letter=%s&version=pe"
            return cls.get(url%char)
            
        def get_words():
            tree  = html.fromstring( get_page() )
            table = tree.xpath('//table[@id="body_tabela"]')[0]
            table = html.fromstring( html.tostring(table) )
            cells = table.xpath('//td/text()')
            for i in range(0, len(cells), 3):
                aao = cells[i].strip()
                if not aao:
                    continue
                for dao in cells[i+1].strip().split(','):
                    if dao and dao != aao:
                        yield Word.get(aao, Priberam.AAO), Word.get(dao, Priberam.DAO)
             
        return dict([each for each in get_words()])
    
    @classmethod
    def get_words(cls):
        alphabet = [chr(i) for i in range(97, 123)]
        for each in alphabet:
            if Settings.VERBOSE:
                print "\n>> Getting words starting with '%s'" %each.upper()
            yield cls.get_words_starting_with_char(each)
            
    
        

    