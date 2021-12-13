from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('id', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Account, AccountAdmin)

class AsusManagement(admin.ModelAdmin):
    pass
admin.site.register(Login, AsusManagement)

class AsusManagement(admin.ModelAdmin):
    pass
admin.site.register(Sender, AsusManagement)

class DeliveryManagement(admin.ModelAdmin):
    pass
admin.site.register(Delivery, AsusManagement)

class CollectionManagement(admin.ModelAdmin):
    pass
admin.site.register(CollectPoint, AsusManagement)

class DropManagement(admin.ModelAdmin):
    pass
admin.site.register(Drop, AsusManagement)
