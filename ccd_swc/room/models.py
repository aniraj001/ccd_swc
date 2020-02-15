from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Company(models.Model):
	name = models.CharField(max_length=250)
	industry = models.CharField(max_length=250)
	poc = models.CharField(max_length=250)

	def get_absolute_url(self):
		return reverse('room:detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.name

	def get_photo_url(self):
		if self.logo and hasattr(self.logo, 'url'):
			print("YES")
			return self.logo.url
		else:
			print("NO")
			return "media/company_logo/user.jpg"

class Hostel(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Room(models.Model):
	company = models.ForeignKey(Company,related_name="rooms",on_delete=models.CASCADE)
	hostel = models.ForeignKey(Hostel,on_delete=models.CASCADE)
	room_no = models.CharField(max_length=100,validators=[
        RegexValidator(
			regex='^([A-Z])-([0-9])+$',
            message='room number must be of form: A-9'
        ),
    ])

	class Meta:
		unique_together = ['room_no','hostel']
	def company_fill(self,Company):
		self.company = Company.pk
	def save(self,*args, **kw):
		super(Room,self).save(*args, **kw)
	def __str__(self):
		return self.room_no
