from django.urls import path
from .views import ListBooks, ListBorrowedBooks, GetBookDetails, GetUserBooks, BorrowBook, ReturnBook, AddBook, EditBook, DeleteBook

app_name = "book"

urlpatterns = [
    path("", ListBooks, name="list_books"),
    path("borrowed/", ListBorrowedBooks, name="list_borrowed_books"),
    path('<int:pk>/', GetBookDetails, name="details"),
    path("me/", GetUserBooks, name="my_books"),
    path("borrow/<int:pk>/", BorrowBook, name="borrow"),
    path("return/<int:pk>/", ReturnBook, name="return"),
    path("add/", AddBook, name="add"),
    path("edit/<int:pk>/", EditBook, name="edit"),
    path("delete/<int:pk>/", DeleteBook, name="delete"),
]
