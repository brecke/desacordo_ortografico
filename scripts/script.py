#!/usr/bin/env python
# encoding: utf-8
import requests, re, argparse, time, sys
from utils.settings    import Settings
from utils.words       import Words
from utils.file        import File

reload(sys)
sys.setdefaultencoding( "utf-8" )

ALPHABET = [chr(i) for i in range(97, 123)]

def get_words():
    all_words = {}
    for char in ALPHABET:
        try:
            if Settings.VERBOSE:
                print "\n>> Getting words starting with '%s'" %char.upper()
            words = Words.get( char ).with_variants()
            all_words.update( words )
        except IndexError:
            continue
    return all_words

if __name__ == '__main__':
    Settings.check()
    File.write( get_words() )     
