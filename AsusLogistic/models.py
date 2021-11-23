from django.db import models
from django.conf import settings

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=12, null=True)
    password = models.CharField(max_length=15, null=True)

class Sender(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone_number =  models.CharField(max_length=200, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    customer_address = models.CharField(max_length=200, null=True)
    customer_email = models.CharField(max_length=200, null=True)
    customer_phone_number = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    item_name = models.CharField(max_length=200, null=True)
    item_width = models.CharField(max_length=200, null=True)
    item_height = models.CharField(max_length=200, null=True)
    item_length = models.CharField(max_length=200, null=True)
    sender_ID = models.ForeignKey(Sender, default=None, null=True, on_delete=models.CASCADE)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.first_name

class CollectPoint(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200, null=True)
    town = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)

class Drop(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200, null=True)
    town = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)
