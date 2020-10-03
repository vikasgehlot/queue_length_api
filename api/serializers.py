from rest_framework import serializers
from .models import Queue,Logdata_put,Store


class QueueSerializer(serializers.ModelSerializer):
	queue_length=serializers.IntegerField()
	class Meta:
		model=Queue
		fields=['queue_length']
	
	
class Logdata_putSerializer(serializers.ModelSerializer):
	class Meta:
		model=Logdata_put
		fields='__all__'

class StoreSerializer(serializers.ModelSerializer):
	class Meta:
		model=Store
		fields='__all__'



