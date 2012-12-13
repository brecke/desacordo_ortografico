#!/usr/bin/env python
# encoding: utf-8
from utils import user_input
import re

# http://pt.wikipedia.org/wiki/Preposi%C3%A7%C3%A3o
PREPOSITIONS = [
    "a", "o", "as", "às", "à", "os", "ao", "aos", "na", "nas", "no", "nos",
    "ante", "antes", "apó", "após", "saté", "com", "contra", "de", "des", 
    "da", "das", "do", "dos", "desde", "em", "entre", "perante", "por", 
    "sem", "sob", "sobre", "trás", "no", "nos", "anti", "auto", #"para"
]


class Plural(object):
    """
    http://pt.wikipedia.org/wiki/Plural
    """
    
    @classmethod
    def get(self, word):
        if "-" in word or " " in word:
            return self.__hifen_rules( word )
        return self.__get( word )
    
    @classmethod
    def __get(self, word):
        for rules in [self.__special_rules, self.__simple_rules]:
            plural = rules( word )
            if plural:
                return plural
        return word+"s"
    
    @classmethod
    def __simple_rules(self, word):
        #TODO: terminado em ditongo oral -> words+"s"
        #TODO: nome de letras -> words+"s"
        #TODO: nome dos números excepto os terminados em "s" ou "z" -> words+"s"
        for char in ['a','e','i','o','u', "ã", "ãe"]:
            if word.endswith( char ):
                return word+"s"
    
    @classmethod
    def __hifen_rules(self, word):
        splited = re.split( r'-|\s', word )
        if len(splited) >= 3:
            if splited[1] in PREPOSITIONS:
                return "-".join( [self.__get(splited[0])]+splited[1:] )
        elif len(splited) == 2:
            if splited[0] in PREPOSITIONS:
                return "%s-%s" %( splited[0], self.__get(splited[1]) )
        return self.__get( word )
          
    @classmethod
    def __special_rules(self, word):
        if word.endswith("r") or word.endswith("z"):
            return word[:-1]+"es"
        if word.endswith("n"):
            options = [ word+"s", word+"es" ]
            return user_input( options )
        if word.endswith("ens"):
            return word
        if word.endswith("s"):
            return word if word in ["cós", "cais", "xis"] else  word[:-1]+"es"
        if word.endswith("al") or word.endswith("el") or word.endswith("ol") or word.endswith("ul"):
            exceptions = {
                "mal": "males", "cal": "cales", "aval": "avais", "mel": "meles",
                "fel": "feles", "mol": "moles", "cônsul": "cônsules",
            }
            return exceptions[word] if word in exceptions else word[:-1]+"is"
        if word.endswith("il"):
            options = [ word[:-1]+"s", word[:-2]+"eis" ] 
            return "tiles" if word=="til" else user_input( options )
        if word.endswith("m"):
            return word[:-1]+"ns"
        if word.endswith("x"):
            return word+"es" if word in ["fax", "fénix"] else word
        if word.endswith("ão"):
            size    = len("ão")
            options = [ word[:-size]+"ões", word[:-size]+"ãos", word[:-size]+"ães" ]
            return user_input( options )
