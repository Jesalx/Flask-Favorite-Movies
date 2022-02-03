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
    return flask.render_template("index.html")


app.run(debug=True)