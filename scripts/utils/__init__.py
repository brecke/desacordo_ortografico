#!/usr/bin/env python
# encoding: utf-8
from utils.settings   import Settings
from utils.exceptions import NoInputGiven
import sys

def user_input(options):
    if Settings.DONT_ASK:
        return options[0]
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
