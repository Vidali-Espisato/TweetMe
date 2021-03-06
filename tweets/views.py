import random
from django.conf import settings
from django.utils.http import is_safe_url
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .forms import TweetForm
from .serializers import TweetSerializer, TweetActionSerializer, TweetCreateSerializer
from .models import Tweet
# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html')

@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    serializer = TweetSerializer(qs.first())
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_action_view(request, *args, **kwargs):
    serializer = TweetActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get('pk')
        action = data.get('action')
        content = data.get('content')
            
        qs = Tweet.objects.filter(id=tweet_id)
        if not qs.exists():
            return Response({}, status=404)

        obj = qs.first()
        if action == "like":
            obj.likes.add(request.user)
            serializer = TweetSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "unlike":
            obj.likes.remove(request.user)
            serializer = TweetSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "retweet":
            retweet = Tweet.objects.create(parent=obj, user=request.user, content=content)
            serializer = TweetSerializer(retweet)
            return Response(serializer.data, status=201)
        elif action == "delete":
            qs = qs.filter(user=request.user)
            if not qs.exists():
                return Response({'message': "You are not authorized to delete this tweet"}, status=401)
            obj = qs.first()
            obj.delete()
            return Response({'message': f"Tweet {tweet_id} deleted succesfully."})
    return Response({}, status=201)


# @api_view(['GET', 'DELETE', 'POST'])
# def tweet_delete_view(request, tweet_id, *args, **kwargs):
#     qs = Tweet.objects.filter(id=tweet_id)
#     if not qs.exists():
#         return Response({}, status=404)
#     qs = qs.filter(user=request.user)
#     if not qs.exists():
#         return Response({'message': "You are not authorized to delete this tweet"}, status=401)
#     obj = qs.first()
#     obj.delete()
#     return Response({'message': f"Tweet {tweet_id} deleted succesfully."})


# def tweet_create_view(request, *args, **kwargs):
#     serializer = TweetSerializer(data=request.POST or None)
#     if serializer.is_valid():
#         serializer.save(user=request.user)
#         return JsonResponse(serializer.data, status=201)
#     return JsonResponse({}, status=400)


# def tweet_create_view(request, *args, **kwargs):
#     user = request.user
#     if not user.is_authenticated:
#         user = None
#         if request.is_ajax():
#             return JsonResponse({}, status=403)
#         return redirect(settings.LOGIN_URL)
#     form = TweetForm(request.POST or None)
#     next_url = request.POST.get("next") or None
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.save()
#         if request.is_ajax():
#             return JsonResponse(obj.serialize(), status=201)
#         if next_url != None and is_safe_url(next_url, allowed_hosts=ALLOWED_HOSTS):
#             return redirect(next_url)
#         form = TweetForm()
#     if form.errors and request.is_ajax():
#         return JsonResponse(form.errors, status=400)
#     return render(request, 'components/form.html', context={'form': form})


# def tweet_list_view(request, *args, **kwargs):
#     qs = Tweet.objects.all()
#     # tweets_list = [{'id': x.id, 'content': x.content,
#     #                 'likes': random.randint(0, 99)} for x in qs]
#     tweets_list = [x.serialize() for x in qs]
#     data = {'isUser': False, 'response': tweets_list}
#     return JsonResponse(data, status=200)


# def tweet_detail_view(request, tweet_id, *args, **kwargs):
#     data = {
#         'id': tweet_id,
#     }
#     status = 200
#     try:
#         tweet = Tweet.objects.get(id=tweet_id)
#         data['content'] = tweet.content
#     except:
#         data['error'] = "Not Found!"
#         status = 404
#     return JsonResponse(data, status=status)
