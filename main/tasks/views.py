from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, ModerateTaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # Пометить, что задача ожидает модерации
            task.is_approved = False
            task.save()
            return redirect('task_submitted')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})


def moderate_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        form = ModerateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('moderation')
    else:
        form = ModerateTaskForm(instance=task)
    return render(request, 'tasks/moderate_task.html', {'form': form, 'task': task})


@login_required
def task_submitted(request):
    return render(request, 'tasks/task_submitted.html')

@staff_member_required
def moderation(request):
    tasks_to_moderate = Task.objects.filter(is_approved=False)
    return render(request, 'tasks/moderation.html', {'tasks_to_moderate': tasks_to_moderate})

@staff_member_required
def moderate_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        form = ModerateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('moderation')
    else:
        form = ModerateTaskForm(instance=task)
    return render(request, 'tasks/moderate_task.html', {'form': form, 'task': task})



def tasks(request):
    news = Task.objects.filter(is_approved=True)
    return render(request, 'tasks/tasks_list.html', {'news': news })

def news_detail(request, news_id):
    news = get_object_or_404(Task.objects.filter(is_approved=True), pk=news_id)
    return render(request, 'tasks/task.html', {'news': news})