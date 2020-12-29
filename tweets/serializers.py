from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content']

        def validate_content(self, content):
            if len(content) > 240:
                raise serializers.ValidationError("Tweet's max length exceeded!")
            return content