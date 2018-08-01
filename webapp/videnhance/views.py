from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'index.html')


def save_video(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['fileUpload']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        # TODO: THis url will be used in future to give user download link
        url = fs.url(filename)
        full_url = request.build_absolute_uri(url)
        import time
        time.sleep(2)
        # return redirect(full_url)
        # return HttpResponse(template)
        return render(request, 'video.html', context={'video_url': full_url})

