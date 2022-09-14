from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos


# Create your views here.

def index(request):
    todo_list = Todos.object.all()
    return render(request, "todo/index.html", {'todo_list':todo_list})

def home(request):
    return render(request, "todo/home.html" )

def about(request):
    return render(request, "todo/about.html" )

def link(request):
    return render(request, "todo/link.html")

def create(request):
    return render(request, "todo/create.html")

