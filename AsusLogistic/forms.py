from django import forms
from .models import *

class DeliveryForm(forms.ModelForm):

    class Meta:
        model = Delivery
        fields = ('customer', 'customer_email', 'customer_phone_number', 'item_name','item_width','item_height','item_length')

class SenderForm(forms.ModelForm):

    class Meta:
        model = Sender
        fields = ('name','email','phone_number')
