# Milestone 2

This milestone is meant to familiarize myself with databases and get more practice with external libraries such as Flask-login and SQLAlchemy.

This project adds to [project1](https://github.com/csc4350-sp22/project1-jpatel152) by adding additional features. These features include implementing a system to signup/login, managing user sessions, allowing users to leave ratings/comments, and displaying user ratings/comments on the appropriate movie's webpage.

One of the most useful resources for this milestone was [Flask-login: Lengthy example](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login) which helped me get a deeper understanding of flask-login and how to use it. It also provided a good and simple example of how to do password hashing and checking by making using of the [werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/utils/#module-werkzeug.security) library.

This project differed from my project planning in a couple key ways. There were a lot of small details that I missed during planning that become clear when working on the project. For example, when writing the login page the user could enter a 1000 length string as the username which would result in an error page because I had set the string limit in the model to be 128. There were a lot of little issues like this which had to be fixed that I hadn't prepared for during project planning.

The project is hosted on Heroku and can be found at [Heroku_URL](http://powerful-thicket-45733.herokuapp.com/)

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

Once you have all of the packages downloaded you are able to run the app with

```python3 app.py```

## Technical Issues

- One issue that I encountered during this milestone was an issue with the database where I would go look at the tables and the user table would have a single item in it no matter how many user accounts I had added to the database. Everything still worked when querying for users in app.py but when querying manually I would just find the one element which was the same as the table owner. After googling `postgresql user table` I found a few stackoverflow results saying that I shouldn't name my table user because it's reserved. I renamed the user model to account which fixed the issue.
- Another technical issue that I encountered during this milestone was using the input HTML tag with `type="number"`. When the user would use the provided up-down arrows to choose an integer, or enter an integer themselves everything would work fine. If they decided to enter something like 4.0 then we would get an error page because I was giving the input directly to the table which didn't like the float. The html was preventing input like 4.1 or 4.8939, but it would be happy taking 4.0. At first I was going to implement javascript to check the input before submission, but was frustrated that there wasn't a more simple solution. Eventually I realized that it was be much simpler to typecast the string to a float then to an integer.

## Known Problems

- An issue that this milestone currently has is that clicking submit multiple times in the review section leads to multiple review submissions.
- An issue that I'm not sure about is how I'm handling the server response in `tmdb.py`. If the app doesn't get status code 200 then it will return a bunch of pretty useless default information, but I would have to do more research to know if there are other status codes that are still viable and would have provided the relevant information.
- An issue that I'm still not sure about is how the default values for the movie information should look. Right now I have it so the default values are clearly not movie information, but I don't know if it would be better to just hardcode the information for one movie and just set that as the default.

## Future Improvements

- I think one important future improvement will be having the average rating of the movie be calculated using only the latest review per user. The way that it currently works is that every review, regardless of who posted it, is counted equally.
- I think another future improvement would be a small search bar at the top which would allow you to search a movie through the tmdb API. It would take the API information and display some links that the user could select and then load the milestone 2 page for that movie.
- I think that an interesting future improvement would be to split the webpage into thirds and have a different movie's information populate each third of the page. A cool extension of this feature would be that if the page is wide enough more movies will be loaded and if the page shrinks then the page will also lower the amount of movies shown.
