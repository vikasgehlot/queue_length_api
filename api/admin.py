from django.contrib import admin
from .models import Queue,Logdata_put,Logdata_get,Store
# Register your models here.

admin.site.register(Queue)
admin.site.register(Logdata_get)
admin.site.register(Logdata_put)
admin.site.register(Store)