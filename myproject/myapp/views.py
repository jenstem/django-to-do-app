from django.shortcuts import render


def add(request):
    return render(request, 'myapp/add.html')
