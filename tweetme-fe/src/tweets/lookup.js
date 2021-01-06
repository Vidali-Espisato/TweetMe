import backendLookup from '../lookup'

const apiTweetCreate = (newTweet, callback) => {
    backendLookup('POST', "/tweets/create/", callback, {content: newTweet})
}

const apiTweetsList = callback => {
    backendLookup('GET', "/tweets/", callback)   
}

export { apiTweetCreate, apiTweetsList }