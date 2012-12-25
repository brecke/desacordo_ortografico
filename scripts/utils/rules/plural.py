#!/usr/bin/env python
# encoding: utf-8
from utils            import PREPOSITIONS
from utils.rules      import Rules
from utils.exceptions import MultipleOptions
import re

# http://pt.wikipedia.org/wiki/Preposi%C3%A7%C3%A3o


class Plural(Rules):
    """
    http://pt.wikipedia.org/wiki/Plural
    """
    
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
    def __special_rules(self, word):
        if word.endswith("r") or word.endswith("z"):
            return word[:-1]+"es"
        if word.endswith("n"):
            raise MultipleOptions( word+"s", word+"es" )
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
            if word=="til":
                return "tiles"
            raise MultipleOptions( word[:-1]+"s", word[:-2]+"eis" )
        if word.endswith("m"):
            return word[:-1]+"ns"
        if word.endswith("x"):
            return word+"es" if word in ["fax", "fénix"] else word
        if word.endswith("ão"):
            size = len("ão")
            raise MultipleOptions( word[:-size]+"ões", word[:-size]+"ãos", word[:-size]+"ães" )
