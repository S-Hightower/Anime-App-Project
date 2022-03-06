from jikanpy import Jikan
jikan = Jikan()

from requests import Session

class Show:
    def searchAnime(title):
        jikan = Jikan()

        result = jikan.search('anime', title)
        print(result)

