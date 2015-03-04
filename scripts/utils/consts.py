#!/usr/bin/env python
# encoding: utf-8
from lxml import html


PREPOSITIONS = [
    "a", "o", "as", "às", "à", "os", "ao", "aos", "na", "nas", "no", "nos",
    "ante", "antes", "apó", "após", "saté", "com", "contra", "de", "des", 
    "da", "das", "do", "dos", "desde", "em", "entre", "perante", "por", 
    "sem", "sob", "sobre", "trás", "no", "nos", "anti", "auto", #"para"
]

PREFIXES = [
    "auto", "anti", "re", "speudo", "foto", "ultra", "sobre", "sub", "electro",
    "eletro", "bi", "contra", "info", "in", "dis", "proto", "quimio","infra", 
    "imuno", "co", "tele", "super", "retro", "hetero",
]


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
