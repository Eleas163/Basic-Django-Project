from django.conf.urls import url  
from django.contrib import admin  
from student import views  
urlpatterns = [  
        url('admin/', admin.site.urls),  
        url(r'^$', views.movies_list, name='movies_list'),
        url(r'^new$', views.movies_create, name='movies_new'),  
        url(r'^edit/(?P<pk>\d+)$', views.movies_update, name='movies_edit'),  
        url(r'^delete/(?P<pk>\d+)$', views.movies_delete, name='movies_delete'),    
]  
