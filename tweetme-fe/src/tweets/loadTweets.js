const lookup = (method, endpoint, callback, data) => {
    const jsonData = data ? JSON.stringify(data) : null
    const xhr = new XMLHttpRequest();
    const url = `http://127.0.0.1:8000/api/v1${endpoint}`;
    xhr.responseType = "json";
    xhr.open(method, url);
    xhr.onload = () => {
        callback(xhr.response, xhr.status);
    };
    xhr.onerror = err => {
        console.log(err);
        callback({ message: "Somehting is wrong!" }, 400);
    };
    xhr.send(jsonData);
}

const loadTweets = callback => {
    lookup("GET", "/tweets/", callback)   
}

export default loadTweets