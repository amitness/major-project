import os
import cv2


class Video:

    def __init__(self, path_in, path_out):
        self.__path_in = path_in
        self.__path_out  = path_out

    # Segment video into respective frames.
    def extract_frames(self):
        print("Extracting frames from video ...")
        vidcap = cv2.VideoCapture(self.__path_in)
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        success, frame = vidcap.read()
        frames = []
        while success:
            frames.append(frame)
            success, frame = vidcap.read()
        vidcap.release()
        print("Total frames extracted : %d" % len(frames))
        return fps, frames


    def extract_fps(self):
        vidcap = cv2.VideoCapture(self.__path_in)
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        return fps

    def scale_frames(self, frames, scale_x=4, scale_y=4):
        print("Scaling images")
        scaled_frames = []
        for frame in frames:
           size =  (frame.shape[1],frame.shape[0])
           scaled_frame = cv2.resize(frame, (0,0), fx=scale_x, fy=scale_y, interpolation=cv2.INTER_CUBIC)
           scaled_frames.append(scaled_frame)
        return scaled_frames

    # Combine respective frames into a video
    def frames_to_video(self, frames, fps):
        print('Combining frames')
        fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
        out = cv2.VideoWriter(self.__path_out, fourcc, fps, frames[0].shape[:2][::-1])
        for frame in frames:
           out.write(frame)
        out.release()

    def scale_video(self,scale_x, scale_y):
        fps, frames = self.extract_frames()  # Choose your PathOut yourself.
        scaled_frames = self.scale_frames(frames, scale_x, scale_y)
        self.frames_to_video(scaled_frames, fps)


video = Video('to_segment.mp4', './out.mp4')
video.scale_video(scale_x = 2, scale_y = 2)
