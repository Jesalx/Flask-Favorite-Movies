/* eslint-disable */
export function Review(props) {

  return (
    <li>
      <form>
        <label>Movie ID: {props.movieId}</label><br/>
        <label>Comment: {props.content}</label><br/>
        <input type="number" min="0" max="10" value={props.rating} onChange={(e) => props.changeFunc(e.target.value)} /><br/>
        <input className="invisible_input" type="number" value={props.reviewId} name="movie_id" readOnly />
        <button type="button" onClick={() => props.deleteFunc()}>Delete</button>
      </form>
      <br/>
    </li>
  );
}

export default Review;
