from django.urls import path

from calories.views import index, calories

urlpatterns = [
    path('', index),
    path('counter/', calories)
]