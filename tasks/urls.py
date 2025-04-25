from django.urls import path
from . import views
from django.urls import include

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('date/<int:year>/<int:month>/<int:day>/', views.task_by_date, name='task_by_date'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>', views.delete_task, name='delete_task'),
    
]   