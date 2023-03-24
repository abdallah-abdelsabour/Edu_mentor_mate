# Generated by Django 4.1.7 on 2023-03-23 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roomsession', '0002_alter_sessiondate_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomsession',
            name='ended_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='roomsession',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='roomsession',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]