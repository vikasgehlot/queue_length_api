
from django.urls import path
from . import views



urlpatterns = [
   
    path('queue_length/<int:id>/',views.queue_length,name='queue_length'),
  
    path('all_updates/',views.all_updates,name='all_updates'),
    path('store/',views.store,name='store'),

 
]


