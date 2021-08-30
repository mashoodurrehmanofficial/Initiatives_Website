
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [   
    path('', user_profile, name='user_profile'),  
    path('user_profile/', user_profile, name='user_profile'),  
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 