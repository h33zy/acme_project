from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    bio = models.TextField(verbose_name='Биография', blank=True)
