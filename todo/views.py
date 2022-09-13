from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "todo/index.html", {"name":"Fuat SEVINC"} )

def home(request):
    return render(request, "todo/home.html", {"namex":"HOME PAGE"} )

def about(request):
    return render(request, "todo/about.html", {"surname":"ABOUT SAYFASI"} )

def link(request):
    return render(request, "todo/link.html", {"tamname":"LINK SAYFASI"} )

def create(request):
    return render(request, "todo/create.html", {"pagename":"CRAETA Page"} ) 