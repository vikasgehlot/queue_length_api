from django.db import models



class Queue(models.Model):
	queue_length=models.IntegerField()

class Logdata_get(models.Model):
	date_time_get=models.DateTimeField(auto_now_add=True)


class Logdata_put(models.Model):
	date_time_put=models.DateTimeField(auto_now_add=True)
	queue_length=models.IntegerField()
