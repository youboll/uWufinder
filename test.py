from source import anime
from alias import video
from PIL import Image as im 
def extractor(file,folder,size):
	vd = video(file,folder)
	vd.storage()
	info = vd.get_info()
	vd.randomize(size,0)
	res = vd.video_capture()

	return(res)
uzaki = extractor('testing.mp4','temp',3)
names = uzaki['local']
frames = uzaki['frames']
cont = 0
final = []
for x in names:
	ani = anime()
	exit = 'uzaki' + str(cont)
	#Put a name different from "write"
	pls = ani.search(x,exit,"write")
	cont = cont + 1
	final.append(pls)
fosasi = ani.composer(final)
print(fosasi)
ani.del_temp(names)