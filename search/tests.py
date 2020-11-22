import re
from search.models import user
class test:
	def signup(payload):
		
		for x in payload:
			if (len(payload[x]) == 0):
				return([False,'Error: Fields empty'])
			if (len(payload[x]) ==50):
				return([False,'Unkwon error'])

		#Check if email is valid
		regex = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
		if not (re.search(regex,payload['email'])):
			return([False,'Please type a valid E-mail'])

		if (payload['pwd1'] != payload['pwd2']):
			return([False,'Passwords doesn\'t match'])

		if (len(payload['pwd1']) > 18):
			return([False,'Passwords too long'])

		if (len(payload['pwd1']) < 8):
			return([False,'Passwords too short'])

		try:
			if user.objects.get(email=str(payload['email'])):
			 	return([False,'Email already used'])
		except:
			pass

		try:
			if user.objects.get(username=str(payload['username'])):
			 	return([False,'Username already used'])
		except:
			pass
		return([True])
				
	def signin(payload):
		for x in payload:
			if (len(payload[x]) == 0):
				return([False,'Error: Fields empty'])
			if (len(payload[x]) >50):
				return([False,'Unkwon error'])


		if (len(payload['pwd1']) > 18):
			return([False,'Passwords too long'])

		if (len(payload['pwd1']) < 8):
			return([False,'Passwords too short'])
		return([True])