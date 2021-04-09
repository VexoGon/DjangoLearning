from django.contrib import admin
from .models import post #gets post models from models.py
# Register your models here.

admin.site.register(post) #Connects model with admin page