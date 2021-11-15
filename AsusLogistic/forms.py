from django import forms
from .import models
from django.forms import ModelForm
<<<<<<< HEAD
from .models import *
from django.utils.safestring import mark_safe
=======
>>>>>>> parent of 4641f42... form works just won't save to database

class BookingForm(forms.ModelForm):

    class Meta:
<<<<<<< HEAD
        model = Item
        fields = ('item_name','item_width', 'item_height', 'item_length')

    def clean_item_name(self):
        item_name = self.cleaned_data['item_name'].lower()
        try:
           item = Item.objects.get(item_name=item_name)
        except Exception as e:
            return item_name
=======
        model = models.Item
        fields = ['item_name', 'item_width', 'item_height', 'item_length']
>>>>>>> parent of 4641f42... form works just won't save to database
