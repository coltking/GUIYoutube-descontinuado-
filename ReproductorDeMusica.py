#! /usr/bin/env python3
# -*- encoding=utf-8 -*-

import os
from PyQt4 import QtGui, QtCore
import subprocess
import vlc

class reproductorDeMusica(QtGui.QWidget):

    def __init__(self, link, thumbNumero, titulo):
        QtGui.QWidget.__init__(self)
        self.link = link
        self.thumbNumero = thumbNumero
        self.titulo = titulo

        # Lista de títulos
        self.titulos = []

        # Lista de thumbnails
        self.miniaturas = []

        # Iconos
        self.playIcono = QtGui.QIcon(".iconos/play.svg")
        self.pausaIcono = QtGui.QIcon(".iconos/pause.svg")
        self.stopIcono = QtGui.QIcon(".iconos/stop.svg")
        self.adelanteIcono = QtGui.QIcon(".iconos/forward.svg")
        self.atrasIcono = QtGui.QIcon(".iconos/backwards.svg")
        self.aleatorioIcono = QtGui.QIcon(".iconos/shuffle.svg")
        self.repetirIcono = QtGui.QIcon(".iconos/repeat.svg")
        self.volumenIcono = QtGui.QIcon(".iconos/volume.svg")

        self.instancia = vlc.Instance()
        self.reproductor = self.instancia.media_player_new()
        self.reproductorDeLista = self.instancia.media_list_player_new()
        self.reproductorDeLista.set_media_player(self.reproductor)

        self.listaDeReproduccion = self.instancia.media_list_new()

        # Widget del reproductor
        self.construirWidget()

    def construirWidget(self):
        # Reproductor
        #self.contenedor = QtGui.QFrame(self)
        self.contenedorLayout = QtGui.QGridLayout(self)
        self.contenedorLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedorLayout.setHorizontalSpacing(20)
        #self.contenedor.setLayout(self.contenedorLayout)

        # Thumbnail
        thumb = QtGui.QPixmap(".thumbs/" + str(self.thumbNumero) + ".jpg")
        self.miniaturaFrame = QtGui.QLabel( self)
        self.miniaturaFrame.setPixmap(thumb)
        self.miniaturaFrame.setScaledContents(True)
        self.miniaturaFrame.setMinimumWidth(200)
        self.miniaturaFrame.setMaximumWidth(220)
        self.miniaturaFrame.setMaximumHeight(120)
        self.contenedorLayout.addWidget(self.miniaturaFrame, 0, 0, 3, 3)

        # Título
        self.tituloWidget = QtGui.QLabel(self.titulo, self)
        self.tituloWidget.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.contenedorLayout.addWidget(self.tituloWidget, 0, 3, 1, 8)

        # Botones
        self.atrasBoton = QtGui.QPushButton(self)
        self.atrasBoton.setMaximumSize(25, 25)
        self.atrasBoton.setIcon(self.atrasIcono)
        self.atrasBoton.clicked.connect(self.atras)
        self.contenedorLayout.addWidget(self.atrasBoton, 2, 3, 1, 1)

        self.playBoton = QtGui.QPushButton(self)
        self.playBoton.setMaximumSize(25, 25)
        self.playBoton.setIcon(self.pausaIcono)
        self.playBoton.clicked.connect(self.play)
        self.contenedorLayout.addWidget(self.playBoton, 2, 4, 1, 1)

        self.stopBoton = QtGui.QPushButton(self)
        self.stopBoton.setMaximumSize(25, 25)
        self.stopBoton.setIcon(self.stopIcono)
        self.stopBoton.clicked.connect(self.stop)
        self.contenedorLayout.addWidget(self.stopBoton, 2, 5, 1, 1)

        self.adelanteBoton = QtGui.QPushButton(self)
        self.adelanteBoton.setMaximumSize(25, 25)
        self.adelanteBoton.setIcon(self.adelanteIcono)
        self.adelanteBoton.clicked.connect(self.adelante)
        self.contenedorLayout.addWidget(self.adelanteBoton, 2, 6, 1, 1)

        # Botón espaciador
        self.espaciadorBoton = QtGui.QPushButton(self)
        self.espaciadorBoton.setFlat(True)
        self.contenedorLayout.addWidget(self.espaciadorBoton, 2, 7, 1, 1)

        self.contenedorLayout.setColumnMinimumWidth(7, 300)

        self.aleatorioBoton = QtGui.QPushButton(self)
        self.aleatorioBoton.setMaximumSize(25, 25)
        self.aleatorioBoton.setIcon(self.aleatorioIcono)
        self.contenedorLayout.addWidget(self.aleatorioBoton, 2, 8, 1, 1)

        self.repetirBoton = QtGui.QPushButton(self)
        self.repetirBoton.setMaximumSize(25, 25)
        self.repetirBoton.setIcon(self.repetirIcono)
        self.contenedorLayout.addWidget(self.repetirBoton, 2, 9, 1, 1)

        # Botón espaciador
        self.espaciador2Boton = QtGui.QPushButton(self)
        self.espaciador2Boton.setFlat(True)
        self.contenedorLayout.addWidget(self.espaciador2Boton, 2, 10, 1, 1)

        self.contenedorLayout.setColumnMinimumWidth(7, 50)

        self.volumenBoton = QtGui.QPushButton(self)
        self.volumenBoton.setMaximumSize(25, 25)
        self.volumenBoton.setFlat(True)
        self.volumenBoton.setIcon(self.volumenIcono)
        self.contenedorLayout.addWidget(self.volumenBoton, 2, 11, 1, 1)

        # Slider para control de volumen
        self.volumenSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        self.volumenSlider.setMinimum(0)
        self.volumenSlider.setMaximum(100)
        self.volumenSlider.setValue(self.reproductor.audio_get_volume())
        self.volumenSlider.valueChanged.connect(self.volumen)

        self.contenedorLayout.addWidget(self.volumenSlider, 0, 12, 3, 1)

        # Slider para tiempo de reproducción (seek)
        self.lineaDeTiempoSlider = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        self.contenedorLayout.addWidget(self.lineaDeTiempoSlider, 1, 3, 1, 9)

    def construirMedio(self):
        self.medio = self.buscarEnlace()
        self.stream = self.instancia.media_new("https" + self.medio[-1][:-1])
        self.listaDeReproduccion.add_media(self.stream)

        self.titulos.append(self.titulo)
        self.miniaturas.append(self.thumbNumero)

        self.reproductorDeLista.set_media_list(self.listaDeReproduccion)
        self.reproductor.audio_set_volume(100)

        self.play()

    def buscarEnlace(self):
        with subprocess.Popen(['python3 youtube_dl/__main__.py --get-url ' + self.link + '--get-url'],
        stdout=subprocess.PIPE,
        shell=True, universal_newlines=True) as proc:
            texto = proc.stdout.read()

        textoSplit = texto.split("https")
        return textoSplit

    def play(self):
        if self.reproductorDeLista.is_playing():
            self.reproductorDeLista.pause()
            self.playBoton.setIcon(self.playIcono)
        elif not self.reproductorDeLista.is_playing():
            self.reproductorDeLista.play()
            self.playBoton.setIcon(self.pausaIcono)

    def stop(self):
        self.reproductor.stop()
        self.playBoton.setIcon(self.playIcono)
        self.parent().parent().destruirReproductorDeMusica()

    def adelante(self):
        self.reproductorDeLista.next()
        pass

    def atras(self):
        self.reproductorDeLista.previous()

    def cambiarMedio(self, descarga, thumbNumero, titulo):
        self.thumbNumero = thumbNumero
        self.titulo = titulo
        self.link = descarga

        self.tituloWidget.setText(self.titulo)
        self.medioNuevo = self.buscarEnlace()
        self.streamNuevo = self.instancia.media_new("https" + self.medioNuevo[-1][:-1])



        thumbNuevo = QtGui.QPixmap(".thumbs/" + str(self.thumbNumero) + ".jpg")


        self.reproductor.set_media(self.streamNuevo)
        self.miniaturaFrame.setPixmap(thumbNuevo)
        self.play()

        return True

    def agregarALista(self, link, titulo, thumbNumero):
        self.link = link

        itemDeLista = self.buscarEnlace()
        print(itemDeLista)
        nuevoMedio = self.instancia.media_new("https" + itemDeLista[-1][:-1])
        self.listaDeReproduccion.add_media(nuevoMedio)

        self.titulos.append(titulo)
        miniatura = self.generarMiniaturaDeLista(thumbNumero)
        self.miniaturas.append(miniatura)

    def generarMiniaturaDeLista(self, thumbNumero):
        pass

    def volumen(self, volumen):
        self.reproductor.audio_set_volume(volumen)