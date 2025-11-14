from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='api_overview'),
    path('list/', views.view_tasks, name='task_list'),
    path('detail/<int:pk>/', views.view_task, name='task_detail'),
    path('create/', views.add_items, name='task_create'),
    path('update/<int:pk>/', views.update_task, name='task_update'),
    path('delete/<int:pk>/', views.delete_task, name='task_delete'),
]
