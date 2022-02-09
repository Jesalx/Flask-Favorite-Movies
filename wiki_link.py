"""
This module works with the Wikipedia API to find a specific movie's page id
and also generate a working Wikipedia url from a page id
"""
import requests

BASE_URL = "https://www.wikipedia.org/w/api.php"
WIKI_URL = "https://en.wikipedia.org/?curid="


def get_wiki_page_id(title, release_year):
    """
    Returns Wikipedia page id associated with specified movie title and release year
    """
    query_params = {
        "action": "query",
        "list": "search",
        "format": "json",
        "srsearch": f"{title} {release_year} film",
    }

    response = requests.get(BASE_URL, params=query_params)
    return response.json()["query"]["search"][0]["pageid"]


def get_wiki_link(page_id):
    """
    Returns string containing Wikipedia url for the specified page_id
    """
    return WIKI_URL + str(page_id)


def main():  # pylint: disable=missing-function-docstring
    page_id = get_wiki_page_id("The Prestige", "2006")
    page_link = get_wiki_link(page_id)
    print(page_link)


if __name__ == "__main__":
    main()
