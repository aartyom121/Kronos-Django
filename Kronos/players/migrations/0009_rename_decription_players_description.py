# Generated by Django 5.0 on 2024-05-23 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_players_decription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='players',
            old_name='decription',
            new_name='description',
        ),
    ]
