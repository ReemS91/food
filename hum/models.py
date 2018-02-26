from django.db import models

# Create your models here.
class Hum(models.Model):
	name = models.CharField(max_length=100)
	caloreies = models.CharField(max_length=250)
	exp_date = models.DateField()
	processed = models.BooleanField()
	healthy = models.BooleanField() 

	def __str__(self):
		return self.name