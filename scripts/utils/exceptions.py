#!/usr/bin/env python
# encoding: utf-8

class WordNotRecognized(Exception):
    def __init__(self, word):
        self.word=word
    def __str__(self):
        return "Definition of the word '%s' unknown to Priberam." %self.word

class WordUnknown(Exception):
    def __init__(self, word):
        self.word=word
    def __str__(self):
        return "Word '%s' unknown to Priberam." %self.word

class PluralUnknown(Exception):
    def __init__(self, word):
        self.word=word
    def __str__(self):
        return "Plural form of word '%s' unknown to Priberam." %self.word
        
class PluralNotFound(Exception):
    def __init__(self, word):
        self.word=word
    def __str__(self):
        return "Plural form of word '%s' not parsed from Priberam." %self.word

class VerbNotFound(Exception):
    def __init__(self, word):
        self.word=word
    def __str__(self):
        return "Verb '%s' not found in Priberam. It may not be a verb" %self.word
