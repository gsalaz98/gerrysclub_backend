# Generated by Django 2.1.2 on 2018-10-25 10:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calories', '0003_auto_20181025_0633'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CalorieCounter',
            new_name='Calories',
        ),
    ]