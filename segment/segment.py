import os
import cv2
import subprocess
import logging
from moviepy.editor import VideoFileClip

logging.basicConfig(level=logging.DEBUG)

class VideoScaler(object):

    def __init__(self, path_in, path_out):
        if  os.path.exists(path_in):
            self.__path_in = path_in
        else:
            raise IOError('File does not exist: {}'.format(path_in))
        self.__path_out  = path_out

    def extract_frames(self):
        logging.info("Extracting frames from video ...")
        vidcap = cv2.VideoCapture(self.__path_in)
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        success, frame = vidcap.read()
        frames = []
        while success:
            frames.append(frame)
            success, frame = vidcap.read()
        vidcap.release()
        logging.debug("Total frames extracted : {}".format(len(frames)))
        return fps, frames


    def scale_frames(self, frames, scale_x=4, scale_y=4):
        logging.info('Scaling images')
        scaled_frames = []
        for frame in frames:
           size =  (frame.shape[1],frame.shape[0])
           scaled_frame = cv2.resize(frame, (0,0), fx=scale_x, fy=scale_y, interpolation=cv2.INTER_CUBIC)
           scaled_frames.append(scaled_frame)
        return scaled_frames

    def frames_to_video(self, frames, fps):
        logging.info('Combining frames')
        fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
        resolution = frames[0].shape[:2][::-1]
        out = cv2.VideoWriter(self.__path_out, fourcc, fps, resolution)
        for frame in frames:
           out.write(frame)
        out.release()

    def sync_audio(self):
        audio_extract_command = "ffmpeg -i {} -f mp3 -ab 192000 -vn out.mp3 -loglevel quiet".format(self.__path_in)
        audio_merge_command = "ffmpeg -i out.mp4 -i out.mp3 -c:v copy -c:a aac -strict experimental output.mp4 -loglevel quiet"

        subprocess.call(audio_extract_command, shell=True)
        subprocess.call(audio_merge_command, shell=True)


    def scale_video(self,scale_x, scale_y):
        fps, frames = self.extract_frames()
        scaled_frames = self.scale_frames(frames, scale_x, scale_y)
        self.frames_to_video(scaled_frames, fps)

    def update_codec(self):
        clip = VideoFileClip('output.mp4')
        clip.write_videofile("output_final.mp4")

if  __name__ == '__main__':
    video = VideoScaler('to_segment.mp4', './out.mp4')
    video.scale_video(scale_x = 2, scale_y = 2)
    video.sync_audio()
    video.update_codec()
