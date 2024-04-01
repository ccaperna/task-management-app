from django.urls import path
from task_service.views import TaskManager, create_task

urlpatterns = [
    path("home/", TaskManager.as_view(), name="home"),
    path("home/create", create_task, name="new_task"),
]
