from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('Please enter email')
        
        ne = self.normalize_email(email)
        user = self.model(email=ne,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user=self.create_user(email, first_name, last_name, password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    is_active=models. BooleanField(default=True) 
    is_staff=models. BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    def _str_(self):
        return self.first_name+" "+self.last_name