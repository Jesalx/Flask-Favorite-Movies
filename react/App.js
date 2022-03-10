/* eslint-disable */
import { useState, useRef, useEffect } from 'react';
import { Review } from './Review.js'

function App() {
    const [reviews, setReviews] = useState([]);


    useEffect(() => {
        // setReviews()
        fetch('/user_reviews')
            .then(response => response.json())
            .then(data => {
                setReviews(data)
                console.log(reviews)
            })
    }, [])

    function handleDelete(reviewId){
        const newReviews = []
        for(const review of reviews){
            if(review["review_id"] !== reviewId){
                newReviews.push(review)
            }
        }
        setReviews(newReviews)
    }

    function handleChange(reviewId, newValue){
        const newReviews = []
        for(const review of reviews){
            if(review["review_id"] === reviewId){
                const reviewCopy = JSON.parse(JSON.stringify(review))
                reviewCopy["rating"] = newValue
                newReviews.push(reviewCopy)
            } else {
                newReviews.push(review)
            }
        }
        setReviews(newReviews)
    }

    function saveReviews(){
        console.log(reviews)
    }

    function createReview(reviewObj) {
        return <Review
            key={reviewObj["reviewId"]}
            content={reviewObj["content"]}
            rating={reviewObj["rating"]}
            movieId={reviewObj["movie_id"]}
            reviewId={reviewObj["review_id"]}
            deleteFunc={() => handleDelete(reviewObj["review_id"])}
            changeFunc={(e) => handleChange(reviewObj["review_id"], e)}
        />
    }

    return (
        <div className="App">
            <h2>User Reviews</h2>
            <ul>
                {reviews.map(review => createReview(review))}
            </ul>
            <button type="button" onClick={() => saveReviews()}>Save</button>
        </div>
    );
}

export default App;
