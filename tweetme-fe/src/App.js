import { useState, useEffect } from 'react';
import './App.css';
import Tweet from './Tweet';


const loadTweets = (callback) => {
  const xhr = new XMLHttpRequest();
  const method = "GET";
  const url = "http://127.0.0.1:8000/api/v1/tweets/";
  const responseType = "json";
  xhr.responseType = responseType;
  xhr.open(method, url);
  xhr.onload = () => {
    callback(xhr.response, xhr.status);
  };
  xhr.onerror = err => {
    console.log(err);
    callback({message: "An error occurred!"}, 400);
  }
  xhr.send();
};


function App() {
  const [tweets, setTweets] = useState([]);
  
  useEffect(() => {
    const myCallback = (response, status) => {
      if (status === 200) {
        setTweets(response);
      } else {
        alert("An error occurred!");
      }
    }
    loadTweets(myCallback);
  }, [])

  return (
    <div className="App">
      <header className="App-header">          
      </header>
      {
        tweets.map((tweet, index) => <Tweet key={index} tweet={tweet} className="my-10 mx-auto bg-light text-success shadow-lg text-center" />)
      }
    </div>
  );
}

export default App;
