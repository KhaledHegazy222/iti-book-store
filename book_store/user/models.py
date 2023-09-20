from django.db import models
from django.contrib.auth.models import User


class BUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[
                            ("admin", "admin"), ("student", "student")])
