# Flask - Favorite Movies

This project is a small website using [Flask](https://flask.palletsprojects.com/en/2.1.x/) that dynamically generates a page with information about a random movie that I enjoyed along with allowing the posting of reviews by signed in users.

The website makes use of the [TMDB](https://www.themoviedb.org/?language=en-US) to display a poster of that movie along with other movie related information. Implementing this required the use of TMDB's API which is able to provide the title, tagline, description, genres, and poster image.

Another portion of this website generates and display a [Wikipedia](https://www.wikipedia.org) URL for the currently displayed movie. Implementing this required the use of [Wikipedia's API](https://www.mediawiki.org/wiki/API:Main_page).

The website uses [Flask-Login](https://flask-login.readthedocs.io/en/latest/) for managing user sessions, allowing the user to sign-up, login, and restrict pages to signed-in users. Password hashing and checking is done by making use of the [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/utils/#module-werkzeug.security) library.

The movie reviews are managed in a [PostgreSQL](https://www.postgresql.org) database with the use of [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

The website uses [React](https://reactjs.org) to modify/delete user review's on their profile page before sending the modifications to the Flask server.

## Installation Instructions

The first step to installation is going to be downloading the necessary files. If you wish to clone the repo you can do so by following [Github's documented instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). Otherwise you could download a zip of the repo and extract the contents where you would like them.

Once you have the repository downloaded you will need to do a couple of things. First you will need to navigate to inside the project directory and create a file called `.env`. You can create this file with

```touch .env```

or another method of your choice. Inside this file should be three lines in the following format

```text
TMDB_KEY = "YOUR_TMDB_API_KEY"
DATABASE_URL = "YOUR_DATABASE_URL"
SECRET_KEY = "YOUR_SECRET_KEY
```

where `YOUR_TMDB_API_KEY` is your [TMDB](https://developers.themoviedb.org/3/getting-started/introduction) API key, ```YOUR_DATABASE_URL``` is the url to your postgresql database that starts with ```postgresql://```, and ```YOUR_SECRET_KEY``` is a secret key that you have created.

Now that you have the right items inside of `.env` in the correct format you'll need to make sure that you have the correct packages installed for Python to run the project. To do this you can look inside the `requirements.txt` file and install each of the named packages individually, or run the command

```pip install -r requirements.txt```

To install the required npm packages you can run the command

```npm install```

Once you have all of the packages downloaded you are able to run the app with

```npm run start```
