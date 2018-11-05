# Generated by Django 2.1.3 on 2018-11-04 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0005_auto_20181025_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='calories',
            name='calories_per_serving',
            field=models.FloatField(blank=True, null=True, verbose_name='kcal_per_serving'),
        ),
        migrations.AddField(
            model_name='calories',
            name='isbn',
            field=models.FloatField(blank=True, null=True, verbose_name='isbn'),
        ),
        migrations.AddField(
            model_name='calories',
            name='restaurant',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='calories',
            name='time_eaten',
            field=models.DateTimeField(blank=True, null=True, verbose_name='t_eat'),
        ),
        migrations.AddField(
            model_name='calories',
            name='weight_after',
            field=models.FloatField(blank=True, null=True, verbose_name='weight_after'),
        ),
        migrations.AddField(
            model_name='calories',
            name='weight_before',
            field=models.FloatField(blank=True, null=True, verbose_name='weight_before'),
        ),
    ]
