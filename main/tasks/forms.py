from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'solution', 'answer']

class ModerateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['is_approved', 'topic', 'difficulty']