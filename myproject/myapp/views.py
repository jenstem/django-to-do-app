from django.shortcuts import render
from .models import Task
from django.shortcuts import redirect


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')

        task = Task(name=name, priority=priority)
        task.save()
        return redirect('/')

    return render(request, 'myapp/add.html')


def index(request):
    task_list = Task.objects.all()
    return render(request, 'myapp/index.html', {'task_list': task_list})
