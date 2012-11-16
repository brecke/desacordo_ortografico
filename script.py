#!/usr/bin/env python
# encoding: utf-8
import requests, re, simplejson, sys, codecs

reload(sys)
sys.setdefaultencoding( "utf-8" )

def dict_to_str(d):
    x = [u"\t'"+unicode(k)+"': '"+unicode(v)+"',\n" for k,v in d.iteritems() if k and v]
    return u"var mappings = {\n" + "".join(x) + u"}"
    
def write_to_file(dic, filename="mappings.js"):
    js_file = codecs.open( filename, "w", "utf-8" )
    js_file.write( dict_to_str(dic) )
    js_file.close()
    
def plural(word):
    if word.endswith("ão"):
        size = len("ão")
        return word[:-size]+"ãos", word[:-size]+"ães", word[:-size]+"ões"
    elif word.endswith("m"):
        return word[:-1]+"ns",
    elif word.endswith("il"):
        return word[:-2]+"is", word[:-2]+"eis"
    elif word.endswith("al"):
        if word=="mal": 
            return "males",
        elif word=="cal": 
            return "cales",
        elif word=="aval": 
            return "avais",
        return word[:-1]+"is",
    elif word.endswith("el"):
        if word=="mel":
            return "meles",
        elif word=="fel":
            return "feles",
        return word[:-1]+"is",
    elif word.endswith("ol"):
        if word=="mol":
            return "moles",
        return word[:-1]+"is",
    elif word.endswith("ul"):
        if word=="cônsul":
            return "cônsules",
        return word[:-1]+"is",
    elif word.endswith("r") or word.endswith("z"):
        return word[:-1]+"es",
    elif word.endswith("n"):
        return word+"es", word+"s"
    elif word.endswith("ens"):
        return word,
    elif word.endswith("s"):
        if word in ["cós", "cais", "xis"]:
            return word,
        return word[:-1]+"es",
    else:
        return word+"s",
        

def add_plurals_to_dict(dic):
    l = []
    for k,v in dic.iteritems():
        l += zip( plural( k ), plural( v ) )
    dic.update( dict( l ) )
    

url = "http://www.portaldalinguaportuguesa.org/?action=novoacordo&act=list&letter=%s&version=pe"
alphabet = [chr(i) for i in range(97, 123)]

table_regex    = r"<tr><th>Ortografia Antiga<th>Ortografia Nova<th>Notas(.*)<p></table>"
old_word_regex = r"<td title='forma antiga'>(.*)<td>.*<td>"
new_word_regex = r"<td title='forma antiga'>.*<td>(.*)<td>"

all_words = {}
for char in alphabet:
    words = {}
    try:
        response  = requests.get( url%char ).content.replace( '\n', '' )
        table     = re.findall( table_regex, response )[0].split( '<tr' )
        
        old_words = [ re.findall( old_word_regex, row )[0] for row in table if row ]
        new_words = [ re.findall( new_word_regex, row )[0] for row in table if row ]
        
        words.update( dict( zip(new_words, old_words) ) )
        add_plurals_to_dict( words )
        all_words.update( words )
    except IndexError:
        continue
       
write_to_file( all_words ) 
