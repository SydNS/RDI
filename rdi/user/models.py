from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from rdi.roles.models import Role


class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username
