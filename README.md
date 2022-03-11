# Milestone 3

This milestone focuses on having React communicate with a flask server to add client-side logic to the web app.

To get to the new react page created for this milestone you click the button in the upper-right corner of the root page (default page that loads random movies) that has your username in it.

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

## Hardest Part

The hardest part of this assignment for me was handling the relationship between React components. It was pretty difficult at first for me to wrap my head around the way we need to pass down functions to our components using props and how the function we passed down should interact with its parent component. I would say that struggling with this concept was particularly valuable because painstakingly finding a method that worked finally let the concept sink in.

## Technical Issues

- One issue that I encountered during this milestone was sending my modified json back to the flask server once the user had made their changes. At first I tried to make an html form button that sent the request itself, but it didn't work properly for many reasons. One of those reasons being that it would reload the page even when the required behavior is that it doesn't do that. After not getting anywhere with that it made more sense to make a button in the react app that would just run a function that sent the request using fetch, especially since this function would be able to directly access the updated state of reviews easily.
- One issue that I encountered during this milestone was using `useState()` to properly maintain the user's reviews and change them when the user deleted or modified the rating. Initially, I tried to pass down functions as props that would manually change one review item in the array, but this ended up not working. It was also quite difficult for me to wrap my head around what functions I wanted to send down to my review component and what exactly they should do. After looking back at the tic-tac-toe example I decided to scrap everything I was doing with trying to change individual reviews and created a `handleDelete(review_id)` and `handleChange(reviewId, newValue)` function which worked similarly to the tic-tac-toe example and passed those down as props.
- One issue that I encountered during this milestone was using fetch properly to receive the json data from my flask server. My original attempt involved creating a new async function and using the await keyweyword instead of using `.then()` like the milestone 3 example used. I had a lot of issues with this where even though I was using await to ensure completion before the next step there were issues were various issues where the function wouldn't return the expected values. I ended up solving this by reevaluating whether I wanted to continue the function I was currently doing or move to a method more similar to the milestone example. I ended up following what the milestone example did for this issue which worked better.

## Known Problems

- An issue that this milestone currently has is that clicking submit multiple times in the review section leads to multiple review submissions.
- An issue that I'm not sure about is how I'm handling the server response in `tmdb.py`. If the app doesn't get status code 200 then it will return a bunch of pretty useless default information, but I would have to do more research to know if there are other status codes that are still viable and would have provided the relevant information.
- An issue that I'm still not sure about is how the default values for the movie information should look. Right now I have it so the default values are clearly not movie information, but I don't know if it would be better to just hardcode the information for one movie and just set that as the default.

## Future Improvements

- I think one important future improvement will be having the average rating of the movie be calculated using only the latest review per user. The way that it currently works is that every review, regardless of who posted it, is counted equally.
- I think another future improvement would be a small search bar at the top which would allow you to search a movie through the tmdb API. It would take the API information and display some links that the user could select and then load the milestone 2 page for that movie.
- I think that an interesting future improvement would be to split the webpage into thirds and have a different movie's information populate each third of the page. A cool extension of this feature would be that if the page is wide enough more movies will be loaded and if the page shrinks then the page will also lower the amount of movies shown.
