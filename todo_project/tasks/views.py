from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")

    form = TaskForm()
    tasks = Task.objects.all()

    return render(request, "tasks/task_list.html", {
        "form": form,
        "tasks": tasks
    })

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("task_list")