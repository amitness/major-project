import os
import cv2

def extractImages(pathIn, pathOut):
  os.makedirs('/home/kamal/Desktop/major-project/frames', exist_ok=True) # Replace Path with your desired Path.
  vidcap = cv2.VideoCapture(pathIn)
  success,image = vidcap.read()
  count = 0
  success = True
  while success:
    success,image = vidcap.read()
    print ('Read a new frame: ', success) #check whether the video is segmented for each frame.
    cv2.imwrite( pathOut + "frame%d.png" % count, image)
    count += 1

extractImages('to_segment.mp4', '/home/kamal/Desktop/major-project/frames/') # Choose your PathOut yourself.
