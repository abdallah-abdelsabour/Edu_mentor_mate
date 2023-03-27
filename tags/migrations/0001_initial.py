# Generated by Django 4.1.7 on 2023-03-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=50)),
                ('degree', models.CharField(blank=True, choices=[('bachelor', 'Bachelor'), ('master', 'Master')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('caption', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
    ]
