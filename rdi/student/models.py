from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from rdi.user.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
