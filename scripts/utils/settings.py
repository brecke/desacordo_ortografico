#!/usr/bin/env python
# encoding: utf-8
import argparse

class Settings(object):
    DONT_ASK    = False
    VERBOSE     = False
    NO_PRIBERAM = False
    
    @classmethod
    def check(self):
        parser = argparse.ArgumentParser(description='Get list of words affected by the new AO')
        parser.add_argument('--dont-ask', dest='dont_ask', action='store_const', const=True,  default=False,
                            help='do not ask the user for the right plural/feminine form in case of doubt (defaults to False)')
        parser.add_argument('--verbose',  dest='verbose',  action='store_const', const=True,  default=False,
                            help='keep the user informed of what is happening (defaults to False)')
        parser.add_argument('--no-priberam', dest='no_priberam', action='store_const', const=True, default=False,
                            help='try to guess before asking *priberam.pt* (defaults to False)')
        
        args = parser.parse_args()
        self.DONT_ASK    = args.dont_ask
        self.VERBOSE     = args.verbose
        self.NO_PRIBERAM = args.no_priberam
    