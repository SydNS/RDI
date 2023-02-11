from django.db import models

from rdi.student.models import Student
from rdi.teacher.models import Teacher


# Create your models here.

class SchClass(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
