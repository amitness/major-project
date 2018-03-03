import os
import cv2


# Segment video into respective frames.
def extract_frames(pathIn):
    print("Extracting frames from video ...")
    vidcap = cv2.VideoCapture(pathIn)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    success, frame = vidcap.read()
    frames = []
    while success:
        frames.append(frame)
        success, frame = vidcap.read()
    vidcap.release()
    print("Total frames extracted : %d" % len(frames))
    return fps, frames


def extract_fps(path):
    vidcap = cv2.VideoCapture(path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    return fps

def scale_frames(frames, scale_x=4, scale_y=4):
    print("Scaling images")
    scaled_frames = []
    for frame in frames:
       size =  (frame.shape[1],frame.shape[0])
       scaled_frame = cv2.resize(frame, (0,0), fx=scale_x, fy=scale_y, interpolation=cv2.INTER_CUBIC)
       scaled_frames.append(scaled_frame)
    return scaled_frames

# Combine respective frames into a video
def frames_to_video(frames, fps, pathOut="./out.mp4"):
    print('Combining frames')
    fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
    out = cv2.VideoWriter(pathOut, fourcc, fps, frames[0].shape[:2][::-1])
    for frame in frames:
       out.write(frame)
    out.release()

def scale_video(video_location, dest_path="./out.mp4", scale_x=2, scale_y=2):
    fps, frames = extract_frames(video_location)  # Choose your PathOut yourself.
    scaled_frames = scale_frames(frames, scale_x, scale_y)
    frames_to_video(scaled_frames, fps, dest_path)


if __name__ == '__main__':
    video_location = 'to_segment.mp4'
    scale_video(video_location, dest_path="./out.mp4", scale_x=2, scale_y=2)

