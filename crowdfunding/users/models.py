from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): # AbstractUser is a Django's built-in user model that provides complete default implementation of a user model for CustomUser class

    def __str__(self):
        return self.username
