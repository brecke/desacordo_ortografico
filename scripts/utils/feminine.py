#!/usr/bin/env python
# encoding: utf-8
from utils import user_input
import re


class Feminine(object):
    """
    http://www.flip.pt/FLiP-On-line/Gramatica/Morfologia-Partes-do-discurso/Genero/Feminino-dos-substantivos-e-dos-adjectivos.aspx
    """
    
    @classmethod
    def get(self, word):
        if word.endswith("ão"):
            exceptions = {
                "barão": "baronesa", "cão": "cadela", "ladrão": "ladra", "lebrão": "lebre",
                "perdigão": "perdiz", "tecelão": "tecedeira", "zângão": "abelha",
            }
            size    = len("ão")
            options = [word[:-size]+"â", word[:-size]+"oa", word[:-size]+"ona"]
            return exceptions[word] if word in exceptions else user_input( options )
        if word.endswith("o"):
            exceptions = {
                "melro": "melroa", "marido": "mulher", "genro": "nora", "padrasto": "madrasta",
                "carneiro": "ovelha", "padrinho": "madrinha", "diácono": "diaconisa",
                "galo": "galinha", "avõ": "avó",
            }
            return exceptions[word] if word in exceptions else word[:-1]+"a"
        if word.endswith("eu"):
            exceptions = {
                "reu": "ré", "judeu": "judia", "sandeu": "sandia"
            }
            return exceptions[word] if word in exceptions else word[:-2]+"eia"
        if word.endswith("u"):
            exceptions = {
                "mau": "má", "peru": "perua", "cru": "crua", "europeu": "europeia",
                "pigmeu": "pigmeia", "plebeu": "plebeia", "ilhéu": "ilhoa",
            }
            return exceptions[word] if word in exceptions else word[:-1]+"a"
        if word.endswith("or"):
            exceptions = {
                "cantador": "cantadeira", "caiador": "caiadeira", "cardador": "cardadeira",
                "bailador": "bailadeira", "comendador": "comendadeira", "vendedor": "vendedeira",
                "dançador": "dançadeira", "lavrador": "lavradeira", "ator": "atriz", "actor": "actriz", 
                "embaixador": "embaixatriz", "motor": "motriz","imperador": "imperatriz", "prior": "prioresa",
            }
            return exceptions[word] if word in exceptions else word+"a"
        if word.endswith("ês"):
            size = len("ês")
            return word if word in ["cortês", "pedrês"] else word[:-size]+"esa"
        if word.endswith("z"):
            return word+"a" if word in ["andaluz", "juiz", "aprendiz"] else word
        exceptions = {
            "abade": "abadessa", "alcaide": "alcaidessa", "bode": "cabra", "conde": "condessa",
            "cônsul": "consulesa", "deus": "deusa", "dom": "dona", "duque": "duquesa",
            "elefante": "elefanta", "frade": "soror", "frei": "freira", "frere": "freira",
            "herói": "heroína", "hóspede": "hóspede", "infante": "infanta", "mestre": "mestra",
            "monge": "monja", "papa": "papisa", "parente": "parenta", "poeta": "poetisa",
            "profeta": "profetisa", "príncipe": "princesa", "rapaz": "rapariga", "rei": "rainha",
            "sacerdote": "sacerdotisa", "sultão": "sultana", "visonde": "viscondessa", "zagal": "zagala",
        }
        return exceptions[word] if word in exceptions else word
    
    