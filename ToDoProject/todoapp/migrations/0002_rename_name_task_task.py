# Generated by Django 4.1.5 on 2023-06-23 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Name',
            new_name='Task',
        ),
    ]
