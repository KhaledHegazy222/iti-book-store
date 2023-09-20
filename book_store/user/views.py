from django.shortcuts import render
from django.http import HttpResponse


def ListUsersView(request):
    return HttpResponse("Hello users")


def GetUserView(request, pk=1):
    return HttpResponse(f"Hello user {pk}")


def ListBooksView(request):
    return HttpResponse("Hello books")


def ListBorrowedBookView(request):
    return HttpResponse("Hello borrowed books")
