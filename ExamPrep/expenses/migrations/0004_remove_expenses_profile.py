# Generated by Django 3.1.5 on 2021-01-22 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_expenses_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='profile',
        ),
    ]