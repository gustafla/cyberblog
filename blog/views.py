from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    latest_posts = Post.objects.order_by("-date")[:100]
    return render(request, "blog/index.html", context={"latest_posts": latest_posts})


def view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/view.html", {"post": post})
