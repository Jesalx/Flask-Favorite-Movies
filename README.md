# Project 1

This project is meant to familiarize myself with external APIs and properly set up and use technologies such as Flask, Git, Github, and Heroku.

The project sets up a webpage that randomly selects a [TMDB](https://www.themoviedb.org/?language=en-US) movie id and displays a poster of that movie along with other related information. Implementing this required the use of TMDB's API which is able to provide the title, tagline, description, genres, and poster image.

Another portion of the project was to generate and display a [Wikipedia](https://www.wikipedia.org) URL for the currently selected movie. Implementing this required the use of [Wikipedia's API](https://www.mediawiki.org/wiki/API:Main_page).

The project is hosted on Heroku and can be found at [Project URL](https://serene-woodland-90689.herokuapp.com)

## Installation Instructions

The first step to installation is going to be downloading the necessary files. If you wish to clone the repo you can do so by following [Github's documented instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). Otherwise you could download a zip of the repo and extract the contents where you would like them.

Once you have the repository downloaded you will need to do a couple of things. First you will need to navigate to inside the project directory and create a file called `.env`. You can create this file with

```touch .env```

or another method of your choice. Inside this file should be a single line in the following format

```TMDB_KEY = "YOUR_KEY"```

where `YOUR_KEY` is your [TMDB](https://developers.themoviedb.org/3/getting-started/introduction) API key. Note that your API key must be surrounded by quotations in the file.

Now that you have your TMDB API key inside of `.env` in the correct format you'll need to make sure that you have the correct packages installed for Python to run the project. To do this you can look inside the `requirements.txt` file and install each of the named packages individually, or run the command

```pip install -r requirements.txt```

Once you have all of the packages downloaded you are able to run the app with

```python3 app.py```

## Technical Issues

- One technical issue that I encountered in this project was that I would keep adding updates to the webpage CSS, but nothing was changing. At first I thought I was just making mistakes in my CSS, but eventually realized that I had a typo in the CSS path when linking in the HTML file.
- Another technical issue that caused me a lot of trouble was converting a Wikipedia page id into a working Wikipedia URL. I spent a lot of time looking at the Wikipedia API without success. I'm sure there is still a method using the API, but I haven't found it. I eventually found that you could pass the page id as a query parameter to Wikipeida to get to the page as a simpler method rather than using the API.
- Another technical issue that was pretty annoying was trying to get the movie poster to be consistent and look nice. I had kind of weird results when experimenting with the width/height settings of the image, but after googling found a useful [stack overflow answer](https://stackoverflow.com/a/17183996) that helped by providing a solution that I liked.

## Known Problems

- A known issue that I still have in my project is handling movie cases where the movie doesn't provide necessary information like a tagline or description. None of the movies that I've experimented with have had an issue like this, but I've seen other people talk about this being an issue. I think that a simple solution might be to have default values for these like an empty string or something similar.

## Future Improvements

- I think that an interesting future improvement would be to split the webpage into thirds and have a different movie's information populate each third of the page. A cool extension of this feature would be that if the page is wide enough more movies will be loaded and if the page shrinks then the page will also lower the amount of movies shown.
