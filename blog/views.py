from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm
from django.views.decorators.http import require_POST


def index(request):
    todo = ToDo.objects.all()
    form = ToDoForm()
    return render(request, 'index.html', {'todo_list': todo, 'form': form})


@require_POST
def addTodo(request):
    form = ToDoForm(request.POST)
    if form.is_valid():
        new_todo = ToDo(text=request.POST['text'])
        new_todo.save()
    return redirect('/')


def complete_todo(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    if todo.complete:
        todo.complete = False
        todo.save()
    else:
        todo.complete = True
        todo.save()
    return redirect('index')


def delete_completed(request):
    ToDo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def delete_all(request):
    ToDo.objects.all().delete()
    return redirect('index')

