
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from authentication.views import attach_user_context, is_admin, is_logged_in, is_student

from user.models import BUser
from .models import Book
from .forms import BookForm


def ListBooks(request):

    if not is_logged_in(request):
        return redirect("/api/auth/login")
    books_set = Book.objects.all()
    context = {
        "books": books_set
    }
    return render(request, "book/list.html", attach_user_context(request, context))


def ListBorrowedBooks(request):

    if not is_logged_in(request):
        return redirect("/api/auth/login")

    if not is_admin(request):
        return redirect("/api/auth/login")

    books_set = Book.objects.filter(state="Taken")
    context = {
        "books": books_set
    }
    return render(request, "book/list.html", attach_user_context(request, context))


def GetBookDetails(request, pk=1):

    if not is_logged_in(request):
        return redirect("/api/auth/login")

    book_data = Book.objects.get(pk=pk)
    context = {
        "id": book_data.id,
        "title": book_data.title,
        "author": book_data.author,
        "state": book_data.state,
        "return_date": book_data.return_date,
        "price": book_data.price,
        "borrowing_user": book_data.borrowing_user,
    }
    return render(request, "book/details.html", attach_user_context(request, context))


def GetUserBooks(request):
    if not is_logged_in(request):
        return redirect("/api/auth/login")

    if not is_student(request):
        return redirect("/api/auth/login")

    user_id = request.session["id"]
    user = BUser.objects.get(id=user_id)
    context = {
        "books": user.book_set.all(),
        "can_return": True
    }
    return render(request, "book/list.html", attach_user_context(request, context))


@csrf_exempt
def BorrowBook(request, pk):
    if not is_logged_in(request):
        return redirect("/api/auth/login")

    if not is_student(request):
        return redirect("/api/auth/login")

    user_id = request.session["id"]

    selected_book = Book.objects.get(pk=pk)
    selected_book.state = "Taken"
    selected_book.save()
    selected_user = BUser.objects.get(id=user_id)
    selected_user.book_set.add(selected_book)
    selected_user.save()

    return redirect("/api/book/")


@csrf_exempt
def ReturnBook(request, pk):
    if not is_logged_in(request):
        return redirect("/api/auth/login")

    if not is_student(request):
        return redirect("/api/auth/login")

    user_id = request.session["id"]
    selected_book = Book.objects.get(pk=pk)
    selected_book.state = "Available"
    selected_book.save()
    selected_user = BUser.objects.get(id=user_id)
    selected_user.book_set.remove(selected_book)
    selected_user.save()
    selected_book = Book.objects.get(pk=pk)

    return redirect("/api/book/")


def AddBook(request):

    if not is_logged_in(request):
        return redirect("/api/auth/login")

    if not is_admin(request):
        return redirect("/api/auth/login")

    if request.method == "GET":
        bookForm = BookForm()
        context = {
            "form": bookForm,
            "button_text": "Add Book"
        }
        return render(request, "book/add.html", attach_user_context(request, context))
    elif request.method == "POST":
        bookForm = BookForm(request.POST)
        if (bookForm.is_valid()):
            bookForm.save()
            return redirect("/api/book/")
        else:
            context = {
                "form": bookForm,
                "button_text": "Add Book"
            }
            return render(request, "book/add.html", attach_user_context(request, context))


def EditBook(request, pk):
    if not is_logged_in(request):
        return redirect("/api/auth/login")

    if not is_admin(request):
        return redirect("/api/auth/login")

    book_obj = Book.objects.get(pk=pk)
    if request.method == "GET":
        bookForm = BookForm(instance=book_obj)
        context = {
            "form": bookForm,
            "button_text": "Edit Book"
        }
        return render(request, "book/add.html", attach_user_context(request, context))
    elif request.method == "POST":
        bookForm = BookForm(request.POST, instance=book_obj)
        if (bookForm.is_valid()):
            bookForm.save()
            return redirect("/api/book/")
        else:
            context = {
                "form": bookForm,
                "button_text": "Edit Book"
            }
            return render(request, "book/add.html", attach_user_context(request, context))


def DeleteBook(request, pk):
    if not is_logged_in(request):
        return redirect("/api/auth/login")

    if not is_admin(request):
        return redirect("/api/auth/login")

    Book.objects.get(pk=pk).delete()
    return redirect("/api/book")
