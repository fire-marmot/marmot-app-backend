# Generated by Django 4.0.1 on 2022-05-14 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marmot', '0002_alter_movies_movieid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='movieID',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movies',
            name='streaming_service',
            field=models.CharField(max_length=500),
        ),
    ]
