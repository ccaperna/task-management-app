from django.urls import path
from task_service.views import TaskManager

urlpatterns = [
    path("home/", TaskManager.as_view(), name="task_manager"),
]
