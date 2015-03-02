#!/usr/bin/env python
# encoding: utf-8
from .settings import Settings


class WordNotRecognized(Exception):
    pass


class WordUnknown(Exception):
    pass


class PluralUnknown(Exception):
    pass

        
class PluralNotFound(Exception):
    pass


class VerbNotFound(Exception):
    def __init__(self, word):
        self.word = word


class WordFormUnknown(Exception):
    pass


class MultipleOptions(Exception):
    def __init__(self, *options):
        self.options = options
        self.parent_options = self.options
        
    def ask_priberam(self, priberam):
        for i in range(len(self.options)):
            if priberam.word_exists( self.options[i] ):
                return self.parent_options[i]
            if priberam.word_exists( self.parent_options[i] ):
                return self.parent_options[i]
        if Settings.VERBOSE and Settings.DONT_ASK: 
            print "\tCouldn't decide which one is correct:", ', '.join(self.parent_options)
