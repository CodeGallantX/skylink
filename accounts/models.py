from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(_('phone number'), max_length=20, blank=True)
    is_verified = models.BooleanField(_('verified'), default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    passport_number = models.CharField(max_length=50, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()}'s Profile"