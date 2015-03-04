#!/usr/bin/env python
# encoding: utf-8
from utils.consts import PREPOSITIONS, PREFIXES
from utils.exceptions import MultipleOptions


class Grammar(str):
    
    @classmethod
    def get_form(cls, word, formname):
        
        def apply_form(word, rejoin=None):
            try:
                new_word = getattr(cls(word), 'to_'+formname)()
                return rejoin( new_word ) if rejoin else new_word
            except MultipleOptions as e:
                if rejoin:
                    e.parent_options = [rejoin(each) for each in e.options]
                raise e
        
        def apply_hifen_rules(sep):
            subwords = word.split( sep )
            if len(subwords) == 2:
                return apply_form(
                    word   = subwords[1], 
                    rejoin = lambda x: sep.join([subwords[0], x])
                )
            elif len(subwords) >= 3 and subwords[1] in PREPOSITIONS:
                return apply_form( 
                    word   = subwords[0], 
                    rejoin = lambda x: sep.join([x] + subwords[1:])
                )
            return apply_form( word=word )
            
        def apply_composite_rules():
            for each in PREFIXES:
                if word.startswith( each ):
                    subword = word[len(each):]
                    if subword[0] == subword[1]:
                        return apply_form( 
                            word   = subword[1:], 
                            rejoin = lambda x: each + subword[0] + x
                        )
                    else:
                        return apply_form(
                            word   = subword, 
                            rejoin = lambda x: each + x
                        )
            return apply_form( word=word )
                
        if "-" in word:
            return apply_hifen_rules(sep="-")
        elif " " in word:
            return apply_hifen_rules(sep=" ")
        else:
            return apply_composite_rules()
    
    def to_plural(self):
        """
        http://pt.wikipedia.org/wiki/Plural
        """
        
        def apply_simple_rules():
            #TODO: terminado em ditongo oral -> words+"s"
            #TODO: nome de letras -> words+"s"
            #TODO: nome dos números excepto os terminados em "s" ou "z" -> words+"s"
            for char in ['a','e','i','o','u', "ã", "ãe"]:
                if self.endswith( char ):
                    return self+"s"
          
        def apply_special_rules():
            if self.endswith("r") or self.endswith("z"):
                return self[:-1]+"es"
            if self.endswith("n"):
                raise MultipleOptions(self+"s", self+"es")
            if self.endswith("ens"):
                return self
            if self.endswith("s"):
                return self if self in ["cós", "cais", "xis"] else  self[:-1]+"es"
            if self.endswith("al") or self.endswith("el") or self.endswith("ol") or self.endswith("ul"):
                exceptions = {
                    "mal": "males", "cal": "cales", "aval": "avais", "mel": "meles",
                    "fel": "feles", "mol": "moles", "cônsul": "cônsules",
                }
                return exceptions[self] if self in exceptions else self[:-1]+"is"
            if self.endswith("il"):
                if self=="til":
                    return "tiles"
                raise MultipleOptions(self[:-1]+"s", self[:-2]+"eis")
            if self.endswith("m"):
                return self[:-1]+"ns"
            if self.endswith("x"):
                return self+"es" if self in ["fax", "fénix"] else self
            if self.endswith("ão"):
                size = len("ão")
                raise MultipleOptions(self[:-size]+"ões", self[:-size]+"ãos", self[:-size]+"ães")
        
        for rules in [apply_special_rules, apply_simple_rules]:
            plural = rules()
            if plural:
                return plural
        return self+"s"
    
        
    def to_feminine(self):
        """
        http://www.flip.pt/FLiP-On-line/Gramatica/Morfologia-Partes-do-discurso/Genero/Feminino-dos-substantivos-e-dos-adjectivos.aspx
        """
        if self.endswith("ão"):
            size       = len("ão")
            exceptions = {
                "barão": "baronesa", "cão": "cadela", "ladrão": "ladra", "lebrão": "lebre",
                "perdigão": "perdiz", "tecelão": "tecedeira", "zângão": "abelha",
            }
            if self in exceptions:
                return exceptions[self]
            raise MultipleOptions(self[:-size]+"ã", self[:-size]+"oa", self[:-size]+"ona")
        if self.endswith("o"):
            exceptions = {
                "melro": "melroa", "marido": "mulher", "genro": "nora", "padrasto": "madrasta",
                "carneiro": "ovelha", "padrinho": "madrinha", "diácono": "diaconisa",
                "galo": "galinha", "avõ": "avó",
            }
            return exceptions[self] if self in exceptions else self[:-1]+"a"
        if self.endswith("eu"):
            exceptions = {
                "reu": "ré", "judeu": "judia", "sandeu": "sandia"
            }
            return exceptions[self] if self in exceptions else self[:-2]+"eia"
        if self.endswith("u"):
            exceptions = {
                "mau": "má", "peru": "perua", "cru": "crua", "europeu": "europeia",
                "pigmeu": "pigmeia", "plebeu": "plebeia", "ilhéu": "ilhoa",
            }
            return exceptions[self] if self in exceptions else self[:-1]+"a"
        if self.endswith("or"):
            exceptions = {
                "cantador": "cantadeira", "caiador": "caiadeira", "cardador": "cardadeira",
                "bailador": "bailadeira", "comendador": "comendadeira", "vendedor": "vendedeira",
                "dançador": "dançadeira", "lavrador": "lavradeira", "ator": "atriz", "actor": "actriz", 
                "embaixador": "embaixatriz", "motor": "motriz","imperador": "imperatriz", "prior": "prioresa",
            }
            return exceptions[self] if self in exceptions else self+"a"
        if self.endswith("ês"):
            size = len("ês")
            return self if self in ["cortês", "pedrês"] else self[:-size]+"esa"
        if self.endswith("z"):
            return self+"a" if self in ["andaluz", "juiz", "aprendiz"] else self
        exceptions = {
            "abade": "abadessa", "alcaide": "alcaidessa", "bode": "cabra", "conde": "condessa",
            "cônsul": "consulesa", "deus": "deusa", "dom": "dona", "duque": "duquesa",
            "elefante": "elefanta", "frade": "soror", "frei": "freira", "frere": "freira",
            "herói": "heroína", "hóspede": "hóspede", "infante": "infanta", "mestre": "mestra",
            "monge": "monja", "papa": "papisa", "parente": "parenta", "poeta": "poetisa",
            "profeta": "profetisa", "príncipe": "princesa", "rapaz": "rapariga", "rei": "rainha",
            "sacerdote": "sacerdotisa", "sultão": "sultana", "visonde": "viscondessa", "zagal": "zagala",
        }
        return exceptions[self] if self in exceptions else self


class Plural(object):
    @classmethod
    def get(cls, word):
        return Grammar.get_form( word, 'plural' )


class Feminine(object):
    @classmethod
    def get(cls, word):
        return Grammar.get_form( word, 'feminine' )
