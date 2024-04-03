from task_service.models import Task


def update_task(task, action):
    if action == "update_done":
        # Update task status
        task.status = 2
        task.save()

    elif action == "update_in_progress":
        task.status = 1
        task.save()

# build and return a dictionary where the key is the status and the value in the set of tasks
def get_filtered_tasks():
    dic = dict()
    dic["to_do"] = Task.objects.filter(status=0).order_by("deadline")
    dic["in_progress"] = Task.objects.filter(status=1).order_by("deadline")
    dic["done"] = Task.objects.filter(status=2).order_by("deadline")

    return dic
