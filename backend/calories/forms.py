from django.forms import ModelForm, TextInput
from calories.models import Calories

class CalorieForm(ModelForm):
    class Meta:
        model = Calories
        fields = ['food_name', 'calories']

        labels = {
            'food_name': 'Food Name',
            'calories': 'Calories/kcals'
        }
        widgets = {
            'food_name': TextInput(attrs={
                'placeholder': 'Enter Food Name'
            }),
            'calories': TextInput(attrs={
                'placeholder': 'Enter Calories/kcal',
            })
        }