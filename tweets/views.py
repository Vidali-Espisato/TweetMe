from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
# Create your views here.


def home_view(request, *args, **kwargs):
    return HttpResponse("Hello World")


def tweet_detail_view(requst, tweet_id, *args, **kwargs):
    data = {
        'id': tweet_id,
    }
    status = 200
    try:
        tweet = Tweet.objects.get(id=tweet_id)
        data['content'] = tweet.content
    except:
        data['error'] = "Not Found!"
        status = 404
    return JsonResponse(data, status=status)
