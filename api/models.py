from django.db import models

class Store(models.Model):
	name=models.CharField(max_length=20)
	add=models.CharField(max_length=200,blank=True,null=True)
	threshold=models.IntegerField()
	

class Queue(models.Model):
	queue_length=models.IntegerField(null=True)
	store=models.OneToOneField(Store,on_delete=models.CASCADE,null=True)

class Logdata_get(models.Model):
	date_time_get=models.DateTimeField(auto_now_add=True)
	store=models.ForeignKey(Store,on_delete=models.CASCADE,null=True)

class Logdata_put(models.Model):
	date_time_put=models.DateTimeField(auto_now_add=True)
	queue_length=models.IntegerField()
	store=models.ForeignKey(Store,on_delete=models.CASCADE,null=True)


