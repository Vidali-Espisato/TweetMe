import React, { useState, useEffect } from 'react'
import { Tweet } from "./Tweet"
import loadTweets from "./loadTweets"

export function TweetList(props) {
    const [tweets, setTweets] = useState([])
    
    useEffect(() => {
        const myCallback = (response, status) => {
          if (status === 200) {
            setTweets(response)
          } else {
            alert(response.message)
          }
        }
        loadTweets(myCallback)
      }, [])
    
    return (
        <div>
            {
                tweets.map((tweet, index) => <Tweet key={index} tweet={tweet} className="my-10 mx-auto bg-light text-success shadow-lg text-center" />)
            }
        </div>
    )
}