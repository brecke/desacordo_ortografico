#!/usr/bin/env python
# encoding: utf-8
import codecs

class File(object):    
    def __init__(self, filename):
        self.filename = filename
    
    def write(self, dic):
        
        def get_text(): 
            lines = []
            for key,value in dic.iteritems():
                try:
                    if key and value:
                        lines.append( u"\t'"+unicode(key)+"': '"+unicode(value)+"'" )
                except UnicodeDecodeError:
                    continue         
            return u"var mappings = {\n" + ",\n".join(lines) + u"}"
        
        file_ = codecs.open( self.filename, "w", "utf-8" )
        file_.write( get_text() )
        file_.close()
    
    