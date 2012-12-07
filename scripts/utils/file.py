#!/usr/bin/env python
# encoding: utf-8
import codecs

class File(object):
    
    def __init__(self, filename="mappings.js"):
        self.filename = filename
        
    def __dict_to_str(self, d):
        l = []
        for k,v in d.iteritems():
            if k and v:
                try:
                    element = u"\t'"+unicode(k)+"': '"+unicode(v)+"',\n"
                    l.append( element )
                except UnicodeDecodeError:
                    print '|'
                    continue         
        #l = [u"\t'"+unicode(k)+"': '"+unicode(v)+"',\n" for k,v in d.iteritems() if k and v]
        return u"var mappings = {\n" + "".join(l) + u"}"

    def write(self, dic):
        file_ = codecs.open( self.filename, "w", "utf-8" )
        file_.write( self.__dict_to_str(dic) )
        file_.close()
    
    