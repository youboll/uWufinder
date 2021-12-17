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
	#This algo will cut half the responses based on apperance, the rest will be sorted according to the simililarity
	def composer(self,resp):
		def getElement(item):
			return item['similarity']
		#Entire data
		finalOutput = []
		#Anime codes -- For apperance based sorting
		parcialData=[]
		for x in resp:
			responseData = json.loads(x)
			for y in responseData['result']:
				parcialData.append(y['anilist'])
				finalOutput.append({"anilistID":y['anilist'],"similarity":y['similarity'],"ep":y['episode']})
		
		sortedAnimeList = sorted(list(set(parcialData)))
		cutedAnimeList = sortedAnimeList[(-1 * math.ceil(len(sortedAnimeList)/2)):-1]
		cutedAnimeList.append(sortedAnimeList[-1])
		
		finalAnimeList = []
		for x in cutedAnimeList:
			animeSimilarity = 0.0
			counter = 0
			for y in finalOutput:
				if (y['anilistID'] == x):
					animeObj = y
					break
			for y in finalOutput:
				if (y['anilistID'] == animeObj['anilistID']):
					animeSimilarity =+ y['similarity']
					counter =+ 1
			finalAnimeList.append({"anilistID": animeObj['anilistID'],'similarity':(animeSimilarity / counter)})
		finalAnimeList.sort(key=getElement)
		animeData = Anime(finalAnimeList[-1]['anilistID']).json()
		print("Anilist code: ",finalAnimeList[-1]['anilistID'])
		print("Similarity: ",finalAnimeList[-1]['similarity'])
		print("Anime Title: ",animeData['data']['Page']['media'][0]['title']['romaji'])
		print("Status: ",animeData['data']['Page']['media'][0]['status'])
	#Remove all temp files
	def del_temp(self,local):
		for x in local:
			os.remove(x)
#https://trace.moe/api/search -d "image=$(base64 -w 0 your_search_image.jpg)"
# Importing all necessary libraries