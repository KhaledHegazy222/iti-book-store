from django.urls import path
from .views import ListUsers, GetUser

app_name = "user"

urlpatterns = [
    path("", ListUsers, name="list_users"),
    path("<int:pk>/", GetUser, name="get_user"),
]
