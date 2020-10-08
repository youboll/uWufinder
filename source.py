import requests
import json
import os
from PIL import Image
import PIL
import math
class anime():

	def search(self,file,name="Default",tipo="write"):
		files = {'image': open(str(file),'rb')}
		r = requests.post('https://trace.moe/api/search', files = files)
		j = json.dumps(r.json())
		string = str(name) + '.json'
		if (tipo =="write"):
			exit = open(string,'w')
			exit.write(str(j))
		self.response = j
		return(j)

		#print(type(alpha))
		#print("Nome: ",alpha["title_romaji"]," Semelhanca",alpha["similarity"])
	def composer(self,resp):
		anime_exit = {'title':[],'ep':[],'mal_id':[],'is_adult':[],
		'similarity':[]}
		cont = 0
		#Try to extrack title from json responses
		for x in resp:			
			array = json.loads(x)
			docs = array["docs"]
			c = math.ceil(len(docs) * 0.35)
			while (c != 0):
				alpha = docs[(c - 1)]
				title = alpha['title_romaji']
				episode = alpha['episode']
				anime_exit['title'].append(title)
				anime_exit['ep'].append(episode)
				anime_exit['mal_id'].append(alpha['mal_id'])
				anime_exit['is_adult'].append(alpha['is_adult'])
				anime_exit['similarity'].append(alpha['similarity'])

				cont = cont + 1
				c = c-1
		sum_si = 0
		for x in anime_exit['similarity']:
			sum_si = sum_si + x
		sum_si = sum_si / len(anime_exit['similarity'])
		anime_exit['similarity'] = [sum_si]
		#Where all the info returns

		final = {}
		#Select info from json files
		for x in anime_exit:
			delta = anime_exit[x]
			p = set([x for x in delta if delta.count(x) > (cont *0.35)])

			#Exceptions
			if (x == "ep"):
				p = set([x for x in delta if delta.count(x) > (cont *0.15)])
			elif (x == "similarity"):
				sum_si = 0
				for y in delta:
					sum_si = sum_si + y
				sum_si = sum_si / len(anime_exit['similarity'])
				p = [sum_si]
			p = list(p)
			final[str(x)] = p 
			
			if (p):
				print("Probably ",str(x)," ",p)
			else:
				print("Not Found. All possible animes: ",delta)
		return(final)
	#Remove all temp files
	def del_temp(self,local):
		for x in local:
			print("Deleting: ",x)
			os.remove(x)
#https://trace.moe/api/search -d "image=$(base64 -w 0 your_search_image.jpg)"
# Importing all necessary libraries



# Read the video from specified path
ani = anime()
ani.search('anime.jpg')