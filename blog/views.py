from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt
import datetime

from .models import Post


@xframe_options_exempt
def index(request):
    latest_posts = Post.objects.order_by("-date")[:100]
    return render(request, "blog/index.html", context={"latest_posts": latest_posts})


@xframe_options_exempt
def view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/view.html", {"post": post})


def text2paras(text):
    output_paras = []
    output = ""

    for line in text.splitlines():
        if line.strip():
            if output:
                output += "<br />"
            output += line
        else:
            if output:
                output_paras.append(output)
                output = ""

    output_paras.append(output)
    return "".join("<p>" + para + "</p>" for para in output_paras)


@login_required
@csrf_exempt
@xframe_options_exempt
def create_post(request):
    post = Post()
    post.author = request.user
    post.title = request.GET.get("title", "No title")
    post.text = text2paras(request.GET.get("text", ""))
    post.date = datetime.datetime.now()
    post.save()
    return redirect("/blog/")


@login_required
@csrf_exempt
@xframe_options_exempt
def post(request):
    return render(request, "blog/post.html")
