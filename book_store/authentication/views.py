from user.models import BUser
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import json


@csrf_exempt
def Login(request):
    request_body = json.loads(request.body)
    username = request_body["username"]
    password = request_body["password"]
    user = authenticate(username=username, password=password)
    if user == None:
        return HttpResponse(status=404)
    return HttpResponse(f"{user.buser} {user.buser.role}")


@csrf_exempt
def Signup(request):

    request_body = json.loads(request.body)
    username = request_body["username"]
    password = request_body["password"]
    is_admin = request_body["is_admin"]
    new_user = User.objects.create_user(username=username, password=password)
    new_buser = BUser.objects.create(
        user=new_user, role="admin" if is_admin else "student")
    return HttpResponse(f"{new_buser} {new_buser.role}")


@csrf_exempt
def Logout(request):
    return HttpResponse("Logout")
