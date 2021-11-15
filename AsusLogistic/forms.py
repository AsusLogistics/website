from django import forms
from .import models
from django.forms import ModelForm
from .models import *

class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('item_name', 'item_width', 'item_height', 'item_length')
    
    def clean_item_name(self):
        item_name = self.cleaned_data['item_name'].lower()
        try:
           item = Item.objects.get(item_name=item_name)
        except Exception as e:
            return item_name