from django.shortcuts import render #Allows us to render templates
from django.http import HttpResponse #Don't know why we need this but we do
from .models import post #In same dir so . is good


posts = [ #Dumb data NOT IN USE NOW
    {
        'author':'Matt',
        'title':'Blog Post 1',
        'Content':'First Post Content',
        'Date_posted':'2021',
    },
    {
        'author':'Testing',
        'title':'Blog Post 2',
        'Content':'First Post Content2',
        'Date_posted':'2020',   
    }
]

def home(request):
    context = { #Local Var for Context
    'posts': post.objects.all} #Key makes data accessable This returns all the data base models created

    #return HttpResponse('<h1>Blog Home</h1>') #When this view (when home func) is called this is what will return
    return render(request,'blog/home.html',context) #Looks inside templates file - then sub dirs
    #Context param allows us to access it in the template
def about(request):
    #return HttpResponse('<h1>About Pageasdsadsadsadsadasdsadsaaaaaaaaa/h1>') #Created another view - this is done when about() is called
    return render(request,'blog/about.html', {'title':'About'}) #Direct Pass in of title Context
# Create your views here.
