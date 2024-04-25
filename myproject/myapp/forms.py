from .models import Task
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task name...'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }