import React from 'react';
import { TweetActions } from "./TweetActions"

export function Tweet(props) {
    const { tweet } = props;
    const className = props.className ? props.className : "my-10 mx-auto bg-light text-dark";
    return (
        <div className={className}>
            <p>{tweet.id}: {tweet.content}</p>
            {
                ["like", "unlike", "retweet", "delete"]
                    .map((t, i) => <TweetActions key={i} tweet={ tweet } action={{ type: t }}/>)
            }
        </div>
    )
}

