# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import subprocess
import sys
import os
sys.path.append(os.getcwd() + "youtube_dl")
from youtube_dl import YoutubeDL as YT


class VideoWidget(QtGui.QWidget):

    def __init__(self, title, orden, duración, vlc, mpv, descarga, preferido):
        QtGui.QWidget.__init__(self)
        self.orden = orden
        self.title = title
        self.duración = duración
        self.vlc = vlc
        self.mpv = mpv
        self.descarga = descarga
        self.preferido = preferido
        #
        self.setObjectName(("widget"))
        #self.resize(593, 176)
        self.sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(self.sizePolicy)
        #self.setMaximumSize(QtCore.QSize(530, 130))
        #self.setMinimumSize(QtCore.QSize(450, 150))
        self.playIcono = QtGui.QIcon(".iconos/play.svg")
        self.descargarIcono = QtGui.QIcon(".iconos/download.svg")
        self.agregarAListaIcono = QtGui.QIcon(".iconos/playlistAdd.svg")

        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName(("gridLayout"))

        #Botón Play
        self.playBtn = QtGui.QPushButton("Video", self)
        self.playBtn.setToolTip("Reproducir el video en un reproductor externo")
        self.playBtn.setIcon(self.playIcono)
        self.playBtn.setMaximumHeight(25)
        self.playBtn.setObjectName(("playBtn"))
        self.playBtn.pressed.connect(self.play)

        self.gridLayout.addWidget(self.playBtn, 2, 3, 1, 1)

        # Botón de Música
        self.musicaBtn = QtGui.QPushButton("Música", self)
        self.musicaBtn.setToolTip("Reproducir como sólo audio con el reproductor interno\nRequiere VLC Media Player")
        self.musicaBtn.setIcon(self.playIcono)
        self.musicaBtn.setMaximumHeight(25)
        self.musicaBtn.clicked.connect(self.reproducirMusica)

        self.gridLayout.addWidget(self.musicaBtn, 2, 4, 1, 1)

        #Label con título de video
        self.titleLabel = QtGui.QLabel(self.title, self)
        self.titleLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.titleLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setObjectName(("titleLabel"))

        self.gridLayout.addWidget(self.titleLabel, 0, 3, 2, 6)

        #Botón Descarga
        self.downloadBtn = QtGui.QPushButton("Descargar", self)
        self.downloadBtn.setToolTip("Descargar el video en el formato escogido")
        self.downloadBtn.setIcon(self.descargarIcono)
        self.downloadBtn.setMaximumHeight(25)
        self.downloadBtn.setObjectName(("downloadBtn"))
        self.downloadBtn.pressed.connect(self.descargar)

        self.gridLayout.addWidget(self.downloadBtn, 2, 7, 1, 1)

        # Botón de lista de reproducción
        self.listaBoton = QtGui.QPushButton(self)
        self.listaBoton.setToolTip("Agregar este video a la lista de reproducción actual")
        self.listaBoton.setIcon(self.agregarAListaIcono)
        self.listaBoton.setMaximumSize(25, 25)

        self.gridLayout.addWidget(self.listaBoton, 2, 8, 1, 1)

        #Label del thumbnail
        self.thumbLabel = QtGui.QLabel(self)
        self.pic = QtGui.QPixmap(".thumbs/" + str(self.orden) + ".jpg")
        self.thumbLabel.setPixmap(self.pic)
        self.thumbLabel.setScaledContents(True)
        self.thumbLabel.setMaximumWidth(220)
        self.thumbLabel.setMaximumHeight(120)

        self.gridLayout.addWidget(self.thumbLabel, 0, 0, 3, 3)

        # Label de Duración de video
        self.duracionLabel = QtGui.QLabel(self)
        self.duracionLabel.setStyleSheet("color: white; background-color: black")
        #self.duracionLabel.setStyleSheet("color: white")
        self.duracionLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.duracionLabel.setText(str(self.duración))

        self.gridLayout.addWidget(self.duracionLabel, 2, 0, 1, 1)

        #Label de duración
        #self.durLabel = QtGui.QLabel("Time: " + str(self.duración), self)
        #self.durLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        #self.gridLayout.addWidget(self.durLabel, 2, 4, 1, 1)

    # Funciones de clase.
    def play(self):
        if "VLC" in self.preferido:
            subprocess.Popen(self.vlc)
        if "MPV" in self.preferido:
            subprocess.Popen(self.mpv)

    def descargar(self):
        self.parent().parent().parent().parent().parent().seleccionDeCalidad()
        self.parent().parent().parent().parent().parent().link = self.descarga[0]
        #Dialogo que consulta la calidad y formato
        #self.dialogo = self.formato()
        """
        ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mp4'
                        }]
                    }

        with YT(ydl_opts) as yt:
            homedir = os.getenv("HOME")
            exdir = os.getcwd() #exdir es el directorio actual, se guarda para saber donde volver una vez completada la descarga
            #print(exdir)
            if not os.path.exists(homedir+ "/Descargas/GUIYoutube"): os.makedirs(homedir+"/Descargas/GUIYoutube")
            os.chdir(homedir+"/Descargas/GUIYoutube")
            #print(os.getcwd())
            yt.download([self.descarga[0]])
            os.chdir(exdir)"""
            #self.popup = QtGui.QMessageBox.information(self, "Informacion", """Descarga finalizada (revise la carpeta Descargas)""",QtGui.QMessageBox.Ok)


    def formato(self):
        # Pop-up para elegir reproductor.
        self.popup = QtGui.QMessageBox()
        self.popup.setText("Seleccione un formato para su descarga.")
        self.mp3 = self.popup.addButton("MP3(audio)", QtGui.QMessageBox.ActionRole)
        self.mp4 = self.popup.addButton("MP4(video)", QtGui.QMessageBox.ActionRole)
        self.popup.exec()
        if "MP3" in self.popup.clickedButton().text():
            self.formato = "MP3"
        if "MP4" in self.popup.clickedButton().text():
            self.formato = "MP4"
        return self.formato

    def reproducirMusica(self):
        self.parent().parent().parent().parent().parent().crearReproductorDeMusica(self.descarga[0], self.orden, self.title)


"""
Lo siguiente es el nivel que hay que subir para alcanzar la ventana principal. No borrar!!!!!!!!

self.parent().parent().parent().parent().parent().printerFunc()
"""