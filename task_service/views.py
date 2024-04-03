from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from task_service.forms import TaskForm
from task_service.models import Task
from task_service.utils import update_task, get_filtered_tasks


# implementation of task class-based view
class TaskManager(View):

    # get request handler function
    def get(self, request, *args, **kwargs):

        if "pk" in kwargs:
            # Handle the request with a pk
            pk = kwargs.get("pk")
            task = Task.objects.get(pk=pk)
            # filter operation based on action
            action = request.GET.get("action")
            update_task(task, action)

            return redirect("home")

        else:
            # retrieve tasks data from db filtering upon status
            task_dict = get_filtered_tasks()
            return render(
                request,
                "task_service/index.html",
                {
                    "in_progress": task_dict["in_progress"],
                    "to_do": task_dict["to_do"],
                    "done": task_dict["done"],
                },
            )


# TaskCreator view handles new task creation
class TaskCreator(View):

    def get(self, request):
        form = TaskForm(request.POST)
        return render(request, "task_service/task_new.html", {"form": form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
            return redirect("home")
        else:
            form = TaskForm()
            return render(
                request,
                "task_service/new_task.html",
                {"form": form},
            )


# TaskEditor view handles task editing
class TaskEditor(View):

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, "task_service/task_new.html", {"form": form})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save(commit=False)
            updated_task.save()
            return redirect("task_view", pk=task.pk)
        else:
            return render(request, "task_service/task_new.html", {"form": form})


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task_service/task_view.html", {"task": task})


def task_remove(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("home")


def home_view(request, pk):
    return redirect("home")
