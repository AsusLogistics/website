from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from .models import *
from .forms import *

# Create your views here.

def register_view(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse(f"You are already authenticated as " + str(user.email))

	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			password = form.cleaned_data.get('password')
			account = authenticate(email=email, password=password)
			login(request, account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect('Menu')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return redirect("/")

def login_view(request, *args, **kwargs):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("/")

    destination = get_redirect_if_exists(request)
    print("destination: " + str(destination))
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect("/")
        else:
            context['login_form'] = form
    return render(request, "login.html", context)

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.Get.get("next"))
    return redirect
# def LoginView(request):
#     username = 'not logged in'
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             request.session['username'] = username
#     else:
#         form = LoginForm()
#         return HttpResponseRedirect('Menu')
#     return render(request, 'Login.html', {'username':username})

# def formView(request):
#    if request.session.has_key('username'):
#       username = request.session['username']
#       return render(request, 'loggedin.html', {"username" : username})
#    else:
#       return render(request, 'login.html', {})

def Menu_Page(request):
    return render(request, "Menu.html")

def AnythingAnywhere(request):
    return render(request, "anythinganywhere.html")

def Homepage(request):
    return render(request, "Homepage.html")


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
