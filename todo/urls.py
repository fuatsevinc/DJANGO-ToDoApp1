from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('link/', views.link, name="link"),
    path('create/', views.create, name="create"),
    path('delete/<Todos_id>', views.delete, name="delete"),
    path('yesfinished/<Todos_id>', views.yesfinished, name="yesfinished"),
    path('nofinished/<Todos_id>', views.nofinished, name="nofinished"),
    path('update/<Todos_id>', views.update, name="update"),
    ]
