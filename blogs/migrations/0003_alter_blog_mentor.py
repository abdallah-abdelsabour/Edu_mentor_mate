# Generated by Django 4.1.7 on 2023-03-23 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0002_remove_blog_text_rendered_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]