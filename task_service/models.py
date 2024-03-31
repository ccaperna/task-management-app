from django.db import models


# definition of task model
class Task(models.Model):
    author = models.CharField(max_length=50)
    deadline = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
