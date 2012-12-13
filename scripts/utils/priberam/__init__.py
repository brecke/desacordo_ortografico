#!/usr/bin/env python
# encoding: utf-8
from utils.priberam.exceptions import *
import requests, re

PLURAL_REGEXES = [
    r'<span class="varpt">Plural: <span class="varpt"><pt><span class="aAO" [^<>]*><aAO>([^<>]*)\.?</aAO></span>',
    r'<span class="varpt">Plural: <span class="varpt"><pt>([^<>]*)\.?</pt></span>',
    r'<span class="varpt">Plural: <span class="aAO" [^<>]*"><aAO>([^<>]*)\.?</aAO></span>',
    r'<span class="varpt">Plural: ([^<>]*)\.?</span></div><span class="varpt"',
    r'<span class="varpt">Plural: ([^<>]*)\.?</span></div>',
    r'<span class=""><span class="aAO" [^<>]*><aAO>Plural: ([^<>]*)\.?</aAO></span>',
    r'<span class="">Plural: <span class="varpt"><pt>([^<>]*)\.?</pt></span>',
    r'<span class="">Plural: <span class="aAO" [^<>]*><aAO>([^<>]*)\.?</aAO></span>',
    r'<span class="varpt"><span class="aAO" [^<>]*><aAO>Plural: ([^<>]*)\.?</aAO></span>',
    r'Plural: <span class="aAO" [^<>]*><aAO>([^<>]*)\.?</aAO></span>',
    r'Plural: <span class="varpt"><pt><span class="aAO" [^<>]*><aAO>([^<>]*)\.?</aAO></span>',
    r'<span class="">Plural: ([^<>]*)\.?</span>',
    r'Plural: ([^<>]*)\.?</span></div>',
]


class Priberam(object):
    
    class API(object):
        url     = "http://priberam.pt/DLPO/default.aspx?pal=%s"
        cookies = {}
        
        @classmethod
        def get(self, word):
            response = requests.get( self.url%word, cookies=self.cookies ).content
            return " ".join( response.replace( '\n', '' ).split() )
        
        @classmethod
        def get_plural(self, word):
            response = self.get( word )
            if "Palavra reconhecida pelo FLiP mas sem definição no dicionário." in response:
                raise WordNotRecognized( word )
            if "Palavra não encontrada." in response:
                raise WordUnknown( word )
            if "Plural:" not in response:
                raise PluralUnknown( word )
            for regex in PLURAL_REGEXES:
                result = re.findall( regex, response )
                if result:
                    return result[0]
            raise PluralNotFound( word )

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

