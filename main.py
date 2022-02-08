"""
Project 1 - Main flask app
Jpatel152@student.gsu.edu
"""
import flask
import tmdb

app = flask.Flask(__name__)


@app.route("/")
def main():  # pylint: disable=missing-function-docstring
    movie = tmdb.get_random_favorite_movie()
    return flask.render_template("index.html",
                                 movie_title=movie["title"],
                                 movie_tagline=movie["tagline"],
                                 movie_description=movie["description"],
                                 movie_genres=movie["genres"],
                                 movie_poster_url=movie["poster_url"],
                                 movie_wiki_url=movie["wiki_url"])


app.run(debug=True)
