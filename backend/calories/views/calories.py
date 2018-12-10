from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Sum
from django.db.models.functions import TruncDate

from calories.models import Calories
from calories.forms import CalorieForm


@login_required
def calories(request):
    '''
    Get the calories the user has submitted and print them in a log. Show
    only the head of the calories where n = 10
    '''
    if request.method == 'GET':
        user_calories = Calories.objects.filter(user=request.user).order_by('-id')
        user_calories_truncated = user_calories.annotate(calorie_day=TruncDate('ts'))\
            .values('calorie_day')\
            .order_by('-calorie_day')\
            .annotate(calorie_sum=Sum('calories'))\
            .values('calorie_day', 'calorie_sum')

        return render(request, 'calories.html', context={
            'calories': user_calories,
            'calories_daily': user_calories_truncated,
            'calorie_form': CalorieForm(label_suffix='', initial={
                'food_name': None,
                'calories': None,
            }),
        })
    elif request.method == 'POST':
        calorie_form = CalorieForm(request.POST)

        if calorie_form.is_valid():
            form = calorie_form.save(commit=False)
            form.user = request.user
            form.save()

            return redirect('/counter/')

    else:
        return Http404()
