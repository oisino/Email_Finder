from django.db import models

# Create your models here.
class Company(models.Model):
	url = models.URLField(max_length=200)
	
	def __unicode__(self):
		return self.url
		
class Name(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.firstname, self.lastname