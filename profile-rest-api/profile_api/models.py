from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email= self.normalize_email(email)
        user=self.model(email=email , name=name)

        user.set_password(password) 
        user.save(using=self._db) #saving objects in django

        return user 
    def create_superuser(self, email, name, password):
        """Create and save a new suoeruser with given details"""
        user=self.create_user(email, name, password)

        user.is_superuser=True #is_superuser and is_staff are created by PermisssionMixin
        user.is_staff= True
        user.save(using=self.db)
        
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' #username is replaced by email
    REQUIRED_FIELDS = ['name', ]

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    
    #Convert an object to a string in Python
    def __str__(self):
        """Return string representation of our user"""
        return self.email 



