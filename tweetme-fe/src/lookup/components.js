import getCookie from "./cookie"

const backendLookup = (method, endpoint, callback, data) => {
    const jsonData = data ? JSON.stringify(data) : null
    const xhr = new XMLHttpRequest()
    const url = `http://127.0.0.1:8000/api/v1${endpoint}`
    xhr.responseType = "json"
    xhr.open(method, url)

    const csrftoken = getCookie('csrftoken')
    xhr.setRequestHeader('Content-Type', "application/json")
    if (csrftoken) {
        xhr.setRequestHeader('HTTP_X_REQUESTED_WITH', "XMLHttpRequest")
        xhr.setRequestHeader('X-Requested-With', "XMLHttpRequest")
        xhr.setRequestHeader('X-CSRFToken', csrftoken)
    }
    xhr.onload = () => {
        callback(xhr.response, xhr.status)
    }
    xhr.onerror = err => {
        console.log(err)
        callback({ message: "Somehting is wrong!" }, 400)
    }
    xhr.send(jsonData)
}


export default backendLookup