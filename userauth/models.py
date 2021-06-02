from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #When Profile is made, User it is attached too user (one2One), If user deleted remove profile
    image = models.ImageField(default='default.jpg', upload_to='Profile_pics') #Default image (create field etc) and where to upload on server

    def __str__(self):
        return f'{self.user.username} Profile'



