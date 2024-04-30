from django.contrib import admin
from django.urls import path

from video.views import getVideos, syncVideos

urlpatterns = [
    path("videos/", getVideos),
    path("sync/", syncVideos),
]
