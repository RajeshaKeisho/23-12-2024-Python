from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

# FBv
def task_list_create(request):
    tasks = Task.objects.all()

    if request.method =="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_list.html', {"tasks":tasks, 'form':form})

def update_task(request, pk):
    task = get_object_or_404(Task, pk)
    if request.method =="POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form':form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk)
    if request.method =="POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task':task})


from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task


class TaskListCreateView(CreateView, ListView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_list.html"
    success_url = reverse_lazy('cbv_task_list')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['tasks'] = Task.objects.all()
        return context
    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy('cbv_task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy('cbv_task_list')