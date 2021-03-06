from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile


class userReg(UserCreationForm): #Init fuction already creates us other shit (form).
    email = forms.EmailField()

    class meta(): #Tells django which model to save this data too, must be called Meta always
        model = User #Affect model - Basically, will save UserReg to User Model
        fields = ['username','email','password1','password2'] #These are the fields we want saved



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']