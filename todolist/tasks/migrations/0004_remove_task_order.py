# Generated by Django 5.1.2 on 2024-11-03 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='order',
        ),
    ]