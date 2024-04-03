from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    author = forms.CharField(max_length=50, required=True)
    deadline = forms.DateTimeField(
        required=True, widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"})
    )
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 60}))

    class Meta:
        model = Task
        fields = ["author", "deadline", "title", "description"]
