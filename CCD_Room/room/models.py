from django.db import models
from django.urls import reverse

# Create your models here.


class Company(models.Model):
	company_name = models.CharField(max_length=250)
	industry = models.CharField(max_length=250)
	sector = models.CharField(max_length=250)
	company_logo = models.FileField()
	
	

	def  get_absolute_url(self):
		return reverse('room:detail', kwargs={'pk': self.pk}) 

	def __str__(self):
		return self.company_name + ' - ' + self.sector 



class Hostel(models.Model):
	hostel_name = models.CharField(max_length=100)

	def __str__(self):
		return self.hostel_name



class Room(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
	room_no = models.CharField(max_length=100)

	def __str__(self):
		return self.hostel + " " + self.room_no
