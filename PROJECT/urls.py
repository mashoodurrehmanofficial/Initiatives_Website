
from django.contrib import admin
from django.urls import path,include  
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', include('dashboards.urls')),  
    path('account/', include('accounts.urls')),  
    path('dashboard/', include('dashboards.urls')),  
    path('api/', include('API.urls')),  
    path('admin_panel/', include('Admin_Panel.urls')),  
    
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import (
handler400, handler403, handler404, handler500
)

handler404 = 'root.views.handler404'
handler500 = 'root.views.handler500'