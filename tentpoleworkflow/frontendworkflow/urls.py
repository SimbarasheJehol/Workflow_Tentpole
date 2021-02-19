from django.contrib import admin  
from django.urls import path  
from frontendworkflow import views 


urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', views.index),  
    path('renderplot',views.plotview)
] 