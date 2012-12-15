#!/usr/bin/env python
# encoding: utf-8

VERB_REGEX     = r'<td class="tdCONJ">(.*)<br></td>'

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

DAO_REGEX = r"<td title='forma antiga'>.*<td>(.*)<td>"

AAO_REGEX = r"<td title='forma antiga'>(.*)<td>.*<td>"

WORDS_REGEX = r"<tr><th>Ortografia Antiga<th>Ortografia Nova<th>Notas(.*)<p></table>"
