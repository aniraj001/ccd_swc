from django.db import models
from django.urls import reverse

class Company(models.Model):
	name = models.CharField(max_length=250)
	industry = models.CharField(max_length=250)
	poc = models.CharField(max_length=250)
	# logo = models.ImageField(upload_to='company_logo',blank=True)

	def get_absolute_url(self):
		return reverse('room:detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.name

class Hostel(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='hostel_maps',blank=True)

	def __str__(self):
		return self.name

class Room(models.Model):
	company = models.ForeignKey(Company,related_name="rooms",on_delete=models.CASCADE)
	hostel = models.ForeignKey(Hostel,on_delete=models.CASCADE)
	room_no = models.CharField(max_length=100)
	def company_fill(self,Company):
		self.company = Company.pk
	def save(self,*args, **kw):
		super(Room,self).save(*args, **kw)
	def __str__(self):
		return self.room_no
