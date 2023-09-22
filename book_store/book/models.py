from django.db import models
from user.models import BUser


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    state = models.CharField(max_length=10, choices=[(
        "Available", "Available"), ("Taken", "Taken")], default="Available")
    return_date = models.DateField()
    price = models.FloatField()
    borrowing_user = models.ForeignKey(
        BUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
