
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [    
    path('', Prepare_Main_page, name='Prepare_Main_page'),  
    path('user_profile/', user_profile, name='user_profile'),  
    path('create_initiative/', create_initiative, name='create_initiative'),  
    path('submit_initiative/', submit_initiative, name='submit_initiative'),  
    path('my_initiatives/', my_initiatives, name='my_initiatives'),  
    path('update_initiative/<str:id>', update_initiative, name='update_initiative'),  
    path('initial_filter/', initial_filter, name='initial_filter'),  
    path('my_initiatives_info/', my_initiatives_info, name='my_initiatives_info'),  
    path('set_badge_to_user/', set_badge_to_user, name='set_badge_to_user'),  
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 