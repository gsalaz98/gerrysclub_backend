# Generated by Django 2.1.3 on 2018-12-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0008_auto_20181105_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='calories',
            name='quantity',
            field=models.FloatField(blank=True, null=True, verbose_name='quantity'),
        ),
    ]
