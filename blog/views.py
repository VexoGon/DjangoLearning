from django.shortcuts import render
from django.http import HttpResponse #Don't know why we need this but we do

def home(request):
    return HttpResponse('<h1>Blog Home</h1>') #When this view (when home func) is called this is what will return

def about(request):
    return HttpResponse('<h1><About Pageasdsadsadsadsadasdsadsaaaaaaaaa/h1>') #Created another view - this is done why about() is called

# Create your views here.
