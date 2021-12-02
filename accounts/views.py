from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            django_login(request, user)
            return redirect(request.POST.get("next", "/"))
        else:
            return render(request, "accounts/login.html", {"invalid": True})

    return render(
        request, "accounts/login.html", {"next": request.GET.get("next", "/")}
    )


def logout(request):
    django_logout(request)
    return redirect("/")
