from django import forms
from .models import *

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_name','item_width','item_height','item_length')

class SenderForm(forms.ModelForm):

    class Meta:
        model = Sender
        fields = ('name','email','phone_number')
