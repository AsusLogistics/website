from django import forms
from .import models
from django.forms import ModelForm

class BookingForm(forms.ModelForm):
    
    class Meta:
        model = models.Item
        fields = ['item_name', 'item_width', 'item_height', 'item_length']