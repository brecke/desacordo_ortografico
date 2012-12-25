#!/usr/bin/env python
# encoding: utf-8

class WordNotRecognized(Exception):
    pass


class WordUnknown(Exception):
    pass


class PluralUnknown(Exception):
    pass

        
class PluralNotFound(Exception):
    pass


class VerbNotFound(Exception):
    pass


class NoInputGiven(Exception):
    pass


class MultipleOptions(Exception):
    def __init__(self, *args):
        self.options  = args
        
    def ask_priberam(self, priberam):
        for option in self.options:
            if priberam.word_exists( option ):
                return option
