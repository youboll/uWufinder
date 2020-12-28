from search.models import user as us
class user:
	def __init__(ident):
		self.ident = ident


	def show_user(self):
<<<<<<< HEAD
		#Try to show user ----
		#USELESS
=======
>>>>>>> dea5dc89a68445bff739d48a7eb771a0ba4567e6
		try:
			tr = us.objects.get(ident = self.ident)
			print("Valid login!!! username:",tr.username,' Email: ',tr.email)
			return(tr)
		except:
			print("Not found")
			return(False)

<<<<<<< HEAD
	
=======

>>>>>>> dea5dc89a68445bff739d48a7eb771a0ba4567e6
	def login(payload):
		from search.tests import test
		import hashlib
		#making tests
		y= test.signin(payload)
		if y[0] == False:
			return(y)


		#Hasing password from input
		count_hash = 8

		while (count_hash != 0):
				payload['pwd1'] = hashlib.sha512(str(payload['pwd1']).encode('utf-8')).hexdigest()
				count_hash = count_hash - 1
		password = payload['pwd1']



		#Trying login with username
		if (payload['username']):
			try:
				tr = us.objects.get(username = str(payload['username']))
				if tr.valid == False: return([False,'Conta Invalida. Efetue o pagamento para continuar'])
				print('Username certo')
				if (tr.password == password):
					print("Senha certa")
					
					return([True,tr])

			except BaseException as ex:
				raise ex
				return([False,'Crediencias invalidas. Tente novamente'])
		#Trying login with email
		elif (payload['email']):
			try:
				tr = us.objects.get(email = str(payload['email']))
				if (tr.password == password):
					
					return([True])
			except:
				return([False,'Crediencias invalidas. Tente novamente'])


	def signup(payload):
		from search.tests import test
		import hashlib
		from search.models import user
		import datetime

		ts = test.signup(payload)
		if (ts[0] == False):
			return(ts)
		else:
			#Pases password into 4 times sha512 encryption
			count_hash = 8
			while (count_hash != 0):
				payload['pwd1'] = hashlib.sha512(str(payload['pwd1']).encode('utf-8')).hexdigest()
				count_hash = count_hash - 1
			try:
				#Get server time to signup
				d = datetime.datetime.now()
				time = datetime.datetime(d.year,d.month,d.day)
				ex = time + datetime.timedelta(weeks = 5)
<<<<<<< HEAD

=======
>>>>>>> dea5dc89a68445bff739d48a7eb771a0ba4567e6
				#DB query
				us = user(username=str(payload['username']),email=str(payload['email']),
					first_name=str(payload['first_name']),last_name=str(payload['last_name']),
					password=str(payload['pwd1']),signup_date = time,ex_date = ex)
<<<<<<< HEAD
				
				us.save()
				#Getting info by username
				x = user.get_info_username(us.username,'ident')
				print('user_ID',x)
				check_email(x)


=======
				us.save()
>>>>>>> dea5dc89a68445bff739d48a7eb771a0ba4567e6
				return([True])				
			except ValueError as ex:
				return([False,'Erro Desconhecido'])

<<<<<<< HEAD
=======

>>>>>>> dea5dc89a68445bff739d48a7eb771a0ba4567e6
	#Get user info by id
	def get_info(i,param = None):
		from search.models import user as us
		
		if (param != None):
			try:
				tr = us.objects.get(ident = i)
				payload = {'username':tr.username,'email':tr.email,'first_name':tr.first_name,
				'last_name':tr.last_name}
				return(payload)
			except:
				return(False)
		try:

			tr = us.objects.get(ident = i)
			x =  "tr." + param
			return(eval(x))
		except:
			return(False)

<<<<<<< HEAD
	def get_info_username(i,param = None):
		from search.models import user as us
		
		if (param != None):
			try:
				tr = us.objects.get(username = str(i))
				payload = {'username':tr.username,'email':tr.email,'first_name':tr.first_name,
				'last_name':tr.last_name}
				return(payload)
			except:
				return(False)
		try:

			tr = us.objects.get(username = str(i))
			x =  "tr." + param
			return(eval(x))
		except:
			return(False)

=======
>>>>>>> dea5dc89a68445bff739d48a7eb771a0ba4567e6


	def check_trial(i):
		from search.models import user
		import datetime
		today = datetime.datetime.now()
		
		try:
			us = user.objects.get(ident = i)
			user_date = us.ex_date

			#Check if is trial
			if (us.type_acc != 0): return(False)

			#Check date expiration date
			if (user_date.year < today.year):
				us = user.objects.get(ident = i)
				us.valid = False
				us.save()

				print("ALE")
				return(True)

			if (user_date.year == today.year):
				if (user_date.month < today.month):
					us = user.objects.get(ident = i)
					us.valid = False
					us.save()
					print("ALE")
					return(True)
				if (user_date.month == today.month):
					if (user_date.day < today.day):

						us = user.objects.get(ident = i)
						us.valid = False
						us.save()
						print("ALE")
						return(True)
		except BaseException as ex:
			return(False)

	def check_login(request):
<<<<<<< HEAD
		#Check if user is logged
=======
>>>>>>> dea5dc89a68445bff739d48a7eb771a0ba4567e6
		try:
			request.session['user_auth']
			return(True)
		except:
			return(False)
	def logout(request):
<<<<<<< HEAD
		#Logout based on the request
		if user.check_login(request) == False: return(False)
=======
		if check_login(request) == False: return(False)
>>>>>>> dea5dc89a68445bff739d48a7eb771a0ba4567e6
		try:
			del request.session['user_auth']
			return(True)
		except:
			return(False)

<<<<<<< HEAD
	#Is a controller for the user actions
	def user_controller(request,exit = True):
		action = request.GET.get('action','')
		#Param1 is not required

		param1 = request.GET.get('param1','')
		exit_site = request.GET.get('exit','')

		if (len(param1) != 0):
			com ='user.' + str(action) + '(' + str(param1) +  ')'
		else:
			com =' user.' + str(action) + '('+')'

		try:
			c = eval(str(com))
			payload = {'command':c,'exit_site':exit_site}
			return(payload)
		except BaseException as ex:
			raise ex
	#Create token for future activation
	def get_user_auth(id):
		import hashlib
		import random
		from search.models import user_auth
		import datetime
		ex  = datetime.datetime.now() + datetime.timedelta(days = 3)
		#Generates a key form random, Converting a random int into ascii to hash it
		key = hashlib.sha512(str(random.randint(0,100000)).encode('ASCII')).hexdigest()
		#Create a token into the token table
		try:
			qr = us.objects.get(ident = id)
			key_db = user_auth(token = key, user_id = int(qr.ident), token_ex = ex)
			key_db.save()
			return(key_db)
		except BaseException as ex:
			raise ex

	#Unite all the processes to create token and send to email
	def check_email(i):
		from search.email import email
		from search.models import user_auth
		key = user.get_user_auth(i)
		y = user.get_info(i,True)

		try:
			x = email('pedro.ciclobrasil@gmail.com',y['email'],'','')
			x.get_templates('first',{'user':y['first_name'],'token':key.token})
			x.send_email()
		except BaseException as ex:
			raise ex

	def activate_email(token):
		from search.models import user_auth
		try:
			x = user_auth.objects.get(token = token)
			y = user.objects.get(ident = x.user_id)
			y.valid_email = True
			y.save()
		except BaseException as ex:
			raise ex
=======

	"""
	#The login processsesing isn't made here

	#this function only generate a login view from anywhere in the site
	to other point

	#If you want to look login prceo
	"""

class check_option():
	def __init__(self,request):
		self.request = request

	def user_controller(self,exit = True):
		request = self.request
		if (request.method == "POST"):

			action = request.GET.get('action','')
			param1 = request.GET.get('param','')
			exit_site = request.GET.get('exit','')
			if (exit == None):
				com = str(exit) + ' = user.' + str(action) + '(' + str(param1) +  ')'
			elif (len(param1 != 0)):
				com = 'user.' + str(action) + '(' + str(param1) +  ')'
			else:
				com = str(exit) + ' = user.' + str(action) + '('+')'

			try:
				c = eval(payload)
				payload = {'command':c,'exit_site':exit_site}
				return(payload)
			except BaseException as ex:
				raise ex
>>>>>>> dea5dc89a68445bff739d48a7eb771a0ba4567e6
