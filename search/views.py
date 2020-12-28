from django.shortcuts import render,redirect
from search.source import *
# Create your views here.
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def search(request):
	from search.user import user

	if (request.method == "POST"):

		if (user.check_login(request) == False):
			return(redirect(signin))
		files = request.FILES['ani_file']
		if (files):
			print(files.name)
			ex = video.extractor(files.name,files.read(),'./search/temp/')
			print(ex)
			ani_response = video.video_ani(ex,'./search/temp/',2)
			#Pases all lists into a dict
			
			resp = {}
			if (ani_response):
				for x in ani_response:
					try:
						if x == 'title':
							fefef
						array = {str(x):ani_response[x][0]}
						resp.update(array)
					except:
						array = {str(x):ani_response[x]}
						resp.update(array)
			if (resp['mal_id']):
				mal = mal_search(resp['mal_id'])
				mal_query = mal.search()
				resp['anime_mal'] = mal_query
			return(render(request,'search.html',resp))
	else:
		return(render(request,'search.html',{}))



@csrf_exempt
def index(request):
	from search.user import user
	#Tests if user isn't logged
	if (user.check_login(request) == False):return(render(request,'index.html'))
	
	#If not not logged . then it's logged
	x = user.get_info(request.session['user_auth'],'all')
	#Parsing arguments into the template
	payload = {'user':True,'username':x['username'],'email':x['email'],
	'first_name':x['first_name'],'last_name':x['last_name']}

	return(render(request,'index.html',payload))

	





def signup(request):
	from search.user import user
	
	payload = {}
	#Fields to catch
	fields  = ['username','email','first_name','last_name','pwd1','pwd2']
	if request.method == 'POST':

		for x in request.POST:
			if fields.count(str(x)) != 0:
				payload[str(x)] = request.POST.get(str(x),'')
		tr = user.signup(payload)
		if (tr[0] == False):
			return(render(request,'signup.html',{'error': True,'cod':tr[1]}))
		

		print(payload)
	return(render(request,'signup.html'))


def signin(request):
<<<<<<< HEAD
	import search.controllers as controllers
	#Get destination param
	dest = request.GET.get('param','')
	#Getting user info
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	if (len(username) == 0 or len(password) == 0 ):
		return(render(request,'signin.html',{}))
	if (len(dest) != 0):
		x = controllers.login_controller(request)
		if (x[0] == True):
			#Index is the only exception to the pattern
			if (dest == 'index'): dest = ''
			site = '/' + str(dest)
			return(redirect(site))
		else:
			print(x)
	else:
		print(x)
		return(redirect(index))

def user_controller(request):
	from search.user import user as us
	y= None
	x = us.user_controller(request,'y')
	if (x['exit_site'] == "index"):
		redir ='/'
	else:
		redir ='/' + x['exit_site']
	return(redirect(redir))

def control_panel(request):
	from search.user import user
	#Check some stuff
	if (user.check_login(request) == False):
		return(redirect(index))
	if (user.check_trial(request.session['user_auth']) == True):
		return(redirect(index))
		
	payload = user.get_info(request.session['user_auth'],param = 0)
	return(render(request,'control_panel.html',payload))
=======
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

			return(redirect(index))
		else:
			pl = {'error:':True,'cod':u[1]}
			return(render(request,'signin.html',payload))

	return(render(request,'signin.html',{}))

def user_controller(request):
	from search.user import check_option
	y = 0
	x = check_option.user_controller(request,y)
	return(redirect(x['exit_site']))
>>>>>>> dea5dc89a68445bff739d48a7eb771a0ba4567e6
