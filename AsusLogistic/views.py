from django.shortcuts import render
from .models import *
from .forms import *
from shapeshifter.views import MultiFormView

# Create your views here.
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
