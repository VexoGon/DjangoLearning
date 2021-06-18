from django.db.models.signals import post_save #This signal gets sent when object is saved
from django.contrib.auth.models import User
from django.dispatch import receiver #Reciver preforms the task after signal
from .models import profile

@receiver(post_save, sender=User) #When user is saved send this Signal / Function
def create_profile(sender, instance,created,**kwargs): #All Of these args pasted by Reciever. KWAGS will expect any nonense from signaller
    if created:#If user just made
        profile.objects.create(user=instance)#Creates a profile for the instance / User which sent the signal
        



@receiver(post_save, sender=User) #When user is saved send this Signal / Function 
def save_profile(sender, instance,**kwargs): #All Of these args pasted by Reciever
    instance.profile.save()
