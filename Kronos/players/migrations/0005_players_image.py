# Generated by Django 5.0 on 2024-05-23 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_alter_players_amplua'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images/shop', verbose_name='Изображение'),
        ),
    ]
