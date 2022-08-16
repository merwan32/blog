from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    work = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profilepics',default='profilepics/default-user.png')

class Post(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    type = models.CharField(max_length=100, blank=True)
    titre = models.CharField(max_length=500, blank=True)
    text = models.CharField(max_length=1000, blank=True)
    time = models.DateTimeField(auto_now=True)
