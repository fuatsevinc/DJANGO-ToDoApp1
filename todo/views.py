from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("burasi index sayfasi")


def about(request):
    return HttpResponse("burasi about sayfasi")