from django.db import models


class Post(models.Model):
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.text
