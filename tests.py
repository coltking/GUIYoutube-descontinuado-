#-*- encoding = utf-8 -*-

#import urllib.request as U
#import bs4 as bs
import sys
import os
#from PyQt4 import QtGui, QtCore
sys.path.append(os.getcwd() + "youtube_dl")
#from youtube_dl import YoutubeDL as YT
import subprocess

#from PyQt4.phonon import Phonon as P

#https://www.youtube.com/watch?v=rcXxbuCSaeY
url = "www.youtube.com/watch?v=OWodAv1KHaM"
#os.chdir("youtube_dl")
print(os.getcwd())
stream = subprocess.Popen(["python3 youtube_dl/__main__.py " + url + " -o - | mpv -"],
                            shell=True, stdout=subprocess.PIPE)


while stream.poll() is None:
    pass
    #std = stream.stdout.readline()
    #print(std)