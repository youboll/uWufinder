import requests
import json
import os
from PIL import Image
import PIL
import math
import cv2
import numpy
import random as rs
from mal import Anime
class anime():
    def search(self,file,name="Default",tipo="write"):
        files = {'image': open(str(file),'rb')}
        r = requests.post('https://trace.moe/api/search', files = files)
        j = json.dumps(r.json())
        string = str(name) + '.json'
        if (tipo =="write"):
            exit = open(string,'w')
            exit.write(str(j))
        self.res = j
        return(j)

        #print(type(alpha))
        #print("Nome: ",alpha["title_romaji"]," Semelhanca",alpha["similarity"])
    def composer(self,resp):
        anime_exit = {'title':[],'ep':[],'mal_id':[],'is_adult':[],
        'similarity':[]}
        cont = 0
        #Try to extrack title from json files
        for x in resp:          
            array = json.loads(x)
            docs = array["docs"]
            c = math.ceil(len(docs) * 0.35)
            while (c != 0):
                alpha = docs[(c - 1)]
                similarity = alpha['similarity']
                anime_exit['title'].append((alpha['title_romaji'],similarity))
                anime_exit['ep'].append((alpha['episode'],similarity))
                anime_exit['mal_id'].append((alpha['mal_id'],similarity))
                anime_exit['is_adult'].append((alpha['is_adult'],similarity))
                anime_exit['similarity'].append((alpha['similarity'],similarity))

                cont = cont + 1
                c = c-1
        sum_si = 0
        final = {}
        print(anime_exit)
        for x in anime_exit:
            a = anime_exit[x]
            result = 0
            for y in a:
                avg = anime.finder(y[0],a)
                if a.count(y) != 0:
                    if (avg[1] > result):
                        result = float(avg[1])
                        payload = {str(x):avg[0]}
                        final[str(x)] = avg[0]
                        print(final)
        print(final)
        return(final)
        #Select info from json files
    def finder(number,array):
        final = []
        cont = 0
        z = 0
        for b in array:
            y = int(b.count(number))
            

            if (y != 0):
            #Append similarity on the code
                z = z + b[1]
                cont += 1
        if (cont != 0):
            if (cont > math.ceil(len(array) * 0.40)):
                z = math.floor(z * 1.0550)
                print("ADDED five PERCENT ") 
            avarage = z / cont
            return([number,avarage])

        
    


# Read the video from specified path

class video:
    #Creates a random array
    def __init__(self,video_name,storage_dir):
        self.video_name = video_name
        self.storage_dir = storage_dir
    def try_video(self):
        #Check if payload is a video
        try:
            video = cv2.VideoCapture(self.video_name)
            video.release()
            cv2.destroyAllWindows()
            return(True)
        except:
            return(False)
    def randomize(self,size,mini):
        rand = []
        while (size):
            maxi = math.floor(self.num_frames * 0.80)
            key = rs.randint(mini,maxi)
            rand.append(key)
            size = size -1
            if (size == 0):
                self.rand = rand
                break
        return(self.rand)
    #Open storage
    def storage(self):
        try:

        # creating a folder named data
            if not os.path.exists(self.storage_dir):
                os.makedirs(self.storage_dir)
                return(self.storage)
        # if not created then raise error
        except OSError:
            print('Error: Creating directory of video')

#extract info
    def get_info(self):
        video = cv2.VideoCapture(self.video_name)
        num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_rate = cv2.CAP_PROP_FPS
        video.release()
        self.num_frames = num_frames
        print("Number of frames: ",self.num_frames)
        return(self.num_frames)
    def video_capture(self):
        respo = []
        names  = []
        if (self.rand):
            r = self.rand
            print("\n Random: ",r)
        else:
            print("Please Create a random array")
        for x in r:
            cam = cv2.VideoCapture(self.video_name)
            num_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
            x = math.ceil(x)
            cam.set(cv2.CAP_PROP_POS_FRAMES, x)
            name = str(self.storage_dir)+'frame' + str(x) + '.jpg'
            ret, frame = cam.read()
            names.append(name)
            print("\n\n Writing frame ",x)
            respo.append(frame)
            cv2.imwrite(name, frame)
            cam.release()
            cv2.destroyAllWindows()
        resp = {'frames':respo,'local':names}
        print("Frames local",resp['local'])
        return(resp)
    #Just use this funciton for byte type
    def save_video(self,name,byte):
        #Join final dir with filename
        storage = self.storage_dir + str(name)
        #Convert to byte
        try:
            byte  = bytes(byte)
        except Exception:
            print("Non byte-type obj")
            return(False)
        with open(storage,'wb') as video:
            video.write(byte)
            video.close()
            return(storage)
    #Remove all temp files
    def del_temp(self,local):
        try:
            for x in local:
                print("Deleting: ",x)
                os.remove(x)
            return(True)
        except Exception:
            return(False,Exception)

    #This isn't a view
    def extractor(name,file,folder):
        #Recive the anime video and stores it in the local machine
        vd = video(name,folder)
        if vd.try_video() == False: return(False)

        vd.storage()
        info = vd.save_video(name,file)
        print(info)
        
        #Del temp media
        return(info)
    #Neither this one
    def video_ani(file,folder,size):
        ani = video(file,folder)
        ani.storage()
        info = ani.get_info()
        ani.randomize(size,int(info * 0.30))
        res = ani.video_capture()
        final = []
        cont = 0
        for x in res['local']:
            comp = anime()
            exit = 'uzaki' + str(cont)
            #Put a name different from "write"
<<<<<<< HEAD
            pls = comp.search(x,exit,"tralala")
=======
            pls = comp.search(x,exit,"bla")
>>>>>>> dea5dc89a68445bff739d48a7eb771a0ba4567e6
            cont = cont + 1
            final.append(pls)

        result = comp.composer(final)
        ani.del_temp([file])
        ani.del_temp(res['local'])

        return(result)




class mal_search:
    def __init__(self,ani_cod):
        self.ani_cod = ani_cod
    def search(self):
        ani = Anime(self.ani_cod)
        return(ani)






    """
        Anime(mal_id)

Anime.mal_id
Anime.title
Anime.title_english
Anime.title_japanese
Anime.title_synonyms
Anime.url
Anime.image_url
Anime.type
Anime.episodes
Anime.status
Anime.aired
Anime.premiered
Anime.broadcast
Anime.producers
Anime.licensors
Anime.studios
Anime.source
Anime.genres
Anime.duration
Anime.rating
Anime.score
Anime.scored_by
Anime.rank
Anime.popularity
Anime.members
Anime.favorites
Anime.synopsis
Anime.background
Anime.related_anime
Anime.opening_themes
Anime.ending_themes
            
        """


