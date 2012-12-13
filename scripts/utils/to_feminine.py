#!/usr/bin/env python
# encoding: utf-8
from utils.__init__ import return_tuple

@return_tuple
def to_feminine(word):
    #http://www.flip.pt/FLiP-On-line/Gramatica/Morfologia-Partes-do-discurso/Genero/Feminino-dos-substantivos-e-dos-adjectivos.aspx
    if word.endswith("o"):
        if word=="melro":     return "melroa"
        if word=="marido":    return "mulher"
        if word=="genro":     return "nora"
        if word=="padrasto":  return "madrasta"
        if word=="carneiro":  return "ovelha"
        if word=="padrinho":  return "madrinha"
        if word=="diácono":   return "diaconisa"
        if word=="galo":      return "galinha"
        if word=="avõ":       return "avó"
        return word[:-1]+"a"
    if word.endswith("ão"):
        if word=="barão":     return "baronesa"
        if word=="cão":       return "cadela"
        if word=="ladrão":    return "ladra"
        if word=="lebrão":    return "lebre"
        if word=="perdigão":  return "perdiz"
        if word=="tecelão":   return "tecedeira"
        if word=="zângão":    return "abelha"
        size = len("ão")
        return word[:-size]+"ã", word[:-size]+"oa", word[:-size]+"ona"
    if word.endswith("eu"):
        if word=="reu":     return "ré"
        if word=="judeu":   return "judia"
        if word=="sandeu":  return "sandia"
        return word[:-2]+"eia"
    if word.endswith("u"):
        if word=="mau":     return "má"
        if word=="peru":    return "perua"
        if word=="cru":     return "crua"
        if word=="europeu": return "europeia"
        if word=="pigmeu":  return "pigmeia"
        if word=="plebeu":  return "plebeia"
        if word=="ilhéu":   return "ilhoa"
        return word[:-1]+"a"
    if word.endswith("or"):
        if word=="cantador":    return "cantadeira"
        if word=="caiador":     return "caiadeira"
        if word=="cardador":    return "cardadeira"
        if word=="bailador":    return "bailadeira"
        if word=="comendador":  return "comendadeira"
        if word=="vendedor":    return "vendedeira"
        if word=="dançador":    return "dançadeira"
        if word=="lavrador":    return "lavradeira"
        if word=="ator":        return "atriz"
        if word=="actor":       return "actriz"
        if word=="embaixador":  return "embaixatriz"
        if word=="motor":       return "motriz"
        if word=="imperador":   return "imperatriz"
        if word=="prior":       return "prioresa"
        return word+"a"
    if word.endswith("ês"):
        if word in ["cortês", "pedrês"]: return word
        size = len("ês")
        return word[:-size]+"esa"
    if word.endswith("z"):
        if word in ["andaluz", "juiz", "aprendiz"]: return word+"a"
        return word
    if word=="abade":       return "abadessa"
    if word=="alcaide":     return "alcaidessa"
    if word=="bode":        return "cabra"
    if word=="conde":       return "condessa"
    if word=="cônsul":      return "consulesa"
    if word=="deus":        return "deusa"
    if word=="dom":         return "dona"
    if word=="duque":       return "duquesa"
    if word=="elefante":    return "elefanta"
    if word=="frade":       return "soror"
    if word=="frei":        return "freira"
    if word=="frere":       return "freira"
    if word=="herói":       return "heroína"
    if word=="hóspede":     return "hóspede"
    if word=="infante":     return "infanta"
    if word=="mestre":      return "mestra"
    if word=="monge":       return "monja"
    if word=="papa":        return "papisa"
    if word=="parente":     return "parenta"
    if word=="poeta":       return "poetisa"
    if word=="profeta":     return "profetisa"
    if word=="príncipe":    return "princesa"
    if word=="rapaz":       return "rapariga"
    if word=="rei":         return "rainha"
    if word=="sacerdote":   return "sacerdotisa"
    if word=="sultão":      return "sultana"
    if word=="visonde":     return "viscondessa"
    if word=="zagal":       return "zagala"
    return word
    
def add_feminines(dic):
    l = []
    for k,v in dic.iteritems():
        if not k or not v:
            continue
        k_feminine, v_feminine = to_feminine(k), to_feminine(v)
        if len(k_feminine) != len(v_feminine):
            print "WARNING: %s != %s" %(k_feminine, v_feminine)
        l += zip( k_feminine, v_feminine )
    dic.update( dict(l) )
