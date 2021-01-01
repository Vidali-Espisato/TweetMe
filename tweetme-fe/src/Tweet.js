import React from 'react';

function Tweet(props) {
    const {tweet} = props;
    const className = props.className ? props.className : "my-10 mx-auto bg-light text-dark";
    return (
        <div className={className}>
            <p>{tweet.id}: {tweet.content}</p>
        </div>
    )
}

export default Tweet;
