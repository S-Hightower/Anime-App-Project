from jikanpy import Jikan
jikan = Jikan()

from requests import Session

class Show:
    def __init__(self):
        self.apiurl = 'https://api.jikan.moe'
        self.Session = Session()

    def getAnime(self):
        url = self.apiurl + '/v4/anime/'
        r = self.Session.get(url)
        data = r.json['data']
        return data

