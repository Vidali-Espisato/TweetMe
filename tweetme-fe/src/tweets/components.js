import React, { useState } from 'react'
import { TweetList } from "./TweetList"

export function TweetsComponent(props) {
    const textAreaRef = React.createRef()
    const [newTweets, setNewTweets] = useState([])

    const handleSubmit = event => {
        event.preventDefault()
        const newVal = textAreaRef.current.value
        let tempTweet = [...newTweets]
        tempTweet.unshift({
            content: newVal,
            id: 123,
            likes: 455
        })
        setNewTweets(tempTweet)
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