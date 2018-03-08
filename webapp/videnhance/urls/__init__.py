from django.urls import path

from videnhance.views import home, save_video

urlpatterns = [
    path('', home),
    path('upload/', save_video, name='upload')
]