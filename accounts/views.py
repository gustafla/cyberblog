from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)


@csrf_exempt
@xframe_options_exempt
def login(request):
    context = {"next": request.GET.get("next", "/")}
    if request.method == "POST":
        context["next"] = request.POST.get("next", context.get("next", "/"))
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            django_login(request, user)
            return redirect(context["next"])
        else:
            context["invalid"] = True

    return render(request, "accounts/login.html", context)


def logout(request):
    django_logout(request)
    return redirect("/")
