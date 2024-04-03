from django.db import models
from django_enum import EnumField


# definition of task model
class Task(models.Model):
    class Status(models.IntegerChoices):
        CREATED = 0
        IN_PROGRESS = 1
        DONE = 2

    author = models.CharField(max_length=50)
    deadline = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    status = EnumField(Status, default=Status.CREATED)
    created = models.DateTimeField(auto_now_add=True)
