#!/usr/bin/env python
# encoding: utf-8

def to_plural(word):
    if word.endswith("ão"):
        size = len("ão")
        return word[:-size]+"ãos", word[:-size]+"ães", word[:-size]+"ões"
    if word.endswith("m"):
        return word[:-1]+"ns",
    if word.endswith("il"): 
        return word[:-2]+"is", word[:-2]+"eis"
    if word.endswith("al"):
        if word=="mal":       return "males",
        if word=="cal":       return "cales",
        if word=="aval":      return "avais",
        return word[:-1]+"is",
    if word.endswith("el"):
        if word=="mel":       return "meles",
        if word=="fel":       return "feles",
        return word[:-1]+"is",
    if word.endswith("ol"):
        if word=="mol":       return "moles",
        return word[:-1]+"is",
    if word.endswith("ul"):
        if word=="cônsul":    return "cônsules",
        return word[:-1]+"is",
    if word.endswith("r") or word.endswith("z"):
        return word[:-1]+"es",
    if word.endswith("n"):
        return word+"es", word+"s"
    if word.endswith("ens"):
        return word,
    if word.endswith("s"):
        if word in ["cós", "cais", "xis"]:  return word,
        return word[:-1]+"es",
    return word+"s",
        
def add_plurals_to_dict(dic):
    l = []
    for k,v in dic.iteritems():
        l += zip( to_plural(k), to_plural(v) )
    dic.update( dict(l) )
