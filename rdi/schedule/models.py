from django.db import models

from rdi.schclass.models import SchClass


# Create your models here.
class Schedule(models.Model):
    class_id = models.ForeignKey(SchClass, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    time = models.TimeField()

    def __str__(self):
        return self.class_id.name + " - " + self.day + " " + str(self.time)
