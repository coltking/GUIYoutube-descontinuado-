#-*- encoding = utf-8 -*-
import urllib.request
#from PIL import Image
import sys
import youtube
import subprocess
from PyQt4 import QtGui, QtCore
#import re
from videoWidget import *

#numberOfParameters = 4

#titles = []
#IDs = []
#duration = []
#thumbs = []


class Window(QtGui.QMainWindow):


    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 740, 360)
        self.setWindowTitle("GUIYoutube")
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        ############ Main Menu
        exitMenuEntry = QtGui.QAction("Exit this application.", self)
        exitMenuEntry.setShortcut("Ctrl+Alt+Q")
        exitMenuEntry.setStatusTip("Exit this application")
        exitMenuEntry.triggered.connect(self.closeApp)

        self.statusBar()

        mainMenu = self.menuBar()

        menuFile = mainMenu.addMenu("File")
        menuFile.addAction(exitMenuEntry)

        #videoBlock = VideoWidget()

        self.startPage()

    def startPage(self):

        self.mainW = QtGui.QScrollArea(self)
        self.mainW.setWidgetResizable(True)
        self.listW = QtGui.QWidget(self)
        self.mainL = QtGui.QGridLayout(self)
        self.setCentralWidget(self.mainW)
        self.listW.setLayout(self.mainL)


        for i in range(0, 4):
            title = "This is a test video title! :) It wraps around nicely in it's frame. Also Ñ and ñ are good."
            self.videoBlock = VideoWidget(title)
            self.mainL.addWidget(self.videoBlock)

        self.mainW.setWidget(self.listW)


        self.show()

    def closeApp(self):

        choice = QtGui.QMessageBox.question(self, "Exiting App",
                                            "Are you sure you want out?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Closing App!")
            sys.exit()
        else:
            pass

    #def enlargeWindow(self, state):
        #if state == QtCore.Qt.Checked:
            #self.setGeometry(50, 50, 800, 600)
        #else:
            #self.setGeometry(100, 100, 640, 360)

    #def download(self):
        #self.percentage = 0

        #while self.percentage < 100:
            #self.percentage += 0.00005
            #self.progress.setValue(self.percentage)

    #def styleChange(self, text):
        self.style.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

##################################################

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()


#with subprocess.Popen('youtube-dl "ytsearch2:Godot Engine" --get-id --get-title --get-duration --get-thumb',
     #stdout=subprocess.PIPE, shell=True) as process:
    #members = []
    #clean = []
    #while process.poll() is None:
        #results = process.stdout.readline()
        #members.append(str(results))

    #for i in range(0, len(members)):
        #if len(members[i]) > 5:
            #clean.append(members[i][2:-3])

#for i in range(0, len(clean), numberOfParameters):
    #titles.append(clean[i])
#for i in range(1, len(clean), numberOfParameters):
    #IDs.append(clean[i])
#for i in range(2, len(clean), numberOfParameters):
    #thumbs.append(clean[i])
#for i in range(3, len(clean), numberOfParameters):
    #duration.append(clean[i])

#for i in range(0, len(titles)):
    #print("Video", str(i), ":", titles[i], ". Duration:", duration[i], "Mns. ID:", '"', IDs[i], '".')

#thumbN = 00
#for i in range(0, len(thumbs)):

    #urllib.request.urlretrieve(thumbs[i], "thumbs/thumb" + str(thumbN) + ".jpg")
    #thumbN += 1
    #print(thumbs[i])