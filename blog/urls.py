from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='blog-home'), #Tells what view to return when app is called  then oes to view.py file and returns home func. '' EMPTY BECAUSE HOME PAGE NO PATH
     path('about/', views.about, name='blog-about'), #If blog/about call view.py about func
]
#Once mapped goto http://localhost:8000/blog/