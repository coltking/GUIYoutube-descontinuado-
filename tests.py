#-*- encoding = utf-8 -*-

import urllib.request as U
import bs4 as bs
import sys
import os
sys.path.append(os.getcwd() + "youtube_dl")
from youtube_dl import YoutubeDL as YT
import subprocess

global link

titles = []
IDs = []
duration = []

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4'
    }]
    }

with YT(ydl_opts) as yt:
    yt.download(['https://www.youtube.com/watch?v=OWodAv1KHaM'])