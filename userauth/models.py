from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#When Profile is made,  its attached too user which made it (one2One), If user deleted remove profile
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')#Default image (create field etc) and where to upload on server OVERRIDDEN BY MEDIA ROOT CHECK SETTINGS

    def __str__(self):
        return f'{self.user.username} Profile'



