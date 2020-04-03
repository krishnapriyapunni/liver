from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class UserProfile(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,)
	email=models.EmailField()
	password=models.CharField(max_length=30)
	mobile=models.CharField(max_length=10)
    # appoinment=models.


	def __str__(self):
		return str(self.user.username)

class Regional(models.Model):
	# user=models.ForeignKey(User,on_delete=models.CASCADE,)
	name=models.CharField(default=0, max_length=35)
	email=models.EmailField()
	password=models.CharField(max_length=30)
	mobile=models.CharField(max_length=10)
    # appoinment=models.


	def __str__(self):
		return str(self.name)





class Clinicalmanager(models.Model):
	# user=models.OneToOneField('auth.User',on_delete=models.CASCADE,)
	nameofdepartment=models.CharField(max_length=30)
	partgrp=models.CharField(max_length=30)
	descrptn=models.CharField(max_length=30)
	dte=models.CharField(max_length=30)
	nameofclinicalengr=models.CharField(max_length=30)
	nameofhospital=models.CharField(max_length=30)
	ceid=models.CharField(max_length=30)
	ponumber=models.CharField(max_length=30)
	prnumber=models.CharField(max_length=30)
	status=models.CharField(max_length=30,default="new")
	# approval=models.BooleanField(default=False)

	def __str__(self):
		return str(self.nameofdepartment)


class Requestforregionalmanager(models.Model):	
	feedback=models.TextField()
	details=models.TextField()

	def __str__(self):
		return self.feedback

class SourcingTeam(models.Model):	
	feedback=models.TextField()
	details=models.TextField()

	def __str__(self):
		return self.feedback

# class Areamanager(models.Model):
# 	nameofdepartment=models.CharField(max_length=30)
# 	partgrp=models.CharField(max_length=30)
# 	descrptn=models.CharField(max_length=30)
# 	dte=models.CharField(max_length=30)
# 	nameofclinicalengr=models.CharField(max_length=30)
# 	nameofhospital=models.CharField(max_length=30)
# 	ceid=models.CharField(max_length=30)
# 	ponumber=models.CharField(max_length=30)
# 	prnumber=models.CharField(max_length=30)
# 	status=models.CharField(max_length=30)
# 	approval=models.BooleanField(default=False)

# 	def __str__(self):
# 		return str(self.nameofdepartment)
# 	 
class Document(models.Model):
   
    document = models.FileField(upload_to='documents/')
    