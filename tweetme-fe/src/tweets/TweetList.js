import React, { useState, useEffect } from 'react'
import { Tweet } from "./Tweet"
import loadTweets from "./loadTweets"

export function TweetList(props) {
    const [tweetsInit, setTweetsInit] = useState([])
    const [tweets, setTweets] = useState([])
    const newTweets = props.newTweets

    useEffect(() => {
      const finalTweets = [...newTweets].concat(tweetsInit)
      if (finalTweets.length !== tweetsInit.length) {
        setTweets(finalTweets)
      }
    }, [newTweets, tweetsInit, tweets])

    useEffect(() => {
        const myCallback = (response, status) => {
          if (status === 200) {
            setTweetsInit(response)
          } else {
            alert(response.message)
          }
        }
        loadTweets(myCallback)
      }, [tweetsInit])
    
    return (
        <div>
            {
              tweets.map((tweet, index) => <Tweet key={index} tweet={tweet} className="my-10 mx-auto bg-light text-success shadow-lg text-center" />)
            }
        </div>
    )
}