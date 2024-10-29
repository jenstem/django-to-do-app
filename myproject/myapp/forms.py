from .models import Task
from django import forms

class TodoForm(forms.ModelForm):
    """
    A form for creating and updating Task instances.

    Meta class defines the model and fields to be included in the form.
    """
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task name...'}),
            'priority': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select priority...'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
