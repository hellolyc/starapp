from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length = 30)
	password = models.CharField(max_length = 30)
	phonenum = models.CharField(max_length = 11,default = "none")
	def __unicode__(self):
		return self.username
class Competition(models.Model):
	name = models.CharField(max_length = 30)
	desc = models.CharField(max_length = 30)
	def __unicode__(self):
		return self.name
class UserCompetion(models.Model):
	user = models.ForeignKey(User)
	competion = models.ForeignKey(Competition)
	tag = models.BooleanField()