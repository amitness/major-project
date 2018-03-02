import os
import numpy as np
import cv2

#Segment Video into respective frames.
def extractImages(pathIn, pathOut):
  print ("Segmenting....")
  os.makedirs(pathOut, exist_ok=True) # Replace Path with your desired Path.
  vidcap = cv2.VideoCapture(pathIn)
  fps = vidcap.get(cv2.CAP_PROP_FPS)
  success,image = vidcap.read()
  count = 0
  success = True
  while success:
    success,image = vidcap.read()
    #print ('Read a new frame: ', success) #check whether the video is segmented for each frame.
    cv2.imwrite( pathOut + "frame%d.png" % count, image)
    count += 1
  vidcap.release()

sampleVideo = 'to_segment.mp4'
dest_path = '/home/kamal/Desktop/major-project/frames/'
extractImages(sampleVideo, dest_path) # Choose your PathOut yourself.


#Combine respective frames into a video.
def frames_to_video(pathIn,pathOut,fps):
   print ('Combining...')
   image_array = []
   files = [f for f in os.listdir(pathIn) if os.path.isfile(pathIn + f)] #array of video frames path eg:'/home/kamal/Desktop/major-project/frames/frame1.png'
   files.sort(key = lambda x: int(x[5:-4]))
   for i in range(len(files)-1):
       img = cv2.imread(pathIn + files[i])
       size =  (img.shape[1],img.shape[0])
       img = cv2.resize(img,size)
       image_array.append(img)
   fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
   out = cv2.VideoWriter(pathOut,fourcc, fps, size)
   for i in range(len(image_array)):
       out.write(image_array[i])
   out.release()

pathIn = '/home/kamal/Desktop/major-project/frames/'
pathOut =  'joined_video.mp4'
fps = 23.976023976023978 #this fps is evaluated in extractImage method.
frames_to_video(pathIn,pathOut,fps)
