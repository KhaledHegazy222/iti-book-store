from django.urls import path
from .views import ListUsersView, GetUserView, ListBooksView, ListBorrowedBookView

urlpatterns = [
    path("users/", ListUsersView),
    path("users/<int:pk>/", GetUserView),
    path("books/", ListBooksView),
    path("books/borrowed/", ListBorrowedBookView),
]
