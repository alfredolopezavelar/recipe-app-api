"""
Database models
"""

from django.db import models  # noqa
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    """Manager for users"""
    
    def create_user(self, email, password=None, **extra_field):
        """Create, save and return a new user."""
        


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""

    # AbstractBaseUser -> contains the functionality for the authetication 
    # PermissionMixin -> contains the functionality for the persmissions of the user 

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'