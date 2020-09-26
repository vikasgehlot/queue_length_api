
from django.urls import path
from . import views

urlpatterns = [
   
    path('queue_length/',views.queue_length,name='queue_length'),
    path('queue_length_update/',views.queue_length_update,name='queue_length_update'),
    path('all_updates/',views.all_updates,name='all_updates'),
]
