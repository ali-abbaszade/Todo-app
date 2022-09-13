from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required


@login_required(login_url='users:login')
def index_view(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    count = tasks.filter(status=False).count()

    if request.method == "GET":
        if search := request.GET.get('search'):
            tasks = tasks.filter(body__icontains=search)

        
    context = {'tasks':tasks, 'count':count}    
    return render(request, 'index.html', context)


@login_required(login_url='users:login')
def create_view(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')
    return render(request, 'create.html', {'form':form})


@login_required(login_url='users:login')
def delete_view(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task':task})
    
@login_required(login_url='users:login')    
def update_view(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        form.save()
        return redirect('/')

    return render(request, 'update.html', {'form':form})


@login_required(login_url='users:login')
def finish_task(request, id):
    task = Task.objects.get(id=id)
    task.status = True
    task.save()

    return redirect('/')

