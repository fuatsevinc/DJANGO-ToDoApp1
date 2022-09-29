from django.shortcuts import render, redirect
from todo.forms import ListForm
from .models import Todos


# Create your views here.

def index(request):
    if request.method=="POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todo_list= Todos.objects.all()
            return render(request, "todo/index.html", {'todo_list':todo_list})
    else:
        todo_list= Todos.objects.all()
        return render(request, "todo/index.html", {'todo_list':todo_list})

def home(request):
    return render(request, "todo/home.html" )

def about(request):
    return render(request, "todo/about.html" )

def link(request):
    return render(request, "todo/link.html")

def create(request):
    if request.method=="POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todo_list = Todos.objects.all()
            return render(request, "todo/create.html", {'todo_list':todo_list})
    else:
        todo_list = Todos.objects.all()
        return render(request, "todo/create.html", {'todo_list':todo_list})

def delete(request, Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.delete()
    return redirect("index")
  


def yesfinished(request, Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.finished= False
    todo.save()
    return redirect("index")

def nofinished(request, Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.finished= True
    todo.save()
    return redirect("index")

def update(request, Todos_id):
    if request.method=="POST":
        todo_list = Todos.objects.get(pk=Todos_id)
        form = ListForm(request.POST or None, instance=todo_list)
        if form.is_valid:
            form.save()
            return redirect("index")
    else:
        todo_list = Todos.objects.all()
        return render(request, "todo/update.html", {'todo_list':todo_list})
        
