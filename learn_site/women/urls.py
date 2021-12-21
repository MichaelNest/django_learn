from django.urls import path
from .views import index, cat

urlpatterns = [
    path('', index),
    path('categories/', cat)
]