from django.shortcuts import render
from .models import *
from .forms import *
from django import forms
from django.http import HttpResponse, JsonResponse, FileResponse, Http404

# Create your views here.
def Landing_Page(request):
    return render(request, 'Landing Page.html')

def Booking_Page(request):
<<<<<<< HEAD
<<<<<<< HEAD
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

=======
=======
>>>>>>> parent of 4641f42... form works just won't save to database

# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('Landing Page')
            
        # if a GET (or any other method) we'll create a blank form
    else:
        form = BookingForm()
        
>>>>>>> parent of 4641f42... form works just won't save to database
    return render(request, 'Booking.html', {'form': form})
