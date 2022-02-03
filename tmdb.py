"""
TODO: Write useful module docstring here
"""
import os
import random
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

    # TODO: Write a way to handle the issue if the server doesn't respond
    # TODO: Handle the cases where the movie is missing description or
    # poster urls, or ask professor if thats even necessary.
    url = BASE_URL + str(tmdb_id)
    response = requests.get(url, params=query_params)
    movie_object = response.json()
    movie_info = dict()
    movie_info["title"] = movie_object["title"]
    movie_info["description"] = movie_object["overview"]
    movie_info["genres"] = [obj["name"] for obj in movie_object["genres"]]
    movie_info["poster_url"] = POSTER_URL + movie_object["poster_path"]
    return movie_info


def get_random_favorite_movie():
    """
    Returns movie_info for random movie in favorite movies
    """
    return get_movie_from_tmdb_id(random.choice(MOVIE_IDS))


def main():
    """
    TODO: Write docstring
    """

    movie_info = get_movie_from_tmdb_id(MOVIE_IDS[0])
    for key, val in movie_info.items():
        print(f"{key}: {val}")


if __name__ == "__main__":
    main()
