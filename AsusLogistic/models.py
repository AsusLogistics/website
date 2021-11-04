from django.db import models
from django.conf import settings
from django.utils import timezone
from django.shortcuts import reverse



# Create your models here.
class Customer(models.Model):
    email = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    
