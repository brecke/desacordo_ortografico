#!/usr/bin/env python
# encoding: utf-8
from lxml import html


PREPOSITIONS = [
    "a", "o", "as", "às", "à", "os", "ao", "aos", "na", "nas", "no", "nos",
    "ante", "antes", "apó", "após", "saté", "com", "contra", "de", "des", 
    "da", "das", "do", "dos", "desde", "em", "entre", "perante", "por", 
    "sem", "sob", "sobre", "trás", "no", "nos", "anti", "auto", #"para"
]

PREFIXOS = [
    "auto", "anti", "re", "speudo", "foto", "ultra", "sobre", "sub", "electro",
    "eletro", "bi", "contra", "info", "in", "dis",
]

# response = requests.get('http://pt.wikipedia.org/wiki/Lista_de_prefixos_e_radicais_gregos_e_latinos')
# tree = html.fromstring(response.text)
# for each in tree.xpath('//table')[:2]:
#     table = html.fromstring( html.tostring(each) )
#     for row in table.xpath('//tr'):
#         element = html.fromstring( html.tostring(row) )
#         cells =  element.xpath('//td')
#         if cells:
#             for word in cells[0].split(','):
#                 word = word.strip()
#                 if word.endswith('-'):
#                     word = word[:-1]
#                 PREFIXOS.append( word )


PLURAL_REGEXES = [
    r'<span class="varpt">Plural: <span class="varpt"><pt><span class="aAO" [^<>]*><aAO>([^<>]*)\.?</aAO></span>',
    r'<span class="varpt">Plural: <span class="varpt"><pt>([^<>]*)\.?</pt></span>',
    r'<span class="varpt">Plural: <span class="aAO" [^<>]*"><aAO>([^<>]*)\.?</aAO></span>',
    r'<span class="varpt">Plural: ([^<>]*)\.?</span></div><span class="varpt"',
    r'<span class="varpt">Plural: ([^<>]*)\.?</span></div>',
    r'<span class=""><span class="aAO" [^<>]*><aAO>Plural: ([^<>]*)\.?</aAO></span>',
    r'<span class="">Plural: <span class="varpt"><pt>([^<>]*)\.?</pt></span>',
    r'<span class="">Plural: <span class="aAO" [^<>]*><aAO>([^<>]*)\.?</aAO></span>',
    r'<span class="varpt"><span class="aAO" [^<>]*><aAO>Plural: ([^<>]*)\.?</aAO></span>',
    r'Plural: <span class="aAO" [^<>]*><aAO>([^<>]*)\.?</aAO></span>',
    r'Plural: <span class="varpt"><pt><span class="aAO" [^<>]*><aAO>([^<>]*)\.?</aAO></span>',
    r'<span class="">Plural: ([^<>]*)\.?</span>',
    r'Plural: ([^<>]*)\.?</span></div>',
]
