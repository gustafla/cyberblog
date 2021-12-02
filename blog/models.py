from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(default="Post title", max_length=255)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
