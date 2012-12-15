#!/usr/bin/env python
# encoding: utf-8
import codecs

class File(object):
    filename = "mappings.js"
        
    @classmethod    
    def __dict_to_str(self, d):
        l = []
        for k,v in d.iteritems():
            try:
                if k and v:
                    l.append( u"\t'"+unicode(k)+"': '"+unicode(v)+"',\n" )
            except UnicodeDecodeError:
                continue         
        return u"var mappings = {\n" + "".join(l) + u"}"

    @classmethod
    def write(self, dic):
        file_ = codecs.open( self.filename, "w", "utf-8" )
        file_.write( self.__dict_to_str(dic) )
        file_.close()
    
    