#!/usr/bin/env python
# encoding: utf-8
import requests, re, argparse, time, sys
from utils.settings    import Settings
from utils.words       import Words
from utils.file        import File

reload(sys)
sys.setdefaultencoding( "utf-8" )

ALPHABET = [chr(i) for i in range(97, 123)]

def run():
    all_words = {}
    for char in ALPHABET:
        try:
            if Settings.VERBOSE:
                print ">> Getting words starting with '%s'." %char.upper()
            
            words = Words.get( char )
            words.add_conjugations()
            words.add_feminines()
            words.add_plurals()
            words.remove_redundancy()
            
            all_words.update( words )
        except IndexError:
            continue
    return all_words

if __name__ == '__main__':
    Settings.check()
    words = run()
    File.write( words ) 
    
