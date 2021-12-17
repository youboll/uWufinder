from source import anime
from video import video
from PIL import Image as im 
import argparse

parser = argparse.ArgumentParser(description='Find anime from video')
parser.add_argument('--video', dest='video', help='Video containing the anime')
args = parser.parse_args()

def extractor(file,folder,size):
	vd = video(file,folder)
	vd.storage()
	info = vd.get_info()
	vd.randomize(size,0)
	res = vd.video_capture()

	return(res)
uzaki = extractor(args.video,'temp',3)
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
ani.composer(final)

ani.del_temp(names)