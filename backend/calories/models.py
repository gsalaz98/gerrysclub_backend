from datetime import datetime, timedelta

from django.db import models

class Calories(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ts = models.DateTimeField('ts', auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    food_name = models.CharField('name', blank=False, null=False, max_length=32, default='Food')
    time_eaten = models.DateTimeField('t_eat', blank=True, null=True)
    restaurant = models.CharField('name', blank=True, null=True, max_length=64)

    weight_before = models.FloatField('weight_before', blank=True, null=True)
    weight_after = models.FloatField('weight_after', blank=True, null=True)
    isbn = models.FloatField('isbn', blank=True, null=True)

    calories = models.FloatField('calories', null=False, default=0.00)
    # This differs from servings as servings can have multiple quantities for a single serving
    quantity = models.FloatField('quantity', blank=True, null=True)
    servings = models.FloatField('servings', blank=True, null=True)
    calories_per_serving = models.FloatField('kcal_per_serving', blank=True, null=True)

class Weight(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ts = models.DateTimeField('ts', auto_now_add=True, null=True)

    weight = models.FloatField('weight', blank=False, null=False)
    kg = models.BooleanField('kg', blank=False, null=False, default=False)
    food_eaten_before = models.BooleanField('food_eaten_before', blank=False, null=False)
    food_weight = models.FloatField('food_weight', blank=True, null=True)
