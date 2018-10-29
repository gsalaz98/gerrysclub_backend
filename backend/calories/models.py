from datetime import datetime, timedelta

from django.db import models

class Calories(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ts = models.DateTimeField('ts', auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    food_name = models.CharField('name', blank=True, null=True, max_length=32, default='Food')
    calories = models.FloatField('calories', null=False, default=0.00)