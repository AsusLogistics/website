from django.contrib import admin
from .models import *

# Register your models here.
class AsusManagement(admin.ModelAdmin):
    pass
admin.site.register(Sender, AsusManagement)

class ItemManagement(admin.ModelAdmin):
    pass
admin.site.register(Item, AsusManagement)

class ReceiverManagement(admin.ModelAdmin):
    pass
admin.site.register(Receiver, AsusManagement)

class DeliveryManagement(admin.ModelAdmin):
    pass
admin.site.register(Delivery, AsusManagement)

class CollectionManagement(admin.ModelAdmin):
    pass
admin.site.register(CollectPoint, AsusManagement)

class DropManagement(admin.ModelAdmin):
    pass
admin.site.register(Drop, AsusManagement)
