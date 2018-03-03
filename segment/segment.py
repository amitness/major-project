import os
import cv2

# Segment video into respective frames.
def extract_frames(pathIn):
    print("Extracting frames from video ...")
    #os.makedirs(pathOut, exist_ok=True)
    vidcap = cv2.VideoCapture(pathIn)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    success, frame = vidcap.read()
    frames = []
    while success:
        # cv2.imwrite(pathOut + "frame%d.png" % count, image)
        frames.append(frame)
        success, frame = vidcap.read()
    vidcap.release()
    print("Total frames extracted : %d" % len(frames))
    return fps, frames


def extract_fps(path):
    vidcap = cv2.VideoCapture(path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    return fps

def scale_frames(frames, scaleX=4, scaleY=4):
    print("Scaling images")
    scaled_frames = []
    for frame in frames:
       size =  (frame.shape[1],frame.shape[0])
       scaled_frame = cv2.resize(frame, (0,0), fx=scaleX, fy=scaleY, interpolation=cv2.INTER_CUBIC)
       scaled_frames.append(scaled_frame)
    return scaled_frames

# Combine respective frames into a video
def frames_to_video(frames, fps, pathOut="./out.mp4"):
    print('Combining frames')
    # Array of video frames path eg:'/home/kamal/Desktop/major-project/frames/frame1.png'
    # files = [f for f in os.listdir(pathIn) if os.path.isfile(pathIn + f)]
    # files.sort(key=lambda x: int(x[5:-4]))
    # for file in files:
    #    img = cv2.imread(pathIn + file)
    #    size =  (img.shape[1],img.shape[0])
    #    img = cv2.resize(img,size,interpolation = cv2.INTER_CUBIC)
    #    image_array.append(img)
    fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
    out = cv2.VideoWriter(pathOut, fourcc, fps, frames[0].shape[:2][::-1])
    for frame in frames:
       out.write(frame)
    out.release()

def scale_video(video_location, dest_path="./out.mp4", scaleX=2, scaleY=2):
    fps, frames = extract_frames(video_location)  # Choose your PathOut yourself.
    scaled_frames = scale_frames(frames, scaleX, scaleY)
    frames_to_video(scaled_frames, fps, dest_path)

if __name__ == '__main__':
    video_location = 'to_segment.mp4'
    scale_video(video_location, dest_path="./out.mp4", scaleX=2, scaleY=2)
    # dest_path = './frames/'
    # fps, frames = extract_frames(video_location)  # Choose your PathOut yourself.
    # scaled_frames = scale_frames(frames)
    # pathIn = './frames/'
    # pathOut =  'joined_video.mp4'
    # fps = extract_fps(sample_video)  # this fps is evaluated in extractImage method.
    # frames_to_video(scaled_frames, fps)
