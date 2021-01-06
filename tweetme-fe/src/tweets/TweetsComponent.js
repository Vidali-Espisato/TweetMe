import React, { useState } from 'react'
import { TweetList } from "./TweetList"
import { apiTweetCreate } from "./lookup"

export function TweetsComponent(props) {
	const textAreaRef = React.createRef()
    const [newTweets, setNewTweets] = useState([])

    const handleSubmit = event => {
        event.preventDefault()
        const newVal = textAreaRef.current.value
        let tempTweet = [...newTweets]
        apiTweetCreate(newVal, (response, status) => {
            if (status === 201) {
                tempTweet.unshift(newVal)
                setNewTweets(tempTweet)
            } else {
                console.log(status, response)
                alert("An error occurred!")
            }
        })
        textAreaRef.current.value = ''
    }

    return (
        <div className={ props.className }>
            <div className="col-2 mb-3">
                <form onSubmit={ handleSubmit }>
                    <textarea required={ true } ref={ textAreaRef } className="tweet-form"></textarea>
                    <button type="submit">Tweet</button>
                </form>
            </div>
            <TweetList newTweets={ newTweets }/>
        </div>
    )
}