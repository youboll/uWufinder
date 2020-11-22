from django.db import models

class user(models.Model):
	username = models.CharField(max_length=15,default=None,null=False,unique=True)
	email = models.CharField(max_length= 40,default=None,null=False,unique=True)
	first_name = models.CharField(max_length=15,default=None,null=False)
	last_name = models.CharField(max_length=25,default=None,null=False)
	password = models.TextField(null=False,default=None)
	ident = models.AutoField(primary_key=True)
	type_acc = models.IntegerField(default= 0)
	signup_date = models.DateField(default = None,null=False)
	ex_date = models.DateField(null=True)
	valid = models.BooleanField(default = True,null = False)