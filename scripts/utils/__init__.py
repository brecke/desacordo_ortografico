#!/usr/bin/env python
# encoding: utf-8
from utils.settings   import Settings
from utils.exceptions import NoInputGiven
import sys, re

PREPOSITIONS = [
    "a", "o", "as", "às", "à", "os", "ao", "aos", "na", "nas", "no", "nos",
    "ante", "antes", "apó", "após", "saté", "com", "contra", "de", "des", 
    "da", "das", "do", "dos", "desde", "em", "entre", "perante", "por", 
    "sem", "sob", "sobre", "trás", "no", "nos", "anti", "auto", #"para"
]

MAIN_PREPOSITIONS = ["auto", "anti"]


def items_to_dict(items):
    words = {}
    for key,value in items:
        if not key:
            subwords = re.findall(r'(.*)[pc]([^aeiou].*)', value)
            if subwords and len(subwords[0])==2:
                words[ ''.join(subwords[0]) ] = value
            elif '-' in value:
                words[ value.replace('-', ' ') ] = value
            else:
                words[ key ] = value
        else:
            words[ key ] = value
    return words


def user_input(options):
    if Settings.DONT_ASK:
        raise NoInputGiven()
    print "\nDon't know which one is right: "
    print "\n".join( ['\t%s - %s' %(i+1, options[i]) for i in range(len(options))])
    print '\t0 - None of the above'
    index = input("Which option is the right one? ")
    if index==0 or index>len(options):
        print 'No given answer'
        raise NoInputGiven()
    print "Given answer: %s" %options[index-1]
    return options[index-1]
    

class verbosity(object):
    def __init__(self, text=None):
        self.text = text
        
    def __call__(self, f):
        def wrapper(*args, **kwargs):
            if Settings.VERBOSE:
                if self.text == None:
                    print '.',
                    sys.stdout.flush()
                else:
                    print '\n%s' %self.text
            return f(*args, **kwargs)
        return wrapper
