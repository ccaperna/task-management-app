from django.urls import path
from task_service.views import TaskManager, task_create, task_remove, task_view, task_edit

urlpatterns = [
    path("home/", TaskManager.as_view(), name="home"),
    path("home/create", task_create, name="new_task"),
    path("home/<int:pk>", TaskManager.as_view(), name="task_action"),
    path("home/<int:pk>/view", task_view, name="task_view"),
    path("home/<int:pk>/remove", task_remove, name="task_remove" ),
    path("home/<int:pk>/edit", task_edit, name="task_edit")
]
