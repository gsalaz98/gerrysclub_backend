# Generated by Django 2.1.2 on 2018-10-25 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='caloriecounter',
            name='calories',
            field=models.FloatField(default=0.0, verbose_name='calories'),
        ),
        migrations.AddField(
            model_name='caloriecounter',
            name='food_name',
            field=models.CharField(blank=True, default='Food', max_length=32, null=True, verbose_name='name'),
        ),
    ]
