import requests

class HTTP(object):
    
    @classmethod
    def get(cls, url, cookies=None, whitespaces=False):
        if cookies == None:
            cookies = {}
        try:
            response = requests.get( url, cookies=cookies ).content
        except requests.exceptions.ConnectionError:
            return cls.get(url, cookies, whitespaces)
        else:
            clean = lambda x: " ".join( x.replace( '\n', '' ).split() )
            return response if whitespaces else clean(response)
            