from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def Landing_Page(request):
    return render(request, "Landing Page.html")

def Landing_Test(request):
    return render(request, 'Landing_test.html')

def Booking_Page(request):
    # create a form instance and populate it with data from the request:
    form = BookingForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        customer = form.save(commit=False)
        customer.is_active = False
        form.save()
        # process the data in form.cleaned_data as required
        item_name = form.cleaned_data.get('item_name').lower()
        # redirect to a new URL:
        return HttpResponseRedirect('Landing Page')

context = {
    'DeliveryForm': DeliveryForm(),
    'SenderForm': SenderForm()
}

def Booking_Page(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST or None)
        if form.is_valid():
            obj = Delivery() #gets new object
            obj.customer = obj.customer = form.cleaned_data['customer']
            obj.customer_email = obj.customer_email = form.cleaned_data['customer_email']
            obj.customer_phone_number = obj.customer_phone_number = form.cleaned_data['customer_phone_number']
            obj.item_name = form.cleaned_data['item_name']
            obj.item_width = form.cleaned_data['item_width']
            obj.item_height = form.cleaned_data['item_height']
            obj.item_length = form.cleaned_data['item_length']
            #finally save the object in db
            obj.save()
        return HttpResponseRedirect('/')
    else:
        form = DeliveryForm()
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
