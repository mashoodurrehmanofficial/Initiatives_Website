
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [   
    path('signup/', signup_page, name='signup'),
    path('login/', login_page, name='login_page'),      
    path('logout/', logout_page, name='logout_page'), 


    path('send_reset_url/', send_reset_url, name='send_reset_url'), 
    path('message_page/', message_page, name='message_page'), 
    path('reset_password/<str:reset_code>', reset_password, name='reset_password'), 
       
    path('fetch_cities/', fetch_cities, name='fetch_cities'),    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

