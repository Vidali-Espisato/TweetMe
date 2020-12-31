from rest_framework import serializers
from django.conf import settings
from .models import Tweet

TWEET_ACTION_OPTIONS = settings.TWEET_ACTION_OPTIONS

class TweetActionSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip()
        if value not in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for tweets.")
        return value


class TweetCreateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'content', 'likes']

    def get_likes(self, obj):
        return obj.likes.count()
    
    def validate_content(self, content):
        if len(content) > 240:
            raise serializers.ValidationError("Tweet's max length exceeded!")
        return content


class TweetSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    parent = TweetCreateSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'content', 'likes', 'is_retweet', 'parent']

    def get_likes(self, obj):
        return obj.likes.count()
    


# class TweetSerializer(serializers.ModelSerializer):
#     likes = serializers.SerializerMethodField(read_only=True)
#     content = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Tweet
#         fields = ['id', 'content', 'likes', 'is_retweet']

#     def get_likes(self, obj):
#         return obj.likes.count()
    
#     def get_content(self, obj):
#         content = obj.content
#         if obj.is_retweet:
#             content = obj.parent.content
#         return content   