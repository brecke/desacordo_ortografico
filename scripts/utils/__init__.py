#!/usr/bin/env python
# encoding: utf-8
from utils.settings import Settings

def user_input(options):
    if Settings.DONT_ASK:
        return options[0]
    print "\nDon't know which one is right:\n%s (default)" %options[0]
    for i in options[1:]:
        print i
    return raw_input("Write the right answer: ") or options[0]

class verbosity(object):
    def __init__(self, text):
        self.text = text
        
    def __call__(self, f):
        def wrapper(*args, **kwargs):
            if Settings.VERBOSE:
                print '> '+self.text
            return f(*args, **kwargs)
        return wrapper
