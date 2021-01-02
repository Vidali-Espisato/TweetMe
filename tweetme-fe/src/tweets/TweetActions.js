import React, { useState } from 'react'

export function TweetActions(props) {
    const { tweet, action } = props
    const [ likes, setLikes] = useState(tweet.likes ? tweet.likes : 0)
    const [ userLike, setUserLike ] = useState(tweet.likes ? true : false)
    const className = props.className ? props.className : "btn btn-primary m-3"
    const display = action.type === "like" ? `${ likes } Likes` : action.type

    const handleClick = event => {
        console.log(tweet.likes ? true : false)
        if (action.type === "like") {
            if (userLike) {
                setLikes(likes - 1)
                setUserLike(false)
            } else {
                setLikes(likes + 1)
                setUserLike(true)
            }
        }
    }

    return (
        <div>
            <button className={ className } onClick={ handleClick }>{ display }</button> 
        </div>
    )
}

