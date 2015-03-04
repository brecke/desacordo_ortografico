#!/usr/bin/env python
# encoding: utf-8
import argparse

class Settings(object):
    VERBOSE     = False
    
    @classmethod
    def check(self):
        parser = argparse.ArgumentParser(description='Get list of words affected by the new AO')
        parser.add_argument('--verbose',  dest='verbose',  action='store_const', const=True,  default=False,
                            help='keep the user informed of what is happening (defaults to False)')        
        args = parser.parse_args()
        self.VERBOSE     = args.verbose
    