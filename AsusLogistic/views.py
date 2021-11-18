from django.shortcuts import render
from .models import *
from .forms import *
from shapeshifter.views import MultiFormView

# Create your views here.
def Landing_Page(request):
    return render(request, "Landing Page.html")

context = {
    'ItemForm': ItemForm(),
    'SenderForm': SenderForm()
}

def Booking_Page(request):
    if request.method == "POST":
        form = ItemForm(request.POST or None)
        if form.is_valid():
            obj = Item() #gets new object
            obj.item_name = form.cleaned_data['item_name']
            obj.item_width = form.cleaned_data['item_width']
            obj.item_height = form.cleaned_data['item_height']
            obj.item_length = form.cleaned_data['item_length']
            #finally save the object in db
            obj.save()
    else:
        form = ItemForm()
    return render(request, "Booking.html", context)

def Sender_details(request):
    if request.method == "POST":
        form2 = SenderForm(request.POST or None)
        if form2.is_valid():
            obj = Sender() #gets new object
            obj.name = form2.cleaned_data['name']
            obj.email = form2.cleaned_data['email']
            obj.phone_number = form2.cleaned_data['phone_number']
            #finally save the object in db
            obj.save()
    else:
        form2 = SenderForm()
    return render(request, "Booking.html", context)
