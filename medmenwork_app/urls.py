from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import home


urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about-us', views.about_us, name='about_us'),
    path('services', views.services, name='services'),
    # path('services/<int:id>/', views.service_details, name='service_details'),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)