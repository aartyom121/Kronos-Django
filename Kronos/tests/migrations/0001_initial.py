# Generated by Django 5.0 on 2024-03-08 12:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название теста')),
                ('created_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='Имя')),
                ('cor_ans', models.CharField(max_length=200, verbose_name='Корректный ответ')),
                ('uncor_ans1', models.CharField(max_length=200, verbose_name='Некорректный ответ 1')),
                ('uncor_ans2', models.CharField(max_length=200, verbose_name='Некорректный ответ 2')),
                ('uncor_ans3', models.CharField(max_length=200, verbose_name='Некорректный ответ 3')),
                ('test_number', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tests.test')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
