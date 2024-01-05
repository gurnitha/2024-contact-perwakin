from django.contrib import admin


from .models import (
	Region, Country, City, Category, Perwakin, 
	Bidang, Group, Gender, Hobby, Profession, 
	Contact, IsImportant, Interest, Salutation)

# Register your models here.

admin.site.register(Region)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Perwakin)
admin.site.register(Bidang)
admin.site.register(Group)
admin.site.register(Gender)
admin.site.register(Hobby)
admin.site.register(Profession)
admin.site.register(IsImportant)
admin.site.register(Interest)
admin.site.register(Salutation)
admin.site.register(Contact)