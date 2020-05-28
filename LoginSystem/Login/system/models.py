from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#class SignUp(models.Model):
 #   username=models.CharField(max_length=80)
  #  email=models.EmailField(max_length=100)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username


