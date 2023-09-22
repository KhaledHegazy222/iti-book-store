from django.shortcuts import redirect, render
from user.models import BUser
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import json


def is_logged_in(request):
    return "id" in request.session


def is_admin(request):
    if not is_logged_in(request):
        return False
    buser_id = request.session["id"]
    try:
        buser_obj = BUser.objects.get(id=buser_id)
        return buser_obj.role == "admin"
    except Exception as E:
        return False


def is_student(request):
    if not is_logged_in(request):
        return False
    buser_id = request.session["id"]
    try:
        buser_obj = BUser.objects.get(id=buser_id)
        return buser_obj.role == "student"
    except Exception as E:
        return False


def attach_user_context(request, context):

    if not is_logged_in(request):
        context.update({"logged_in": False})
    elif is_admin(request):
        context.update({"logged_in": True})
        context.update({"user_id": request.session['id']})
        context.update({"is_admin": True})
    else:
        context.update({"logged_in": True})
        context.update({"is_admin": False})
    return context


@csrf_exempt
def Login(request):
    if request.method == "GET":
        context = {}
        return render(request, "authentication/login.html", attach_user_context(request, context))
    else:

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user == None:
            return render(request, "authentication/login.html")
        request.session["id"] = user.buser.id
        return redirect("/home")


@csrf_exempt
def Signup(request):
    if request.method == "GET":
        context = {}
        return render(request, "authentication/signup.html", attach_user_context(request, context))
    else:

        username = request.POST["username"]
        password = request.POST["password"]
        is_admin = False
        new_user = User.objects.create_user(
            username=username, password=password)
        new_buser = BUser.objects.create(
            user=new_user, role="admin" if is_admin else "student")
        request.session["id"] = new_buser.id

        return redirect("/home")


@csrf_exempt
def Logout(request):
    if "id" in request.session:
        del request.session["id"]
    return redirect("/home")


@csrf_exempt
def ChangePassword(request):
    if not is_admin(request):
        return redirect("/api/auth/login")
    if request.method == "GET":
        context = {}
        return render(request, "authentication/change_password.html", attach_user_context(request, context))
    else:

        username = request.POST["username"]
        old_password = request.POST["old_password"]
        new_password = request.POST["new_password"]
        user = authenticate(username=username, password=old_password)
        if user is not None:
            user.set_password(new_password)
            user.save()
            return redirect("/home")
        else:
            return redirect("/api/auth/login")
