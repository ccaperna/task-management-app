from django.shortcuts import render
from django.views import View


# implementation of task class-based view
class TaskManager(View):

    # get request handler function
    def get(self, request):
        return render(request, "base.html")  # "task_service/task.html")
        pass

    # post request handler function
    def post(self, request):
        pass
