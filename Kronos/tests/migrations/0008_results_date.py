# Generated by Django 5.0 on 2024-05-27 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0007_results_res3'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Дата прохождения'),
        ),
    ]
