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
   
   class Category(models.Model):
       name = models.CharField(max_length=100)
   
       def __str__(self):
           return self.name
   
   class Task(models.Model):
       title = models.CharField(max_length=200)
       description = models.TextField()
       category = models.ForeignKey(Category, on_delete=models.CASCADE)
   
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
   from django.shortcuts import render
   from .models import Task
   
   def task_list(request):
       tasks = Task.objects.all()
       return render(request, 'todoapp/task_list.html', {'tasks': tasks})
   
   def add_task(request):
       if request.method == 'POST':
           # Handle form submission and task creation here
       return render(request, 'todoapp/add_task.html')
   ```

10. Create HTML templates for your views. Place them in a folder named `templates/todoapp`:

   `task_list.html`:

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>To-Do List</title>
   </head>
   <body>
       <h1>Task List</h1>
       <ul>
           {% for task in tasks %}
               <li>{{ task.title }}</li>
           {% endfor %}
       </ul>
   </body>
   </html>
   ```

   `add_task.html`:

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Add Task</title>
   </head>
   <body>
       <h1>Add Task</h1>
       <form method="post">
           {% csrf_token %}
           <label for="title">Title:</label>
           <input type="text" id="title" name="title" required><br>
           <label for="description">Description:</label>
           <textarea id="description" name="description" required></textarea><br>
           <label for="category">Category:</label>
           <select id="category" name="category">
               {% for category in categories %}
                   <option value="{{ category.id }}">{{ category.name }}</option>
               {% endfor %}
           </select><br>
           <input type="submit" value="Add Task">
       </form>
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

## Next Steps

You've created a basic To-Do List application. To expand on this project, consider adding features like editing tasks, deleting tasks, user authentication, and improving the user interface. Refer to the Django documentation for more information: [Django Documentation](https://docs.djangoproject.com/en/stable/).

Happy coding!
```

You can save this Markdown content to a `README.md` file in your project directory for clear and concise documentation.