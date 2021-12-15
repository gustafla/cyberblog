from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)


@csrf_exempt
@xframe_options_exempt
def register(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password").lower()
        password2 = request.POST.get("password2").lower()
        if password2 == password:
            if len(password) <= 8 and password.isalnum():
                if (
                    len(username) <= 20
                    and username.isalnum()
                    and not User.objects.filter(username=username).exists()
                ):
                    user = User.objects.create_user(username, None, password)
                    django_login(request, user)
                    return redirect("/")
                else:
                    context["invalid_username"] = True
            else:
                context["invalid_password"] = True
        else:
            context["no_match"] = True

    return render(request, "accounts/register.html", context)


@csrf_exempt
@xframe_options_exempt
def login(request):
    context = {"next": request.GET.get("next", "/")}
    if request.method == "POST":
        context["next"] = request.POST.get("next", context.get("next", "/"))
        username = request.POST.get("username")
        password = request.POST.get("password").lower()
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
