
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [   
    path('', adminpanel, name='adminpanel'),
    path('adminpanel/', adminpanel, name='adminpanel'),
    path('manage_green_areas/', manage_green_areas, name='manage_green_areas'),
    path('manage_green_areas/create_green_area', create_green_area, name='create_green_area'),
    path('manage_green_areas/submit_green_area', submit_green_area, name='submit_green_area'),
    path('manage_green_areas/update_green_area/<str:id>', update_green_area, name='update_green_area'), 

    path('manage_initiatives/', manage_initiatives, name='manage_initiatives'), 
    path('manage_initiatives/mark_green/', mark_green, name='mark_green'), 
    path('manage_initiatives/update_initiative/<str:id>', update_initiative, name='update_initiative'), 


    path('manage_accounts/', manage_accounts, name='manage_accounts'),
    path('manage_accounts/update_profile/<str:id>', update_profile, name='update_profile'), 
    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

