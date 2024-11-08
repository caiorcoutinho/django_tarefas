# Generated by Django 5.1.2 on 2024-11-03 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_remove_task_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='cost',
            field=models.FloatField(verbose_name='Custo'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(verbose_name='Data Limite'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=400, verbose_name='Nome da Tarefa'),
        ),
    ]
