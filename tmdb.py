"""
This module works with the TMDB API to generate useful movie information
when provided with a TMDB movie id
"""
import os
import random
import requests
from dotenv import find_dotenv, load_dotenv
import wiki_link

load_dotenv(find_dotenv())
TMDB_KEY = os.getenv("TMDB_KEY")
BASE_URL = "https://api.themoviedb.org/3/movie/"
CONFIG_URL = "https://api.themoviedb.org/3/configuration"
POSTER_SIZE = "original"
query_params = {"api_key": TMDB_KEY}

MOVIE_IDS = [
    1124,  # The Prestige
    68718,  # Django Unchained
    335984,  # Blade Runner 2049
    13183,  # Watchmen
    496243,  # Parasite
    245891,  # John Wick
    7453,  # The Hitchhiker's Guide to the Galaxy
    4935,  # Howl's Moving Castle
    98,  # Gladiator
]

FALLBACK_MOVIE = {
    "movie_id": 0,
    "title": "No title",
    "description": "No description",
    "tagline": "No tagline",
    "genres": "No genres",
    "poster_url": "",
    "release_year": "No release year",
    "wiki_url": "",
}


def get_movie_from_tmdb_id(tmdb_id):
    """
    Returns dictionary with the following information about the movie:
    title, description, tagline, genres, poster_url, release_year, wiki_url
    """
    url = BASE_URL + str(tmdb_id)
    try:
        response = requests.get(url, params=query_params)
    except requests.exceptions.RequestException:
        return FALLBACK_MOVIE

    # Idea for using the status code from https://stackoverflow.com/a/15258759
    if response.status_code != 200:
        return FALLBACK_MOVIE

    movie_object = response.json()
    movie_info = FALLBACK_MOVIE.copy()
    movie_info["id"] = tmdb_id
    movie_info["title"] = movie_object["title"]
    movie_info["description"] = movie_object["overview"]
    movie_info["tagline"] = movie_object["tagline"]
    movie_info["genres"] = [genre["name"] for genre in movie_object["genres"]]

    # Getting Poster URL
    poster_url_response = requests.get(CONFIG_URL, params=query_params)
    poster_base_url = poster_url_response.json()["images"]["base_url"]
    poster_url = poster_base_url + POSTER_SIZE + movie_object["poster_path"]
    movie_info["poster_url"] = poster_url

    # Getting movie release year stored in format: YEAR-MONTH-DAY
    movie_info["release_year"] = movie_object["release_date"].split("-")[0]

    # Getting Wikipedia link for movie
    movie_page_id = wiki_link.get_wiki_page_id(
        movie_info["title"], movie_info["release_year"]
    )
    movie_info["wiki_url"] = wiki_link.get_wiki_link(movie_page_id)

    return movie_info


def get_random_favorite_movie():
    """
    Returns movie_info for random movie in MOVIE_IDS
    """
    return get_movie_from_tmdb_id(random.choice(MOVIE_IDS))


def main():  # pylint: disable=missing-function-docstring
    movie = get_random_favorite_movie()
    for key, val in movie.items():
        print(f"{key}: {val}")


if __name__ == "__main__":
    main()
