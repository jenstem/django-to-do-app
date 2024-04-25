from django.shortcuts import render
from .models import Task
from django.shortcuts import redirect


def index(request):
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
    task = Task.objects.get(id=taskid)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'myapp/delete.html', {'task': task})
