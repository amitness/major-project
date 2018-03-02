import os
import numpy as np
import cv2

# Segment video into respective frames.
def extractImages(pathIn, pathOut):
  print ("Segmenting....")
  os.makedirs(pathOut, exist_ok=True) # Replace Path with your desired Path.
  vidcap = cv2.VideoCapture(pathIn)
  fps = vidcap.get(cv2.CAP_PROP_FPS)
  success,image = vidcap.read()
  count = 0
  while success:
    cv2.imwrite( pathOut + "frame%d.png" % count, image)
    success,image = vidcap.read()
    count += 1
  vidcap.release()

sampleVideo = 'to_segment.mp4'
dest_path = './frames/'
extractImages(sampleVideo, dest_path) # Choose your PathOut yourself.


#Combine respective frames into a video.
def frames_to_video(pathIn,pathOut,fps):
   print ('Combining...')
   image_array = []
   # Array of video frames path eg:'/home/kamal/Desktop/major-project/frames/frame1.png'
   files = [f for f in os.listdir(pathIn) if os.path.isfile(pathIn + f)] 
   files.sort(key = lambda x: int(x[5:-4]))
   for file in files:
       img = cv2.imread(pathIn + file)
       size =  (img.shape[1],img.shape[0])
       img = cv2.resize(img,size,interpolation = cv2.INTER_CUBIC)
       image_array.append(img)
   fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
   out = cv2.VideoWriter(pathOut,fourcc, fps, size)
   for image in image_array:
       out.write(image)
   out.release()

pathIn = './frames/'
pathOut =  'joined_video.mp4'
fps = 23.976023976023978 #this fps is evaluated in extractImage method.
frames_to_video(pathIn,pathOut,fps)