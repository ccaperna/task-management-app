from django.urls import path
from task_service.views import (
    TaskManager,
    TaskCreator,
    task_remove,
    task_view,
    TaskEditor,
    home_view,
)

urlpatterns = [
    path("", TaskManager.as_view(), name="home"),
    path("create", TaskCreator.as_view(), name="new_task"),
    path("<int:pk>", TaskManager.as_view(), name="task_action"),
    path("<int:pk>/view", task_view, name="task_view"),
    path("<int:pk>/remove", task_remove, name="task_remove"),
    path("<int:pk>/edit", TaskEditor.as_view(), name="task_edit"),
    path("<int:pk>/home", home_view, name="home_view"),
]
