# Importing all necessary libraries
import cv2
import os
import numpy
import random as rs
import math
# Read the video from specified path

class video:
    #Creates a random array
    def __init__(self,video_name,storage_dir):
        self.video_name = video_name
        self.storage_dir = storage_dir
    def randomize(self,size,mini):
        rand = []
        while (size):
            maxi = self.num_frames
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
        payload = {'num_frames':num_frames}
        self.num_frames = payload['num_frames']
        print("Number of frames: ",self.num_frames)
        return(payload)
    def video_capture(self):
        response = []
        names  = []
        if (self.rand):
            r = self.rand
        else:
            print("Please Create a random array")
        for x in r:
            cam = cv2.VideoCapture(self.video_name)
            num_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
            print("\n Random: ",r)
            x = math.ceil(x)
            cam.set(cv2.CAP_PROP_POS_FRAMES, x)
            name = './'+str(self.storage_dir)+'/frame' + str(x) + '.jpg'
            ret, frame = cam.read()
            names.append(name)
            print("\n\n Writing frame ",x)
            response.append(frame)
            cv2.imwrite(name, frame)
            cam.release()
            cv2.destroyAllWindows()
            resp = {'frames':response,'local':names}
        return(resp)