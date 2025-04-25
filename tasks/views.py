from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from datetime import date
from django.http import JsonResponse
from .form import TaskForm
# Create your views here.

@login_required
def task_list(request):
    today = request.GET.get('date', date.today())
    tasks = Task.objects.filter(user=request.user, due_date=today)
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'selected_date': today})
    

@login_required
def task_by_date(request, year, month, day):
    tasks = Task.objects.filter(
        user = request.user,
        due_date__year=year,
        due_date__month=month,
        due_date__day=day
    ).values('id', 'title', 'description', 'completed')
    
    return JsonResponse(list(tasks), safe=False)

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {
        'form': form,
        'form_title': '➕ Δημιουργία Νέας Εργασίας',
    })

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/create_task.html', {
        'form': form,
        'form_title': '✏️ Επεξεργασία Εργασίας',
    })
        
@login_required
def delete_task(request, task_id):
    task =get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task_list')

    return render(request, 'tasks/delete_task.html', {'task': task,})