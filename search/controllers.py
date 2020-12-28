from search.user import user

def login_controller(request):
		from search.tests import test 
		from search.user import user
		import hashlib 
		if request.method == 'POST':
			username = request.POST.get('username','')
			password = request.POST.get('password','')
			payload = {'username': username,'pwd1': password}

			u = user.login(payload)
			print(u)
			if u[0] == True:
				print("logado")
				request.session["user_auth"] = u[1].ident

				return([True])
			else:
				pl = {'error:':True,'cod':u[1]}
				return(u)
		