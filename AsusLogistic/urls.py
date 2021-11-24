from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', views.Landing_Page, name='Landing Page'),
   path('Login', views.Login, name='Login'),
   path('Menu', views.Menu_Page, name='Menu'),
   path('Booking', views.Booking_Page, name='Booking'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
