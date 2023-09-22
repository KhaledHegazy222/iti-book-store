from django.urls import path
from .views import Login, Logout, Signup

app_name = "authentication"

urlpatterns = [
    path("signup/", Signup, name="signup"),
    path("login/", Login, name="login"),
    path("logout/", Logout, name="logout"),
]
