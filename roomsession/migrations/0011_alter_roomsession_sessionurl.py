# Generated by Django 4.1.7 on 2023-04-05 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomsession', '0010_roomsession_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomsession',
            name='sessionUrl',
            field=models.URLField(blank=True),
        ),
    ]