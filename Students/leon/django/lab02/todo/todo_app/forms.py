from django import forms
from .models import TodoItem

class TaskForm(forms.ModelForm):
    task = forms.CharField(label='enter task', max_length=200)
    class Meta:
        model = TodoItem
        fields = ('task', 'start', 'end', 'done')