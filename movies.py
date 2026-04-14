import requests
from config import OMDB_API_KEY

def get_movies(search="action"):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&s={search}&type=movie"
    data = requests.get(url).json()

    return data.get("Search", [])
