# Simple To-Do List 

## Getting Started

0. install django (Virtualenv highly recommended)

   ```bash
   pip install django
   ```

1. Start your first django project 

   ```bash
   mkdir 
   cd first_project
   ```

2. Navigate to the project folder:

   ```bash
   django-admin startproject simpletodo .
   ```

3. Create a Django app for your To-Do List:

   ```bash
   python manage.py startapp todoapp
   ```

4. Add your new app in `simpletodo/setting.py`
   ```python
       "django.contrib.admin",
       "django.contrib.auth",
       "django.contrib.contenttypes",
       "django.contrib.sessions",
       "django.contrib.messages",
       "django.contrib.staticfiles",
       "todoapp"
   ```

5. Do migration and check your database
   ```shell
   python manage.py makemigrations  
   python manage.py migrate
   ```

   

6. Define the models in the `models.py` file within the `todoapp` app:

   ```python
   # todoapp/models.py
   from django.db import models
   
   class Task(models.Model):
       title = models.CharField(max_length=200)
       description = models.TextField()
   
       def __str__(self):
           return self.title
   ```

7. Create database tables for your models

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. Check database with `DB browser or pycharm plugin`

9. Define the views in the `views.py` file within the `todoapp` app:

   ```python
   # todoapp/views.py
   from django.shortcuts import render, redirect
   from .models import Task
   
   def task_list(request):
       tasks = Task.objects.all()
       return render(request, 'todoapp/task_list.html', {'tasks': tasks})
   
   def add_task(request):
       if request.method == 'POST':
           title = request.POST['title']
           description = request.POST['description']
           task = Task(title=title, description=description)
           task.save()
           return redirect('task_list')
       return render(request, 'todoapp/add_task.html')
   
   ```

10. Create HTML templates for your views. Place them in a folder named `templates/todoapp`:

   `task_list.html`:

   ```html
   <!-- templates/todoapp/task_list.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <title>Task List</title>
       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
   </head>
   <body>
       <div class="container">
           <h1 class="mt-4">Task List</h1>
           <table class="table table-striped mt-4">
               <thead>
                   <tr>
                       <th scope="col">Title</th>
                       <th scope="col">Description</th>
                   </tr>
               </thead>
               <tbody>
                   {% for task in tasks %}
                       <tr>
                           <td>{{ task.title }}</td>
                           <td>{{ task.description }}</td>
                       </tr>
                   {% empty %}
                       <tr>
                           <td colspan="2">No tasks available.</td>
                       </tr>
                   {% endfor %}
               </tbody>
           </table>
           <a href="{% url 'add_task' %}" class="btn btn-primary">Add Task</a>
       </div>
   </body>
   </html>
   
   ```

   `add_task.html`:

   ```html
   <!-- templates/todoapp/add_task.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <title>Add Task</title>
       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
   </head>
   <body>
       <div class="container">
           <h1 class="mt-4">Add Task</h1>
           <form method="post" class="mt-4">
               {% csrf_token %}
               <div class="form-group">
                   <label for="title">Title:</label>
                   <input type="text" id="title" name="title" class="form-control" required>
               </div>
               <div class="form-group">
                   <label for="description">Description:</label>
                   <textarea id="description" name="description" class="form-control" required></textarea>
               </div>
               <button type="submit" class="btn btn-success">Add Task</button>
           </form>
           <a href="{% url 'task_list' %}" class="btn btn-secondary mt-3">Back to Task List</a>
       </div>
   </body>
   </html>
   
   
   ```

11. Define the URLs for your views in the `urls.py` file within the `todoapp` app:

    ```python
    # todoapp/urls.py
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', views.task_list, name='task_list'),
        path('add_task/', views.add_task, name='add_task'),
    ]
    ```

12. Include the URLs of your app in the project's `urls.py` file (`simpletodo/urls.py`):

    ```python
    # simpletodo/urls.py
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('todoapp.urls')),
    ]
    ```

13. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

14. Access your To-Do List application in your web browser at `http://localhost:8000`.

