#!/usr/bin/env python
# encoding: utf-8

#http://pt.wikipedia.org/wiki/Plural

import difflib
from utils.grammar import Grammar


def to_plural(after_ao, before_ao):
    plural_before_ao = Grammar.get_plural( before_ao, aao=True )
    plural_after_ao  = Grammar.get_plural( after_ao, aao=False )
    return plural_after_ao, plural_before_ao
    
    if "-" in before_ao and "-" not in after_ao:
        plural_after_ao = " ".join( before_ao.split("-") )
    elif "-" in after_ao:
        plural_after_ao = Grammar.get_plural( after_ao )
    else:
        plural_before_ao = Grammar.get_plural( before_ao )
        plural_after_ao  = Grammar.get_plural( after_ao )
    return plural_after_ao, plural_before_ao
                
def add_plurals(dic):
    list_of_words = []
    for after_ao,before_ao in dic.iteritems():
        if not after_ao or not before_ao:
            continue
        list_of_words.append( to_plural(after_ao, before_ao) )
    dic.update( dict(list_of_words) )
    print '----\n'
