import random
from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=240, blank=True, null=True)
    image = models.FileField(upload_to="images/", blank=True, null=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content

    def serialize(self):
        return {
            'id': self.pk,
            'content': self.content,
            'likes': random.randint(0, 299)
        }
