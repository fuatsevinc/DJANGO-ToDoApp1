from django.shortcuts import render
from todo.forms import ListForm
from .models import Todos

# Create your views here.

def index(request):



    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todo_list = Todos.objects.all()
            return render(request, "todo/index.html", {'todo_list':todo_list})
    else:
        todo_list = Todos.objects.all()
        return render(request, "todo/index.html", {'todo_list':todo_list})

def home(request):
    return render(request, "todo/home.html" )

def about(request):
    return render(request, "todo/about.html" )

def link(request):
    return render(request, "todo/link.html")

def create(request):
    return render(request, "todo/create.html")

