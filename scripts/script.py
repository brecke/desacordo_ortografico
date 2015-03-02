#!/usr/bin/env python
# encoding: utf-8
import sys
from utils.settings    import Settings
from utils.words.words import Words
from utils.file        import File
from utils.http.iltec  import PortalLinguaPortuguesa

reload(sys)
sys.setdefaultencoding( "utf-8" )


def get_words():
    all_words = {}
    for each in PortalLinguaPortuguesa.get_words():
        words = Words(each).with_variants()
        all_words.update( words )
    return all_words

if __name__ == '__main__':
    Settings.check()
    File.write( get_words() )   
