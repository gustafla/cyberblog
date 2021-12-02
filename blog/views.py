from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def index(request):
    latest_posts = Post.objects.order_by("-date")[:10]
    return render(request, "blog/index.html", context={"latest_posts": latest_posts})


def view(request, post_id):
    return HttpResponse(f"You're looking at post {post_id}")
