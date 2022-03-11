/* eslint-disable react/jsx-filename-extension, react/destructuring-assignment, react/prop-types */
import React from 'react';

export function Review(props) {
  return (
    <li>
      <form>
        <div>{`Movie ID: ${props.movieId}`}</div>
        <div>{`Comment: ${props.content}`}</div>
        <input type="number" min="0" max="10" value={props.rating} onChange={(e) => props.changeFunc(e.target.value)} />
        <br />
        <input className="invisible_input" type="number" value={props.reviewId} name="movie_id" readOnly />
        <button type="button" onClick={() => props.deleteFunc()}>Delete</button>
      </form>
      <br />
    </li>
  );
}

export default Review;
