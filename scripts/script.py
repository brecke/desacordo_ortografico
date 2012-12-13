#!/usr/bin/env python
# encoding: utf-8
import requests, re, argparse
from utils.grammar     import Grammar
from utils.settings    import Settings
from utils.file        import File

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

ALPHABET = [chr(i) for i in range(97, 123)]

def run():
    
    def get_dao( table ):
        regex = r"<td title='forma antiga'>.*<td>(.*)<td>"
        return [ re.findall( regex, row )[0].split(',')[0] for row in table if row ]
        
    def get_aao( table ):
        regex = r"<td title='forma antiga'>(.*)<td>.*<td>"
        return [ re.findall( regex, row )[0].split(',')[0] for row in table if row ]
    
    def get_html( char ):
        url = "http://www.portaldalinguaportuguesa.org/?action=novoacordo&act=list&letter=%s&version=pe"
        return requests.get( url%char ).content.replace( '\n', '' )
    
    def get_words( char ):
        regex =  r"<tr><th>Ortografia Antiga<th>Ortografia Nova<th>Notas(.*)<p></table>"
        table = re.findall( regex, get_html(char) )[0].split( '<tr' )
        return dict(zip( get_dao(table), get_aao(table) )) 

    def get_plurals(dic):
        plural = lambda d,a: (Grammar.DAO.get_plural(d), Grammar.AAO.get_plural(a))
        words  = [plural(dao, aao) for dao,aao in dic.iteritems() if dao and aao]
        return dict( words )    
    
    def get_feminine(dic):
        feminine = lambda d,a: (Grammar.DAO.get_feminine(d), Grammar.AAO.get_feminine(a))
        words    = [feminine(dao, aao) for dao,aao in dic.iteritems() if dao and aao]
        return dict( words )
        
    all_words = {}
    for char in ALPHABET:
        try:
            print ":: " + char.upper()
            words = get_words(char)
            words.update( get_feminine(words) )
            words.update( get_plurals(words) )
            all_words.update( words )
        except IndexError:
            continue
    return all_words

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--dont-ask', dest='dont_ask', action='store_const', const=True, default=False,
                       help='Should the script ask you when it is not sure of something or should it try to guess?')
    Settings.DONT_ASK = parser.parse_args().dont_ask

    words = run()
    File().write( words ) 
    
