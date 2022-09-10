from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task

def index_view(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}    
    return render(request, 'index.html', context)


def create_view(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create.html', {'form':form})



def delete_view(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')    
    
def update_view(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        form.save()
        return redirect('/')

    return render(request, 'update.html', {'form':form})

def finish_task(request, id):
    task = Task.objects.get(id=id)
    task.status = True
    task.save()

    return redirect('/')


            
