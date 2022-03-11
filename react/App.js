/* eslint-disable react/jsx-filename-extension */
import React, { useState, useEffect } from 'react';
import { Review } from './Review';

function App() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetch('/user_reviews')
      .then((response) => response.json())
      .then((data) => {
        setReviews(data);
      });
  }, []);

  function changeMessage(newMessage) {
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

  function saveReviews() {
    fetch('/modify_reviews', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(reviews),
    });
    changeMessage('Saved.');
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
