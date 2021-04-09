from django.db import models
from django.utils import timezone #Check docs, but this is just field types i think
from django.contrib.auth.models import User #Django made us a user model use it
# Create your models here.

class post(models.Model): #Every class creates a database table
    title = models.CharField(max_length=10) #This is a field in database, Charfield is just the type of field
    content = models.TextField(blank=True)
    dateposted = models.DateTimeField(default=timezone.now) #Check docs for different types
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Finds author, from the User table from Django and on delete of user removes post again, google. User is the current logged in user
    #Forign key basically connect them together (user and Post classes (you can't remove User without Post))
    def __str__(self):
        return self.title #__STR__ what to show when printed
    
#When user creates post an object is made with this class

#To create this easily pair with admin.py (project dir)

