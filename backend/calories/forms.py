from django.forms import ModelForm, TextInput, CheckboxInput
from calories.models import Calories, Weight

class CalorieForm(ModelForm):
    class Meta:
        model = Calories
        fields = [
            'food_name',
            'calories',
            'quantity',
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
            'quantity': 'Quantity',
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

        widgets = {
            'food_name': TextInput(attrs={
                'placeholder': 'Enter Food Name',
            }),
            'calories': TextInput(attrs={
                'placeholder': 'Enter Calories (kcal)',
            }),
            'quantity': TextInput(attrs={
                'placeholder': 'Enter Quantity (optional)',
                'class': 'optional',
            }),
            'servings': TextInput(attrs={
                'placeholder': 'Enter Servings (optional)',
                'class': 'optional'
            }),
            'calories_per_serving': TextInput(attrs={
                'placeholder': 'Enter Calories per Serving (optional)',
                'class': 'advanced'
            }),
            'restaurant': TextInput(attrs={
                'placeholder': 'Enter Restaurant Name (optional)',
                'class': 'advanced'
            }),
            'time_eaten': TextInput(attrs={
                'placeholder': 'Enter Time Eaten At (optional)',
                'class': 'advanced'
            }),
            'weight_before': TextInput(attrs={
                'placeholder': 'Enter Weight Before (optional)',
                'class': 'advanced'
            }),
            'weight_after': TextInput(attrs={
                'placeholder': 'Enter Weight After (optional)',
                'class': 'advanced'
            })
        }


class WeightForm(ModelForm):
    class Meta:
        model = Weight

        fields = [
            'weight',
            'kg',
            'food_eaten_before',
            'food_weight'
        ]

        labels = {
            'weight': 'Weight',
            'food_weight': 'Food Weight',
            'kg': 'Kilograms',
            'food_eaten_before': 'Food Eaten Before Weigh-in',
        }
        widgets = {
            'weight': TextInput(attrs={
                'placeholder': 'Enter your weight'
            }),
            'food_weight': TextInput(attrs={
                'placeholder': 'Enter food weight (optional)'
            })
        }

    field_order = ['weight', 'food_weight', 'kg', 'food_eaten_before']
