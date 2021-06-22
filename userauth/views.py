from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm #Allows us to use django user form
from django.contrib import messages
from .forms import profileUpdateForm, userReg,UserUpdateForm #Gives us the extra forms in forms.py
# Create your views here. ANYTHING IN VIEW.PY CAN BE ACCESED IN TEMPLATES
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST': #If data sent back to view...
        form = userReg(request.POST) #Userreg - Already inherits from UserCreationForm so it does both, Usercrationform and adds forms 
        if form.is_valid(): #If infomation filled out to default standard
            form.save() #Creates a User autmatically.Auto from the UserCreationForm object, Saves Data from post request
            username = form.cleaned_data.get('username')#Gets username from Dir
            #messages.success(request, f'Account Created for {username}')#Sends Message Request to base.html
            messages.success(request, f'Your account has been created. Please login')
            return redirect('login')#Name of URL pattern for login
            #return redirect('blog-home')#Blog-home name of url pattern for blog

    else: #If Data not being sent but needs to be entered
        form = userReg() #Creates an instance of form every time called gives empty form
    return render(request, 'users/register.html', {'form': form}) #The context for form instance But this time unlike in blog we didn't use var. And call's register.html obvs
#This view is called direct from urls.py in project
@login_required
def profile(request):
    u_form = UserUpdateForm(instance=request.user)#Auto fills with signed in Users info ready to change
    p_form = profileUpdateForm(instance=request.user.profile)#Works  because one2one


    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
#This Code first renders