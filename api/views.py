from django.shortcuts import render
from django.http import HttpResponse
from .models import Queue,Logdata_put,Logdata_get,Store
from .serializers import QueueSerializer,Logdata_putSerializer,StoreSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views import View
import datetime
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist

@api_view(['PUT','GET'])
def queue_length(request,id=None):
	if request.method=='PUT':
		threshold=Store.objects.get(pk=id).threshold
		lessfive=datetime.datetime.now()-datetime.timedelta(minutes=5)
		max_len=Logdata_put.objects.filter(date_time_put__gt=lessfive,store_id=id).aggregate(Max('queue_length'))['queue_length__max']
		if int(request.data['queue_length'])>0 and (max_len is None or  (int(request.data['queue_length'])+threshold > max_len )):
			log_put=Logdata_put(queue_length=request.data['queue_length'],store_id=id)
			log_put.save();
			queue=Queue.objects.filter(store_id=id).get()
			serializer=QueueSerializer(instance=queue,data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		return Response({"error":"Invalid Input queue_length can not decrese by{} in 5 minutes and can not be negative".format(threshold)})
	else:
		log_get=Logdata_get(store_id=id)
		log_get.save()
		try:
			queue=Queue.objects.filter(store_id=id).get()
			print(queue)
			serializer=QueueSerializer(queue,many=False)
			return Response(serializer.data)
		except ObjectDoesNotExist:
			return Response({"errors":"Invalid Store id"})
		except:
			return Response({"errors":"Something went wrong"})



@api_view(['GET'])
def all_updates(request):
	allupdates=Logdata_put.objects.all()
	serializer=Logdata_putSerializer(allupdates,many=True)
	return Response(serializer.data)
	


@api_view(['GET','POST'])
def store(request):
	if request.method=='POST':
		serializer=StoreSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			obj=Store.objects.last()
			queue=Queue(store_id=obj.id)
			queue.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	else:
		store=Store.objects.all()
		serializer=StoreSerializer(store,many=True)
		return Response(serializer.data)


 