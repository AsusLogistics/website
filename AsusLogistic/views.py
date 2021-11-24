from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.

def Login(request):
    username = 'not logged in'
    if request.method == 'POST':
      MyLoginForm = LoginForm(request.POST)
      if MyLoginForm.is_valid():
         username = LoginForm.cleaned_data['username']
         request.session['username'] = username
      else:
        MyLoginForm = LoginForm()
        return HttpResponseRedirect('Menu')
    return render(request, 'Login.html', {'username':username})

def formView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'loggedin.html', {"username" : username})
   else:
      return render(request, 'login.html', {})

def Menu_Page(request):
    return render(request, "Menu.html")

def Landing_Page(request):
    return render(request, "Landing Page.html")

context = {
    'DeliveryForm': DeliveryForm(),
    'SenderForm': SenderForm()
}

def Booking_Page(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST or None)
        if form.is_valid():
            obj = Delivery() #gets new object
            obj.first_name = obj.first_name = form.cleaned_data['first_name']
            obj.last_name = obj.last_name = form.cleaned_data['last_name']
            obj.customer_address = obj.customer_address = form.cleaned_data['customer_address']
            obj.customer_email = obj.customer_email = form.cleaned_data['customer_email']
            obj.customer_phone_number = obj.customer_phone_number = form.cleaned_data['customer_phone_number']
            obj.city = obj.city = form.cleaned_data['city']
            obj.postcode = obj.postcode = form.cleaned_data['postcode']
            obj.county = obj.county = form.cleaned_data['county']
            obj.item_name = obj.item_name = form.cleaned_data['item_name']
            obj.item_width = obj.item_width =form.cleaned_data['item_width']
            obj.item_height = obj.item_height = form.cleaned_data['item_height']
            obj.item_length = obj.item_length = form.cleaned_data['item_length']
            #finally save the object in db
            obj.save()
        return HttpResponseRedirect('/')
    else:
        form = DeliveryForm()
    return render(request, "Booking.html", context)

def Sender_Details(request):
    if request.method == "POST":
        form = SenderForm(request.POST or None)
        if form.is_valid():
            obj = Sender() #gets new object
            obj.name = obj.name = form.cleaned_data['name']
            obj.email = obj.email = form.cleaned_data['email']
            obj.phone_number = obj.phone_number = form.cleaned_data['phone_number']
            #finally save the object in db
            obj.save()
        return HttpResponseRedirect('/')
    else:
        form2 = SenderForm()
    return render(request, "Booking.html", context)
