# Generated by Django 5.0 on 2024-03-29 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_results_res1_results_res10_results_res2_results_res4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='res3',
            field=models.CharField(default=0, max_length=300, verbose_name='Результат 3'),
        ),
    ]
