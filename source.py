import requests
import json
class anime:

	def search(self,file):
		files = {'image': open('anime.jpg','rb')}
		r = requests.post('https://trace.moe/api/search', files = files)
		j = json.dumps(r.json())
		exit = open('exit.json','w')
		exit.write(str(j))
		self.response = j
		return(j)
	def break_video(file):
		pass	
	def list(self):
		response = self.response
		response = json.loads(response)
		res = response["docs"]
		self.alpha = res[0]
		self.beta = res[1]
		self.teta = res[2]
		self.gama = res[3]
		#print(type(alpha))
		#print("Nome: ",alpha["title_romaji"]," Semelhanca",alpha["similarity"])
	def finder(self):
		if (self.alpha < 0.8):
			print("Anime Nao encontrado")
		else:
			print("Nome: ",self.alpha["title_romaji"]," Semelhanca",self.alpha["similarity"])
bc = anime()
request = bc.search('anime.jpg')
bc.list()
bc.finder()

#https://trace.moe/api/search -d "image=$(base64 -w 0 your_search_image.jpg)"