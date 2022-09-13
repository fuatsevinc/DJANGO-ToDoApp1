from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('link/', views.link, name="link"),
    path('create/', views.create, name="create"), 
    ]
