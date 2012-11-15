#!/usr/bin/env python
# encoding: utf-8
import requests, re, simplejson, sys, codecs

reload(sys)
sys.setdefaultencoding( "utf-8" )

def dict_to_str(d):
    x = [u"\t'%s': '%s',\n" %(k,v) for k,v in d.iteritems() if k and v]
    return "{\n" + "".join(x) + "}"
    
def write_to_file(filename="words_OA.js"):
    js_file = codecs.open( filename, "w", "utf-8" )
    js_file.write( dict_to_str(words) )
    js_file.close()
    

url = "http://www.portaldalinguaportuguesa.org/?action=novoacordo&act=list&letter=%s&version=pe"
alphabet = [chr(i) for i in range(97, 123)]

table_regex    = r"<tr><th>Ortografia Antiga<th>Ortografia Nova<th>Notas(.*)<p></table>"
old_word_regex = r"<td title='forma antiga'>(.*)<td>.*<td>"
new_word_regex = r"<td title='forma antiga'>.*<td>(.*)<td>"

words = {}
for char in alphabet:
    try:
        response  = requests.get( url%char ).content.replace( '\n', '' )
        table     = re.findall( table_regex, response )[0].split( '<tr' )
        old_words = [ re.findall( old_word_regex, row )[0] for row in table if row ]
        new_words = [ re.findall( new_word_regex, row )[0] for row in table if row ]
        words.update( dict( zip(new_words, old_words) ) )
    except IndexError:
        continue
       
write_to_file() 
