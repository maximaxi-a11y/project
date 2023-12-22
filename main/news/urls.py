from django.contrib import admin
from django.urls import path, include
from . import views
from .models import News


urlpatterns = [
    path('<int:news_id>', view=views.news_detail),
    path('', view=views.news_list),
]
