import cv2
import numpy as np
import time
video = cv2.VideoCapture('testing.mp4')
video.set(cv2.CAP_PROP_POS_FRAMES,14428)
print(video)
ret, frame = video.read()
cv2.imshow('teste', np.array(frame, dtype = np.uint8 ) )
cv2.waitKey()