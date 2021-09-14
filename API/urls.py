
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [   
    path('get_cluster/', get_cluster, name='get_cluster'),
    path('Handle_Membership/', Handle_Membership, name='Handle_Membership'),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

