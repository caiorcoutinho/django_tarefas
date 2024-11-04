from django.db import models


#id
#name
#cost
#deadline
#pos

class Task(models.Model):
    name = models.CharField(verbose_name='Nome da Tarefa', max_length=400, null=False, blank=False, unique=True,)
    cost = models.FloatField(verbose_name='Custo', null=False, blank=False)
    deadline = models.DateField(verbose_name='Data Limite', null=False, blank=False)
    order = models.PositiveIntegerField(null=True, blank=True, editable=True)  # Campo auto-incrementado

    class Meta:
            ordering = ['order']

    def save(self, *args, **kwargs):
        if self.order is None:  # Verifica se o campo 'order' não foi definido
            last_order = Task.objects.aggregate(models.Max('order'))['order__max']
            if last_order is None:
                self.order = 1  # Começa em 1 se não houver tarefas
            else:
                self.order = last_order + 1  # Incrementa o último valor
        super().save(*args, **kwargs)

        