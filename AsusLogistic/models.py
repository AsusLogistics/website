from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200, null=True)
    item_width = models.CharField(max_length=200, null=True)
    item_height = models.CharField(max_length=200, null=True)
    item_length = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.item_name

    def __str__(self):
        return self.item_width

    def __str__(self):
        return self.item_height

    def __str__(self):
        return self.item_length

class Sender(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.email

    def __str__(self):
        return self.phone_number

class Receiver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)

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

class Delivery(models.Model):
    collect_ID = models.ForeignKey(CollectPoint, default=None, on_delete=models.CASCADE)
    drop_ID = models.ForeignKey(Drop, default=None, on_delete=models.CASCADE)
    receiver_ID = models.ForeignKey(Receiver, default=None, on_delete=models.CASCADE)
    sender_ID = models.ForeignKey(Sender, default=None, on_delete=models.CASCADE)
