import requests
from config import OMDB_API_KEY, FANART_API_KEY

def omdb_details(title):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}"
    return requests.get(url).json()


def fanart_poster(imdb_id):
    url = f"https://webservice.fanart.tv/v3/movies/{imdb_id}?api_key={FANART_API_KEY}"
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        try:
            return data["movieposter"][0]["url"]
        except:
            return ""
    return ""
