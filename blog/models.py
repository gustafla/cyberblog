from django.db import models


class Post(models.Model):
    text = models.TextField()
    date = models.DateTimeField()
