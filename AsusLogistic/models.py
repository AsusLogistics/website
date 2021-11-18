from django.db import models
from django.conf import settings

# Create your models here.
class Sender(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone_number =  models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.email

    def __str__(self):
        return self.phone_number

class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.CharField(max_length=200, null=True)
    customer_email = models.CharField(max_length=200, null=True)
    customer_phone_number = models.CharField(max_length=200, null=True)
    item_name = models.CharField(max_length=200, null=True)
    item_width = models.CharField(max_length=200, null=True)
    item_height = models.CharField(max_length=200, null=True)
    item_length = models.CharField(max_length=200, null=True)
    sender_ID = models.ForeignKey(Sender, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name

    def __str__(self):
        return self.item_width

    def __str__(self):
        return self.item_height

    def __str__(self):
        return self.item_length

    def __str__(self):
        return self.customer_email

    def __str__(self):
        return self.customer_phone_number
    
    def __str__(self):
        return self.customer

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
