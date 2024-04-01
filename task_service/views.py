from django.shortcuts import redirect, render
from django.views import View
from task_service.forms import TaskForm
from task_service.models import Task


# implementation of task class-based view
class TaskManager(View):

    # get request handler function
    def get(self, request):

        # retrieve tasks data from db filtering upon status
        in_progress_tasks = Task.objects.filter(status=1).order_by("deadline")
        to_do_tasks = Task.objects.filter(status=0).order_by("deadline")
        done_tasks = Task.objects.filter(status=1).order_by("deadline")

        return render(
            request,
            "task_service/task.html",
            {
                "in_progress": in_progress_tasks,
                "to_do": to_do_tasks,
                "done": done_tasks,
            },
        )

    # post request handler function
    def post(self, request):
        pass


# create_task function handles new task creation
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = TaskForm()
            return render(
                request,
                "task_service/new_task.html",
                {"form": form},
            )
    form = TaskForm(request.POST)
    return render(request, "task_service/new_task.html", {"form": form})


def update_in_progress(request):
    pass


def update_done(request):
    pass


def delete_task(request):
    pass
