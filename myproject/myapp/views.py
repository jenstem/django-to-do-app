from django.shortcuts import render, redirect
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


class TaskListView(ListView):
    """
    A view that displays a list of tasks.

    Attributes:
        model: The model to be used for the view, which is Task.
        template_name: The template to render the view, located at 'myapp/index.html'.
        context_object_name: The name of the context variable to be used in the template, set to 'task_list'.
    """
    model = Task
    template_name = 'myapp/index.html'
    context_object_name = 'task_list'


class TaskDetailView(DetailView):
    """
    A view that displays the details of a specific task.

    Attributes:
        model: The model to be used for the view, which is Task.
        template_name: The template to render the view, located at 'myapp/detail.html'.
        context_object_name: The name of the context variable to be used in the template, set to 'task'.
    """
    model = Task
    template_name = 'myapp/detail.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    """
    A view that allows for the updating of a specific task.

    Attributes:
        model: The model to be used for the view, which is Task.
        template_name: The template to render the view, located at 'myapp/update.html'.
        context_object_name: The name of the context variable to be used in the template, set to 'task'.
        fields:  The fields to be included in the form for updating the task.
        success_url: The URL to redirect to upon successful update.
    """
    model = Task
    template_name = 'myapp/update.html'
    context_object_name = 'task'
    fields = ['name', 'priority', 'date']
    success_url = '/'

    def get_success_url(self):
        """
        Returns the URL to redirect to after a successful update.

        Returns:
            str: The URL to redirect to, including the primary key of the updated task.
        """
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    """
    A view that allows for the deletion of a specific task.

    Attributes:
        model: The model to be used for the view, which is Task.
        template_name: The template to render the view, located at 'myapp/delete.html'.
        context_object_name: The name of the context variable to be used in the template, set to 'task'.
        success_url: The URL to redirect to upon successful deletion.
    """
    model = Task
    template_name = 'myapp/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('cbvindex')


def index(request):
    """
    Handles the display and creation of tasks.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered template with the task list or a redirect upon task creation.
    """
    task_list = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect('/')
    return render(request, 'myapp/index.html', {'task_list': task_list})


def delete(request, taskid):
    """
    Handles the deletion of a specific task.

    Args:
        request:  The HTTP request object.
        taskid: The ID of the task to be deleted.

    Returns:
        HttpResponse:  The rendered template for deletion confirmation or a redirect upon deletion.
    """
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html', {'task': task})


def update(request, id):
    """
    Handles the updating of a specific task.

    Args:
        request: The HTTP request object.
        id: The ID of the task to be updated.

    Returns:
        HttpResponse: The rendered template for the update form or a redirect upon successful update.
    """
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'myapp/update.html', {'form': form, 'task': task})
