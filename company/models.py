from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    industry = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)  # Make address optional
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class Individual(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name    
    
    






