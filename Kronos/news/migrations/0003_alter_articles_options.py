# Generated by Django 5.0 on 2024-02-07 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_articles_delete_players'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
