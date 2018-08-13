from django.urls import path

from ..views import home, save_video, show_video_comparison

urlpatterns = [
    path('', home),
    path('upload/', save_video, name='upload'),
    path('compare/', show_video_comparison, name='compare')
]