from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Avatar')
    date_of_birth = models.DateTimeField(null=True, blank=True, verbose_name='Date of Birth')
    city = models.CharField(max_length=50, null=True, blank=True)
