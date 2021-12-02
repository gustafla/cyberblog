from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post


def index(request):
    latest_posts = Post.objects.order_by("-date")[:100]
    return render(request, "blog/index.html", context={"latest_posts": latest_posts})


def view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/view.html", {"post": post})


@login_required
def post(request):
    if request.method == "POST":
        return redirect("/blog/")

    return render(request, "blog/post.html")
