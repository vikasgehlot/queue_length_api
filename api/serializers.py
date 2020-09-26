from rest_framework import serializers
from .models import Queue,Logdata_put


class QueueSerializer(serializers.ModelSerializer):
	class Meta:
		model=Queue
		fields=['queue_length']

class Logdata_putSerializer(serializers.ModelSerializer):
	class Meta:
		model=Logdata_put
		fields='__all__'


