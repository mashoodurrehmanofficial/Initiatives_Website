
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [   
    path('signup/', signup_page, name='signup'),
    path('login/', login_page, name='login_page'),      
    path('logout/', logout_page, name='logout_page'), 
       
    path('fetch_states/', fetch_states, name='fetch_states'),    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

