#! /usr/bin/env python3
# -*- encoding=utf-8 -*-

import os
import shutil
import string
import random
from PyQt4 import QtGui, QtCore
import subprocess
import vlc


class reproductorDeMusica(QtGui.QWidget):

    def __init__(self, link, thumbNumero, titulo):
        QtGui.QWidget.__init__(self)
        self.link = link
        self.thumbNumero = thumbNumero
        self.titulo = titulo

        self.indiceDePista = 0

        # Lista de titulos
        self.listaDeReproduccionTemporal = []

        # Iconos
        self.playIcono = QtGui.QIcon(".iconos/play.png")
        self.pausaIcono = QtGui.QIcon(".iconos/pause.png")
        self.stopIcono = QtGui.QIcon(".iconos/stop.png")
        self.adelanteIcono = QtGui.QIcon(".iconos/forward.png")
        self.atrasIcono = QtGui.QIcon(".iconos/backwards.png")
        self.aleatorioIcono = QtGui.QIcon(".iconos/shuffle.png")
        self.repetirIcono = QtGui.QIcon(".iconos/repeat.png")
        self.volumenIcono = QtGui.QIcon(".iconos/volume.png")

        # LibVLC
        self.instancia = vlc.Instance()
        self.reproductor = self.instancia.media_player_new()
        self.reproductorDeLista = self.instancia.media_list_player_new()
        self.reproductorDeLista.set_media_player(self.reproductor)

        self.listaDeReproduccion = self.instancia.media_list_new()

        self.setStyleSheet("border: 1px solid white")

        self.administradorDeEventos = self.reproductor.event_manager()
        self.administradorDeEventos.event_attach(vlc.EventType.MediaPlayerMediaChanged, self.eventoMedioCambiado)

        # Temporizador para refrescar la interfaz
        self.temporizador = QtCore.QTimer(self)
        self.temporizador.timeout.connect(self.actualizarLineaDeTiempo)

        # Widget del reproductor
        self.construirWidget()

    def construirWidget(self):
        self.sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                            QtGui.QSizePolicy.Expanding)
        self.setSizePolicy(self.sizePolicy)

        # Reproductor
        self.contenedor = QtGui.QWidget(self)
        wallpaper = ".thumbs/" + str(self.thumbNumero) + ".jpg"
        self.setStyleSheet("background-image: url(" + wallpaper + "); background-position: left")
        self.setAutoFillBackground(True)
        self.contenedorLayout = QtGui.QGridLayout(self)
        self.setLayout(self.contenedorLayout)

        self.contenedorLayout.addWidget(self.contenedor, 0, 0, 4, 12)
        self.contenedorLayout.setHorizontalSpacing(0)
        self.contenedorLayout.setVerticalSpacing(0)

        # Titulo
        self.tituloWidget = QtGui.QLabel(self.titulo, self)
        self.tituloWidget.setStyleSheet("""background-image: url(bg.png);
                                        font: 'Liberation Sans';
                                        font-size: 20px""")
        self.tituloWidget.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.contenedorLayout.addWidget(self.tituloWidget, 0, 0, 2, 11)

        # Botones
        self.atrasBoton = QtGui.QPushButton(self)
        self.atrasBoton.setFlat(True)
        self.atrasBoton.setStyleSheet("background-image: url(bg.png)")
        self.atrasBoton.setMaximumSize(35, 35)
        self.atrasBoton.setIcon(self.atrasIcono)
        self.atrasBoton.clicked.connect(self.atras)
        self.contenedorLayout.addWidget(self.atrasBoton, 3, 0, 1, 1)

        self.playBoton = QtGui.QPushButton(self)
        self.playBoton.setFlat(True)
        self.playBoton.setStyleSheet("background-image: url(bg.png)")
        self.playBoton.setMaximumSize(35, 35)
        self.playBoton.setIcon(self.pausaIcono)
        self.playBoton.clicked.connect(self.play)
        self.contenedorLayout.addWidget(self.playBoton, 3, 1, 1, 1)

        self.stopBoton = QtGui.QPushButton(self)
        self.stopBoton.setFlat(True)
        self.stopBoton.setStyleSheet("background-image: url(bg.png)")
        self.stopBoton.setMaximumSize(35, 35)
        self.stopBoton.setIcon(self.stopIcono)
        self.stopBoton.clicked.connect(self.stop)
        self.contenedorLayout.addWidget(self.stopBoton, 3, 2, 1, 1)

        self.adelanteBoton = QtGui.QPushButton(self)
        self.adelanteBoton.setFlat(True)
        self.adelanteBoton.setStyleSheet("background-image: url(bg.png)")
        self.adelanteBoton.setMaximumSize(35, 35)
        self.adelanteBoton.setIcon(self.adelanteIcono)
        self.adelanteBoton.clicked.connect(self.adelante)
        self.contenedorLayout.addWidget(self.adelanteBoton, 3, 3, 1, 1)

        # Dummy boton
        self.dummyBoton = QtGui.QPushButton(self)
        self.dummyBoton.setFlat(True)
        self.dummyBoton.setMaximumSize(5, 5)
        self.dummyBoton.clicked.connect(self.actualizarEstilo)
        self.contenedorLayout.addWidget(self.dummyBoton, 3, 6, 1, 1)

        self.aleatorioBoton = QtGui.QPushButton(self)
        self.aleatorioBoton.setFlat(True)
        self.aleatorioBoton.setStyleSheet("background-image: url(bg.png)")
        self.aleatorioBoton.setMaximumSize(35, 35)
        self.aleatorioBoton.setIcon(self.aleatorioIcono)
        self.aleatorioBoton.clicked.connect(self.modoAleatorio)

        self.contenedorLayout.addWidget(self.aleatorioBoton, 3, 7, 1, 1)

        self.repetirBoton = QtGui.QPushButton(self)
        self.repetirBoton.setFlat(True)
        self.repetirBoton.setStyleSheet("background-image: url(bg.png)")
        self.repetirBoton.setMaximumSize(35, 35)
        self.repetirBoton.setIcon(self.repetirIcono)
        self.repetirBoton.clicked.connect(self.modoRepeticion)
        self.contenedorLayout.addWidget(self.repetirBoton, 3, 8, 1, 1)

        self.volumenBoton = QtGui.QPushButton(self)
        self.volumenBoton.setStyleSheet("background-image: url(bg.png)")
        self.volumenBoton.setMaximumSize(25, 25)
        self.volumenBoton.setIconSize(QtCore.QSize(15, 15))
        self.volumenBoton.setFlat(True)
        self.volumenBoton.setIcon(self.volumenIcono)
        self.contenedorLayout.addWidget(self.volumenBoton, 3, 10, 1, 1)

        # Slider para control de volumen
        self.volumenSlider = QtGui.QSlider(QtCore.Qt.Vertical, self)
        self.volumenSlider.setStyleSheet("background-image: url(bg.png)")
        self.volumenSlider.setMinimum(0)
        self.volumenSlider.setMaximum(100)
        self.volumenSlider.valueChanged.connect(self.volumen)

        self.contenedorLayout.addWidget(self.volumenSlider, 0, 11, 4, 1)

        # Slider para tiempo de reproduccion (seek)
        self.lineaDeTiempoSlider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.lineaDeTiempoSlider.setStyleSheet("background-image: url(bg.png)")
        self.lineaDeTiempoSlider.setMaximum(1000)
        self.lineaDeTiempoSlider.sliderMoved.connect(self.cambiarTiempo)

        self.contenedorLayout.addWidget(self.lineaDeTiempoSlider, 2, 0, 1, 11)

        # Eliminar el espacio entre el slider de volumen y los demás widgets
        self.contenedorLayout.setColumnMinimumWidth(11, 0)

    def construirMedio(self):
        self.medio = self.buscarEnlace()
        self.stream = self.instancia.media_new("https" + self.medio[-1][:-1])
        #self.stream.parse()
        self.listaDeReproduccion.add_media(self.stream)

        self.listaDeRreproduccionTemporal = []

        self.reproductorDeLista.set_media_list(self.listaDeReproduccion)

        self.play()
        self.temporizador.start(1000)
        self.reproductor.audio_set_volume(50)
        self.volumenSlider.setValue(self.reproductor.audio_get_volume())

        # Para listas de reproducción
        nombreDeThumb = str(random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.ascii_lowercase))
        shutil.copy(".thumbs/" + str(self.thumbNumero) + ".jpg", ".thumbsTemporales/" + nombreDeThumb + ".jpg")

        # Diccionario
        if len(self.listaDeReproduccionTemporal) > 0:
            for i in len(self.listaDeReproduccionTemporal):
                os.remove(self.listaDeReproduccionTemporal[i]["thumbTemporal"])

        self.listaDeReproduccionTemporal = []
        diccionario = {}
        diccionario["titulo"] = self.titulo
        diccionario["thumbTemporal"] = ".thumbsTemporales/" + nombreDeThumb + ".jpg"

        self.listaDeReproduccionTemporal.append(diccionario)
        self.actualizarLista()

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

            self.temporizador.start(1000)

        elif not self.reproductorDeLista.is_playing():
            self.reproductorDeLista.play()
            self.playBoton.setIcon(self.pausaIcono)

        self.reproduciendo = True

    def stop(self):
        self.reproductor.stop()
        self.playBoton.setIcon(self.playIcono)

        self.parent().parent().destruirReproductorDeMusica()
        self.parent().parent().limpiarThumbsTemporales()

    def adelante(self):
        self.reproductorDeLista.next()

    def atras(self):
        self.reproductorDeLista.previous()

    def cambiarMedio(self, descarga, thumbNumero, titulo):
        self.thumbNumero = thumbNumero
        self.titulo = titulo
        self.link = descarga

        self.tituloWidget.setText(self.titulo)
        self.medioNuevo = self.buscarEnlace()
        self.streamNuevo = self.instancia.media_new("https" + self.medioNuevo[-1][:-1])

        # Liberando elementos de la lista
        self.listaDeReproduccion.unlock()
        self.listaDeReproduccion.release()
        self.listaDeReproduccion = self.instancia.media_list_new()
        self.reproductorDeLista.set_media_list(self.listaDeReproduccion)

        self.listaDeReproduccion.add_media(self.streamNuevo)

        wallpaper = ".thumbs/" + str(self.thumbNumero) + ".jpg"
        self.setStyleSheet("background-image: url(" + wallpaper + "); background-position: left")
        QtGui.QApplication.processEvents()
        self.setStyleSheet("background-image: url(" + wallpaper + "); background-position: left")

        self.reproductorDeLista.stop()
        self.reproductorDeLista.play()
        self.actualizarLista()

        # Para listas de reproducción
        nombreDeThumb = str(random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.ascii_lowercase))
        shutil.copy(".thumbs/" + str(self.thumbNumero) + ".jpg", ".thumbsTemporales/" + nombreDeThumb + ".jpg")

        # Diccionario
        if len(self.listaDeReproduccionTemporal) > 0:
            for i in range(0, len(self.listaDeReproduccionTemporal)):
                os.remove(self.listaDeReproduccionTemporal[i]["thumbTemporal"])

        self.listaDeReproduccionTemporal = []
        diccionario = {}
        diccionario["titulo"] = self.titulo
        diccionario["thumbTemporal"] = ".thumbsTemporales/" + nombreDeThumb + ".jpg"

        self.listaDeReproduccionTemporal.append(diccionario)

    def agregarALista(self, link, titulo, thumbNumero):
        self.link = link

        itemDeLista = self.buscarEnlace()
        nuevoMedio = self.instancia.media_new("https" + itemDeLista[-1][:-1])
        self.listaDeReproduccion.add_media(nuevoMedio)

        #self.parent().parent().actualizarLista(self.listaDeReproduccion.count())

        # Para listas de reproducción
        nombreDeThumb = str(random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.ascii_lowercase))
        shutil.copy(".thumbs/" + str(thumbNumero) + ".jpg", ".thumbsTemporales/" + nombreDeThumb + ".jpg")

        # Diccionario
        diccionario = {}
        diccionario["titulo"] = titulo
        diccionario["thumbTemporal"] = ".thumbsTemporales/" + nombreDeThumb + ".jpg"

        self.listaDeReproduccionTemporal.append(diccionario)
        self.actualizarLista()

    def volumen(self, volumen):
        self.reproductor.audio_set_volume(volumen)

    def modoAleatorio(self):
        self.actualizarLista()

    def modoRepeticion(self):
        self.reproductorDeLista.set_playback_mode("loop")

    def cambiarTiempo(self, tiempo):
        self.reproductor.set_position(tiempo / 1000.0)

    def eventoMedioCambiado(self, evento):
        try:
            medioActual = self.reproductor.get_media()
            indiceDeMedioActual = self.listaDeReproduccion.index_of_item(medioActual)
            self.indiceDePista = indiceDeMedioActual
            self.actualizarLista()

            self.tituloWidget.setText(self.listaDeReproduccionTemporal[indiceDeMedioActual]["titulo"])
            self.dummyBoton.click()
        except:
            pass

    def actualizarLineaDeTiempo(self):
        self.lineaDeTiempoSlider.setValue(self.reproductor.get_position() * 1000)

    def actualizarLista(self):
        try:
            self.parent().parent().actualizarLista(self.listaDeReproduccionTemporal)
            self.parent().parent().actualizarIndiceDeLista(self.indiceDePista)
        except:
            print("Falló la actualización de la lista de Reproducción!")

    def reproducirCancionEn(self, indice):
        self.reproductorDeLista.play_item_at_index(indice)

    def actualizarEstilo(self):
        medioActual = self.reproductor.get_media()
        indiceDeMedioActual = self.listaDeReproduccion.index_of_item(medioActual)
        wallpaper = self.listaDeReproduccionTemporal[indiceDeMedioActual]["thumbTemporal"]
        self.setStyleSheet("background-image: url(" + wallpaper + "); background-position: left")
        QtGui.QApplication.processEvents()

    def eliminarPista(self, indice):
        del self.listaDeReproduccionTemporal[indice]