from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Task

from django.contrib import messages
from django.urls import reverse

class ToDoListView(ListView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    fields = ['name', 'cost', 'deadline']
    success_url = reverse_lazy("task_list")
    def form_invalid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        error_message = "Já existe uma tarefa com esse nome." if form.errors['name'][0] == 'Task com este Nome da Tarefa já existe.' else form.errors['name'][0]
        return HttpResponseRedirect(f'{self.success_url}?error={error_message}')
        '''url = reverse("task_list", kwargs={'errors': form.errors['name']})
        return HttpResponseRedirect(url)'''
    

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['name', 'cost', 'deadline']
    success_url = reverse_lazy("task_list")
    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task_list")


def update_task_order(request):
    if request.method == 'POST':
        try:
            tasks_data = json.loads(request.POST.get('tasks'))
            for task_data in tasks_data:
                task_id = task_data['id']
                new_order = task_data['order']

                task = Task.objects.get(id=task_id)
                task.order = new_order
                task.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False}, status=400)
