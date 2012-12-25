#!/usr/bin/env python
# encoding: utf-8
from utils.exceptions     import *
from utils.priberam       import Priberam
from utils.rules.feminine import Feminine
from utils.rules.plural   import Plural
from utils.settings       import Settings
from utils                import verbosity, user_input


class Grammar(object):
    
    class API(object):
        
        @classmethod
        @verbosity()
        def get_plural(self, word):
            try:
                if Settings.NO_PRIBERAM:
                    return Plural.get( word )
                try:
                    return self.priberam.get_plural( word )
                except (WordNotRecognized, WordUnknown, PluralUnknown, PluralNotFound):
                    return Plural.get( word )
            except MultipleOptions as e:
                return e.ask_priberam( self.priberam ) or user_input( e.options )


        @classmethod
        @verbosity()
        def get_feminine(self, word):
            if Settings.NO_PRIBERAM or not self.priberam.is_feminine( word ):
                try:
                    return Feminine.get( word )
                except MultipleOptions as e:
                    return e.ask_priberam( self.priberam ) or user_input( e.options )
            return word
            
            
        @classmethod
        @verbosity()
        def get_conjugations(self, word):
            try:
                return self.priberam.get_conjugations( word )
            except VerbNotFound:
                return []
    
    
    class AAO(API):
        priberam = Priberam.AAO
        
    class DAO(API):
        priberam = Priberam.DAO
        