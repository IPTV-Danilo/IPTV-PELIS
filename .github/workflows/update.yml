from movies import get_movies
from series import get_series
from metadata import omdb_details
from m3u import create_m3u

def run():

    items = []

    # 🎬 Movies
    movies = get_movies("action")

    for m in movies:
        details = omdb_details(m["Title"])

        items.append({
            "title": m["Title"],
            "url": f"http://YOUR_SERVER/movies/{m['imdbID']}.m3u8",
            "logo": details.get("Poster", ""),
            "group": "Movies",
            "desc": details.get("Plot", "")
        })

    # 📺 Series (TVMaze)
    series = get_series()

    for s in series:
        items.append({
            "title": s["name"],
            "url": f"http://YOUR_SERVER/series/{s['id']}.m3u8",
            "logo": s["image"]["original"] if s.get("image") else "",
            "group": "Series",
            "desc": s.get("summary", "")
        })

    create_m3u(items)


if __name__ == "__main__":
    run()
