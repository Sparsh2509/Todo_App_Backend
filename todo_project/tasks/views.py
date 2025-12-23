
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

@login_required
def task_list(request):

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user   # 🔥 OWNER SET
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    tasks = Task.objects.filter(user=request.user)

    return render(request, "tasks/task_list.html", {
        "form": form,
        "tasks": tasks
    })


@login_required
def toggle_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.delete()
    return redirect("task_list")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # auto login after signup
            return redirect("task_list")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {
        "form": form
    })

