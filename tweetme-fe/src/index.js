import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import TweetsComponent from './tweets';


const root = document.getElementById('tweetme-root') || document.getElementById('root')

ReactDOM.render(
  <React.StrictMode>
    {
      root.id === 'tweetme-root' ? (
        <TweetsComponent />
      ) : (
        <App />
      )
    }
  </React.StrictMode>,
  root
) 

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
