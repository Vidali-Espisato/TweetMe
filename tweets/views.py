import random
from django.conf import settings
from django.utils.http import is_safe_url
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .forms import TweetForm
from .models import Tweet
# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html')


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url, allowed_hosts=ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'components/form.html', context={'form': form})


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{'id': x.id, 'content': x.content,
                    'likes': random.randint(0, 99)} for x in qs]
    data = {'isUser': False, 'response': tweets_list}
    return JsonResponse(data, status=200)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
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
