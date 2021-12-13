from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model
from .models import *

UserModel = get_user_model()

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address.")
    
    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
           account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use.")
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
           account = Account.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Username {username} is already in use.")

class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('username', 'email', 'profile_image', 'hide_email' )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)


    def save(self, commit=True):
        account = super(AccountUpdateForm, self).save(commit=False)
        account.username = self.cleaned_data['username']
        account.email = self.cleaned_data['email'].lower()
        account.profile_image = self.cleaned_data['profile_image']
        account.hide_email = self.cleaned_data['hide_email']
        if commit:
            account.save()
        return account

class DeliveryForm(forms.ModelForm):

    class Meta:
        model = Delivery
        fields = ('first_name', 'last_name', 'customer_address', 'customer_email', 'customer_phone_number', 'city', 'postcode', 'county', 'item_name','item_width','item_height','item_length')

class SenderForm(forms.ModelForm):

    class Meta:
        model = Sender
        fields = ('name','email','phone_number')