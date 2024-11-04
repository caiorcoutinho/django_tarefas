"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import ToDoListView, TaskCreateView, TaskUpdateView, TaskDeleteView

from tasks.views import update_task_order



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ToDoListView.as_view(), name="task_list"),
    path('create/', TaskCreateView.as_view(), name="task_create"),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),

    path('update-order/', update_task_order, name='update_task_order'),
]
