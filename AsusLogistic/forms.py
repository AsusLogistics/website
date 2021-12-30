from django import forms
from .models import *

class DeliveryForm(forms.ModelForm):

    class Meta:
        model = Delivery
        fields = ('first_name', 'last_name', 'customer_address', 'customer_email', 'customer_phone_number', 'city', 'postcode', 'county', 'item_name','item_width','item_height','item_length')

class SenderForm(forms.ModelForm):

    class Meta:
        model = Sender
        fields = ('name','email','phone_number')