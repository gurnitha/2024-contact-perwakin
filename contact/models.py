from django.db import models
from django.utils import timezone

# Create your models here.

class Region (models.Model):
	name = models.CharField(max_length=30)
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	def __str__(self):
		return self.name


class Country (models.Model):
	name = models.CharField(max_length=30)
	region = models.ForeignKey(Region, on_delete=models.CASCADE)  
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Coutries"

	def __str__(self):
		return self.name


class City (models.Model):
	name = models.CharField(max_length=30)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)  
	region = models.ForeignKey(Region, on_delete=models.CASCADE)  
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Cities"

	def __str__(self):
		return self.name