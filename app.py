"""
Project 1 - Main flask app
Jpatel152@student.gsu.edu

This file usees the Flask framework to create a flask app
that will contain some basic information related to a randomly
selected movie and a poster associated with the movie.
"""
import os  # pylint: disable=unused-import
import flask
import tmdb

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


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


# The following runs for me locally, but if there are issues you can
# also try: "app.run(debug=True)" without the host and port parameters
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),  # pylint: disable=invalid-envvar-default
    debug=True)
