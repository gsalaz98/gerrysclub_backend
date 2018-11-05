from django.forms import ModelForm, TextInput
from calories.models import Calories

class CalorieForm(ModelForm):
    class Meta:
        model = Calories
        fields = [
            'food_name',
            'calories',
            'servings',
            'calories_per_serving',
            'restaurant',
            'time_eaten',
            'weight_before',
            'weight_after',
        ]

        labels = {
            'food_name': 'Food Name',
            'calories': 'Calories (kcal)',
            'servings': 'Servings',
            'calories_per_serving': 'Calories per Serving',
            'restaurant': 'Restaurant Name',
            'time_eaten': 'Time Eaten At',
            'weight_before': 'Weight Before',
            'weight_after': 'Weight After',
        }

        advanced = [
            'servings',
            'calories_per_serving',
            'restaurant',
            'time_eaten',
            'weight_before',
            'weight_after',
        ]

        optional = [
            'servings',
            'calories_per_serving',
            'restaurant',
            'time_eaten',
            'weight_before',
            'weight_after',
        ]


        widgets = dict({
            k: TextInput(attrs={
                'placeholder': 'Enter %s' % v
            }) for k, v in labels.items()
            }, **{
                k: TextInput(attrs={
                    'class': 'optional'
                }) for k in optional
            }
        )