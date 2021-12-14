from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.Homepage, name='Homepage'),
   path('Menu', views.Menu_Page, name='Menu'),
   path('Booking', views.Booking_Page, name='Booking'),
   path('anythinganywhere', views.AnythingAnywhere, name='AnythingAnywhere'),
   path('exclusivedeal49', views.ExclusiveDeal49, name='ExclusiveDeal49'),
   path('t&c', views.TC, name='t&c'),
   path('t&c1', views.TC1, name='t&c1'),  #anythinganywhere policy
   path('pp', views.PP, name='pp'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
