from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .segment import VideoScaler
import os
from django.core.cache import cache


def home(request):
    return render(request, 'index.html')


def save_video(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['fileUpload']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(filename)
        uploaded_path = fs.path(filename)
        video = VideoScaler(uploaded_path, './out.mp4')
        video_hash = video.hash
        if not cache.has_key(video_hash):
            print("Not Present in Cache")
            video.scale_normal(2)
            video.upscale()
            # video.scale_video(scale_x=2, scale_y=2)
            # video.sync_audio()
            cache.set(video_hash, True, timeout=None)
        else:
            print("Taking from cache")
        normal_url = fs.url('{}_normal.mp4'.format(video_hash))
        upscaled_url = fs.url('{}_upscaled.mp4'.format(video_hash))
        return render(request, 'video2.html', {'video_url': normal_url, 'video_url2': upscaled_url})
        # return render(request, 'video2.html', context={'video_url': full_url, 'video_url2': full_url2})


def show_video_comparison(request):
    full_url = 'http://127.0.0.1:8000/media/input.mp4'
    full_url2 = 'http://127.0.0.1:8000/media/cnn.mp4'
    return render(request, 'video2.html', context={'video_url': full_url, 'video_url2': full_url2})
