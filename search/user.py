from search.models import user as us
class user:
	def __init__(ident):
		self.ident = ident


	def show_user(self):
		try:
			tr = us.objects.get(ident = self.ident)
			print("Valid login!!! username:",tr.username,' Email: ',tr.email)
			return(tr)
		except:
			print("Not found")
			return(False)


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
				#DB query
				us = user(username=str(payload['username']),email=str(payload['email']),
					first_name=str(payload['first_name']),last_name=str(payload['last_name']),
					password=str(payload['pwd1']),signup_date = time,ex_date = ex)
				us.save()
				return([True])				
			except ValueError as ex:
				return([False,'Erro Desconhecido'])


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
		try:
			request.session['user_auth']
			return(True)
		except:
			return(False)
	def logout(request):
		if check_login(request) == False: return(False)
		try:
			del request.session['user_auth']
			return(True)
		except:
			return(False)


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
