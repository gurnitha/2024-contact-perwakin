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


class Category (models.Model):
	name = models.CharField(max_length=30)
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Categorires"

	def __str__(self):
		return self.name


class Perwakin (models.Model):
	name = models.CharField(max_length=30)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)  
	city = models.ForeignKey(City, on_delete=models.CASCADE)  
	country = models.ForeignKey(Country, on_delete=models.CASCADE)  
	region = models.ForeignKey(Region, on_delete=models.CASCADE) 	
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Perwakins"

	def __str__(self):
		return self.name


class Bidang (models.Model):
	name = models.CharField(max_length=30)
	perwakin = models.ForeignKey(Perwakin, on_delete=models.CASCADE)	
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Bidangs"

	def __str__(self):
		return self.name


class Group (models.Model):
	name = models.CharField(max_length=30)
	bidang = models.ForeignKey(Bidang, on_delete=models.CASCADE)	
	perwakin = models.ForeignKey(Perwakin, on_delete=models.CASCADE)	
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Groups"

	def __str__(self):
		return self.name


class Gender (models.Model):
	name = models.CharField(max_length=30)	
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Genders"

	def __str__(self):
		return self.name


class Hobby (models.Model):
	name = models.CharField(max_length=30)	
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Hobbies"

	def __str__(self):
		return self.name


class Profession (models.Model):
	name = models.CharField(max_length=30)	
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Professions"

	def __str__(self):
		return self.name


class Interest (models.Model):
	name = models.CharField(max_length=30)	
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Interests"

	def __str__(self):
		return self.name


class IsImportant (models.Model):
	name = models.CharField(max_length=30)	
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Is importants"

	def __str__(self):
		return self.name


class Salutation (models.Model):
	name = models.CharField(max_length=30)	
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Salutations"

	def __str__(self):
		return self.name


class Contact (models.Model):
	name = models.CharField(max_length=30)	
	salutation = models.ForeignKey(Salutation, on_delete=models.CASCADE)	
	gender = models.ForeignKey(Gender, on_delete=models.CASCADE)	
	hobby = models.ManyToManyField(Hobby)	
	profession = models.ManyToManyField(Profession)	
	interest = models.ManyToManyField(Interest)	
	group = models.ManyToManyField(Group)	
	bidang = models.ForeignKey(Bidang, on_delete=models.CASCADE)	
	perwakin = models.ForeignKey(Perwakin, on_delete=models.CASCADE)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)  
	region = models.ForeignKey(Region, on_delete=models.CASCADE) 
	is_important = models.ForeignKey(IsImportant, on_delete=models.CASCADE) 
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Contacts"

	def __str__(self):
		return self.name
