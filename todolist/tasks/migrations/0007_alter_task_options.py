# Generated by Django 5.1.2 on 2024-11-03 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['order']},
        ),
    ]
