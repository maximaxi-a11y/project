from django.urls import path
from . import views

urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    path('task_submitted/', views.task_submitted, name='task_submitted'),
    path('moderation/', views.moderation, name='moderation'),
    path('moderate_task/<int:task_id>/', views.moderate_task, name='moderate_task'),
    path('', views.tasks),
     path('<int:news_id>', view=views.news_detail),
]