# Generated by Django 4.0.1 on 2022-05-17 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marmot', '0002_remove_user_favorites_user_liked_user_watched_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
