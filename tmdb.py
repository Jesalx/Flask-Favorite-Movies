"""
TODO: Write useful module docstring here
"""
import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
TMDB_KEY = os.getenv("TMDB_KEY")
BASE_URL = "https://api.themoviedb.org/3/movie/"
POSTER_URL = "https://www.themoviedb.org/t/p/w1280"
query_params = {"api_key": TMDB_KEY}

MOVIE_IDS = [
    1124,  # The Prestige
    68718,  # Django Unchained
    335984,  # Blade Runner 2049
    13183,  # Watchmen
    496243,  # Parasite
]


def get_movie_from_tmdb_id(tmdb_id):
    """
    TODO: Write docstring
    """
    url = BASE_URL + str(tmdb_id)
    response = requests.get(url, params=query_params)
    results = response.json()
    return results


def main():
    """
    TODO: Write docstring
    """

    movie_object = get_movie_from_tmdb_id(MOVIE_IDS[0])

    # Title
    print(f"Title: {movie_object['title']}")

    # Description (Might be str OR null)
    print(f"Description: {movie_object['overview']}")

    # Genres
    genres = [obj["name"] for obj in movie_object["genres"]]
    print(f'Genres: {", ".join(genres)}')

    # Poster url (This doesn't give the full path and needs
    # to be appended to another path)
    print(f"Poster url: {POSTER_URL + movie_object['poster_path']}")


if __name__ == "__main__":
    main()
