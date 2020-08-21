from django.db import models

# Create your models here.


class Tweet(models.Model):
    content = models.CharField(max_length=500, blank=True, null=True)
    image = models.FileField(upload_to="images/", blank=True, null=True)
