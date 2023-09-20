from django.shortcuts import render
from django.http import HttpResponse
from .models import BUser


def ListUsersView(request):
    users = BUser.objects.all()
    return HttpResponse(users)


def GetUserView(request, pk=1):
    return HttpResponse(f"Hello user {pk}")


def ListBooksView(request):
    return HttpResponse("Hello books")


def ListBorrowedBookView(request):
    return HttpResponse("Hello borrowed books")
