/* eslint-disable react/jsx-filename-extension */
import React, { useState, useEffect } from 'react';
import { Review } from './Review';

function App() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    // useEffect is used along with fetch to ensure that user's comments
    // are loaded upon page load.
    fetch('/user_reviews')
      .then((response) => response.json())
      .then((data) => {
        setReviews(data);
      });
  }, []);

  function changeMessage(newMessage) {
    // This function is intended to be called to show a success message
    // once the server has accepted the user's changes and clear the
    // message once a change has been made to a rating.
    const div = document.getElementById('message');
    div.textContent = newMessage;
  }

  function handleDelete(reviewId) {
    const newReviews = [];
    reviews.forEach((review) => {
      if (review.review_id !== reviewId) newReviews.push(review);
    });
    setReviews(newReviews);

    changeMessage('');
  }

  function handleChange(reviewId, newValue) {
    const newReviews = [];
    reviews.forEach((review) => {
      // We are only looking for the review with the passed in reviewId
      // because that is the only review item that has been changed/deleted
      if (review.review_id === reviewId) {
        const reviewCopy = JSON.parse(JSON.stringify(review));
        reviewCopy.rating = newValue;
        newReviews.push(reviewCopy);
      } else {
        newReviews.push(review);
      }
    });
    setReviews(newReviews);
    changeMessage('');
  }

  async function saveReviews() {
    // We're saving the response we get from fetch so that we can
    // determine if it was successful or not so that we can update
    // the user to let them know if their changes were properly saved
    const response = await fetch('/modify_reviews', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(reviews),
    });
    if (response.ok) {
      changeMessage('Changes saved!');
    } else {
      changeMessage('Something went wrong...');
    }
  }

  function createReview(reviewObj) {
    return (
      <Review
        key={reviewObj.reviewId}
        content={reviewObj.content}
        rating={reviewObj.rating}
        movieId={reviewObj.movie_id}
        reviewId={reviewObj.review_id}
        deleteFunc={() => handleDelete(reviewObj.review_id)}
        changeFunc={(e) => handleChange(reviewObj.review_id, e)}
      />
    );
  }

  return (
    <div className="App">
      <h2>User Reviews</h2>
      <ul className="review_list">
        {reviews.map((review) => createReview(review))}
      </ul>
      <button type="button" onClick={() => saveReviews()}>Save</button>
      <div id="message" />
    </div>
  );
}

export default App;
