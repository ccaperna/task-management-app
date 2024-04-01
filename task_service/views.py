from django.shortcuts import redirect, render
from django.views import View
from task_service.forms import TaskForm


# implementation of task class-based view
class TaskManager(View):

    # get request handler function
    def get(self, request):
        return render(request, "task_service/task.html")

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
