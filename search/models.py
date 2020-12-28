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
<<<<<<< HEAD
	valid = models.BooleanField(default = True,null = False)
	valid_email = models.BooleanField(default = False, null = False)
	bio = models.TextField(default=str("Descrição do usuario"))

class user_auth(models.Model):
	token = models.TextField(null = False)
	user_id = models.IntegerField(null = False)
	token_ex = models.DateField(null = False)
=======
	valid = models.BooleanField(default = True,null = False)
>>>>>>> dea5dc89a68445bff739d48a7eb771a0ba4567e6
