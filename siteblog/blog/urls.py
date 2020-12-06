from django.urls import path

from .views import Category, Post, Tag


urlpatterns = [
    path('', index, name='home'),
]