from django.urls import path

import calories.views
import frontend.views

urlpatterns = [
    path('', frontend.views.index),
    path('counter/', calories.views.calories),
]