# Generated by Django 4.2.4 on 2023-10-27 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_completed',
            new_name='is_finished',
        ),
    ]
