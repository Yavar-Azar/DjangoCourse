from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        return render(request, 'todoapp/add_task.html')


