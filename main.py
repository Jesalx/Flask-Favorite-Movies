"""
Project 1 - Main flask app
Jpatel152@student.gsu.edu
"""
import flask
import tmdb

app = flask.Flask(__name__)

MOVIE_IDS = [
    1124,  # The Prestige
    68718,  # Django Unchained
    335984,  # Blade Runner 2049
    13183,  # Watchmen
    496243,  # Parasite
]


@app.route("/")
def main():
    """
    TODO: Ask professor if we need docstring for main function
    """
    movie = tmdb.get_random_favorite_movie()
    return flask.render_template("index.html",
                                 movie_title=movie["title"],
                                 movie_description=movie["description"],
                                 movie_genres=movie["genres"],
                                 movie_poster_url=movie["poster_url"])


app.run(debug=True)
