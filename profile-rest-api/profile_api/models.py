from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, username, password=None):
        """Create a new user profile"""
        if not username:
            raise ValueError('Users must have an username')

        
        user = self.model(username=username)
        user.set_password(password) 
        user.save(using=self._db) #saving objects in django
        return user 

    def create_superuser(self, username, password):
        """Create a new superuser"""
        user=self.create_user( username, password)

        user.is_superuser = True #is_superuser and is_staff are created by PermisssionMixin
        user.is_staff = True
        user.save(using=self.db)
        
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for users in the system """

    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD='username'

    def get_username(self):
        """Retrieve username"""
        return self.username
    
    
    #Convert an object to a string in Python
    def __str__(self):
        """Return string representation of our user"""
        return self.username 
