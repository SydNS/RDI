from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
