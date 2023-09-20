from django.urls import path
from .views import Login, Logout, Signup

urlpatterns = [
    path("signup/", Signup),
    path("login/", Login),
    path("logout/", Logout),
]
