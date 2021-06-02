"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#Where URL's are processed
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as authviews #Login, Logout views
from userauth import views as auth_views #allows us to access our auth views

urlpatterns = [
    path('admin/', admin.site.urls), #when we go to 'admin/' Go to admin.site.urls
    path('blog/', include('blog.urls')), #When we go to blog/ Go to the blog app URLS file. 'Blog/' Anything past the / is path var in views.py in app (this case blog)
    path('register/',auth_views.register, name='register'), #Calls register view func
    path('login/', authviews.LoginView.as_view(template_name='users/login.html'), name='login'), #Renders premade Django login view (creates form etc) Template just changes a few things up (our html).
    #Above also checks login matches User, If so, it logins a user in under that Model so we can do User. etc
    #path('logout/', authviews.LogoutView.as_view(template_name='users/logout.html'), name='logout'), #Doesn't use default temp
    path('logout/', authviews.LogoutView.as_view(template_name='users/logout.html'), name='logout'),#Uses custom temp
    path('profile/', auth_views.profile, name='profile'), 

]
