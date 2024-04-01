from django.db import models
from django_enum import EnumField


# definition of task model
class Task(models.Model):
    class Status(models.IntegerChoices):
        NOT_STARTED = 0
        IN_PROGRESS = 1
        DONE = 2

    author = models.CharField(max_length=50)
    deadline = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    status = EnumField(Status)
