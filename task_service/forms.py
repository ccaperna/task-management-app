from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    author = forms.CharField(max_length=50, required=True)
    deadline = forms.DateTimeField(required=True)
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=500, required=True)

    class Meta:
        model = Task
        fields = "__all__"
