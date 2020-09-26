from django.shortcuts import render
from .models import Queue,Logdata_get,Logdata_put
from .serializers import QueueSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def queue_length(request):
	log_get=Logdata_get()
	log_get.save()
	queue=Queue.objects.first()
	serializer=QueueSerializer(queue,many=False)
	print(serializer.data['queue_length'])
	return Response(serializer.data)


@api_view(['PUT'])
def queue_length_update(request):
	log_put=Logdata_put(queue_length=request.data['queue_length'])
	log_put.save();
	queue=Queue.objects.first()
	serializer=QueueSerializer(instance=queue,data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

