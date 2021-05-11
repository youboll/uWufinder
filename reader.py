##Nada de util aqui
import json
with open('uzaki1.json','r', encoding='utf-8') as j:

    op = json.loads(j.read())

inputs = op['docs'] 
con = 0
ret = {'saida':[]}
for x in inputs:
    print(x['title_romaji'])
    ret['saida'].append(x['title_romaji'])
    con = con + 1
#ret['saida'] = []
anime = set(x for x in ret['saida'] if ret['saida'].count(x) > (con *0.30))
if anime:
	print("oie")
else:
	print("Tcj")
