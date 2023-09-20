from django.http import HttpResponse
from django.shortcuts import render


def Login(request):
    return HttpResponse("Login")


def Signup(request):
    return HttpResponse("Signup")


def Logout(request):
    return HttpResponse("Logout")
