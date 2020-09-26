from django.shortcuts import render
from .models import Queue,Logdata_put,Logdata_get
from .serializers import QueueSerializer,Logdata_putSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def queue_length(request):
	log_get=Logdata_get()
	log_get.save()
	queue=Queue.objects.first()
	serializer=QueueSerializer(queue,many=False)
	return Response(serializer.data)


@api_view(['PUT'])
def queue_length_update(request):
	log_put=Logdata_put(queue_length=request.data['queue_length'])
	log_put.save();
	queue=Queue.objects.first()
	serializer=QueueSerializer(instance=queue,data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(status.HTTP_202_ACCEPTED)
	else:
		return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def all_updates(request):
	allupdates=Logdata_put.objects.all()
	serializer=Logdata_putSerializer(allupdates,many=True)
	return Response(serializer.data)
	