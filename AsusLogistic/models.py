from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Login(models.Model):
    email = models.CharField(max_length=12, null=True)
    password = models.CharField(max_length=15, null=True)

class Sender(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone_number =  models.CharField(max_length=200, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    customer_address = models.CharField(max_length=200, null=True)
    customer_email = models.CharField(max_length=200, null=True)
    customer_phone_number = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    item_name = models.CharField(max_length=200, null=True)
    item_width = models.CharField(max_length=200, null=True)
    item_height = models.CharField(max_length=200, null=True)
    item_length = models.CharField(max_length=200, null=True)
    sender_ID = models.ForeignKey(Sender, default=None, null=True, on_delete=models.CASCADE)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.first_name

class CollectPoint(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200, null=True)
    town = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)

class Drop(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200, null=True)
    town = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)


def get_profile_image_filepath():
    return f'profile_images/{self.pk}/{"profile_image"}'

def get_default_profile_image():
    return "profileImage/profile-picture-default.png"

class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	profile_image			= models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
	hide_email				= models.BooleanField(default=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.username

	def get_profile_image_filename(self):
		return str(self.profile_image)[str(self.profile_image).index('profileImages/' + str(self.pk) + "/"):]

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True