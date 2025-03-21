from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

from django.db import models

class Company(models.Model):
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    industry = models.CharField(max_length=255 ,default="default")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
