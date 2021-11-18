from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', views.Landing_Page, name='Landing Page'),
   path('Booking', views.Booking_Page, name='Booking'),
   path('Landing_test', views.Landing_Test, name='Landing_test'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
