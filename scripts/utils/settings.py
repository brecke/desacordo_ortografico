#!/usr/bin/env python
# encoding: utf-8
import argparse

class Settings(object):
    DONT_ASK = False
    VERBOSE  = False
    LAZY     = False
    PRIBERAM = True
    
    @classmethod
    def check(self):
        parser = argparse.ArgumentParser(description='Get list of words affected by the new AO')
        parser.add_argument('--dont-ask', dest='dont_ask', action='store_const', const=True,  default=False,
                            help='ask the user for the right plural/feminine form in case of doubt (defaults to False)')
        parser.add_argument('--verbose',  dest='verbose',  action='store_const', const=True,  default=False,
                            help='keep the user informed of what is happening (defaults to False)')
        parser.add_argument('--lazy',     dest='lazy',     action='store_const', const=True,  default=False,
                            help='add a 1second interval between request to *proberam.pt* (defaults to False)')
        parser.add_argument('--priberam', dest='priberam', action='store_const', const=False, default=True,
                            help='ask first to priberam before trying to guess (defaults to True)')
        
        args = parser.parse_args()
        self.DONT_ASK = args.dont_ask
        self.VERBOSE  = args.verbose
        self.LAZY     = args.lazy
        self.PRIBERAM = args.priberam
    