from django.db import models
from django.conf import settings
from django.utils import timezone
from django.shortcuts import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200, null=True)
    item_width = models.CharField(max_length=200, null=True)
    item_height = models.CharField(max_length=200, null=True)
    item_length = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def publish(self):
        self.save()

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
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)

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
