from django.db import models

from rdi.user.models import User


# Create your models here.
class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
