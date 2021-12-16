import requests
import json
import os
from PIL import Image
import PIL
import math
from anilistpy import Anime
class anime():

	def search(self,file,name="Default",tipo="write"):
		files = {'image': open(str(file),'rb')}
		r = requests.post('https://api.trace.moe/search', files = files)
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
		finalOutput = []
		for x in resp:
			responseData = json.loads(x)
			for y in responseData['result']:
				finalOutput.append(y['anilist'])
		anime = sorted(list(set(finalOutput)))[-1]
		animeData = Anime(anime).json()
		print("Title ", animeData['data']['Page']['media'][0]['title']['romaji'])
		print("AniList code: ",anime)
		print("Full Data: ",finalOutput)

	#Remove all temp files
	def del_temp(self,local):
		for x in local:
			print("Deleting: ",x)
			os.remove(x)
#https://trace.moe/api/search -d "image=$(base64 -w 0 your_search_image.jpg)"
# Importing all necessary libraries