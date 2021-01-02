
const loadTweets = callback => {
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
        callback({ message: "Somehting is wrong!" }, 400);
    };
    xhr.send();
}

export default loadTweets