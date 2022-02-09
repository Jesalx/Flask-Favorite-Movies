"""
Project 1 - Main flask app
Jpatel152@student.gsu.edu
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


# Uncomment following if running locally and comment if running on Heroku
# app.run(debug=True)

# Uncomment following if running on Heroku and comment if running locally
app.run(host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True)
