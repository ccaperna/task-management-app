from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from task_service.forms import TaskForm
from task_service.models import Task

#TODO update html script names with url names and function signatures

# implementation of task class-based view
class TaskManager(View):

    # get request handler function
    def get(self, request, *args, **kwargs):

        if "pk" in kwargs:
            # Handle the request with a pk
            pk = kwargs.get("pk")
            task = Task.objects.get(pk=pk)
            #filter operation based on action 
            action = request.GET.get("action") 
            # TODO refactor 
            if action == "update_done":
                # Update task status
                task.status = 2
                task.save()
                
            elif action == "update_in_progress":
                task.status = 1
                task.save()
                
            return redirect("home")


        else:
            # retrieve tasks data from db filtering upon status
            in_progress_tasks = Task.objects.filter(status=1).order_by("deadline")
            to_do_tasks = Task.objects.filter(status=0).order_by("deadline")
            done_tasks = Task.objects.filter(status=2).order_by("deadline")

            return render(
                request,
                "task_service/home.html",
                {
                    "in_progress": in_progress_tasks,
                    "to_do": to_do_tasks,
                    "done": done_tasks,
                },
            )


# create_task function handles new task creation
def task_create(request):
    if request.method == "POST":
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
    form = TaskForm(request.POST)
    return render(request, "task_service/task_new.html", {"form": form})

def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task_service/task_view.html", {"task": task})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save(commit=False)
            updated_task.save()
            return redirect("task_view", pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, "task_service/task_new.html", {"form": form})

def task_remove(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("home")