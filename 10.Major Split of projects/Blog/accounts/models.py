# accounts/models.py
from django.contrib.auth.models import AbstractUser

from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_image = models.ImageField(  null=True, blank=True, default='profile_image/default.jpg',upload_to ='profile_image/')
  
