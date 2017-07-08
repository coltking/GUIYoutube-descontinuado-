#! /usr/bin/env python3
# -*- encoding=utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
from urllib.request import urlretrieve
from glob import glob


# Importando clases propias

from VideoWidget import *
from BYT import *


class Ventana(QtGui.QMainWindow):

    def __init__(self):
        super(Ventana, self).__init__()
        self.ver = "0.1 Alpha"
        self.setWindowTitle("GUIYoutube - "+self.ver)
        self.setWindowIcon(QtGui.QIcon("Youtube.ico"))
        self.setGeometry(100, 100, 800, 500)
        self.cantidad = 5
        self.reproductorPreferido = "VLC"
        self.statusBar()

        self.páginaPrincipal()
        #self.poblarLista()

    def páginaPrincipal(self):

        # Barra de menu.
        self.menuBarra = self.menuBar()

        # Acciones.
        self.acciónLimpiar = QtGui.QAction("Limpiar cache de miniaturas", self)
        self.acciónLimpiar.setShortcut("Ctrl+Shift+L")
        self.acciónLimpiar.setStatusTip("Limpiar el directorio de thumbnails.")
        self.acciónLimpiar.triggered.connect(self.limpiarCache)

        self.acciónSalir = QtGui.QAction("Salir de la aplicación", self)
        self.acciónSalir.setShortcut("Ctrl+Shift+E")
        self.acciónSalir.setStatusTip("Salir de la aplicación.")
        self.acciónSalir.triggered.connect(self.salir)

        self.acciónAbout = QtGui.QAction("Acerca del proyecto GUIYoutube", self)
        self.acciónAbout.setStatusTip("Información sobre este proyecto.")

        self.acciónElegirCalidadDeVideo = QtGui.QAction("Elegir calidad de video", self)
        self.acciónElegirCalidadDeVideo.setStatusTip("Seleccionar la calidad por defecto de los videos buscados (No implementado aún).")

        self.acciónElegirCalidadDeAudio = QtGui.QAction("Elegir calidad de sonido", self)
        self.acciónElegirCalidadDeAudio.setStatusTip("Seleccionar la calidad por defecto del sonido en los videos buscados (No implementado aún).")

        # Menú "Archivo".
        self.menuArchivo = self.menuBarra.addMenu("Archivo")
        self.menuArchivo.addAction(self.acciónLimpiar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.acciónSalir)

        # Menú "Preferencias".
        self.menuPreferencias = self.menuBarra.addMenu("Preferencias")
        self.menuPreferencias.addAction(self.acciónElegirCalidadDeVideo)
        self.menuPreferencias.addAction(self.acciónElegirCalidadDeAudio)

        # Menú "About".
        self.menuAbout = self.menuBarra.addMenu("About")
        self.menuAbout.addAction(self.acciónAbout)

        # Widget y Layout para el centro de la ventana.
        self.widgetPrincipal = QtGui.QWidget(self)
        self.layoutPrincipal = QtGui.QGridLayout()
        self.widgetPrincipal.setLayout(self.layoutPrincipal)
        self.setCentralWidget(self.widgetPrincipal)

        # Scrolled area para la lista de videos.

        self.scroll = QtGui.QScrollArea(self)
        self.scroll.setWidgetResizable(True)
        self.scroll.setMinimumSize(550, 300)
        self.layoutPrincipal.addWidget(self.scroll, 0, 0, 6, 4)

        # LineEdit para el término de búsqueda.Ventana

        self.términoDeBúsqueda = QtGui.QLineEdit("Término de búsqueda", self)

        #usar Intro en el line edit por alguna razón no actualiza el label. Comentado por ahora.
        #self.términoDeBúsqueda.returnPressed.connect(self.consulta)

        self.layoutPrincipal.addWidget(self.términoDeBúsqueda, 0, 4, 1, 2)

        # Botón Buscar para búsqueda.

        self.buscarBtn = QtGui.QPushButton("Buscar en YT", self)
        self.layoutPrincipal.addWidget(self.buscarBtn, 1, 5, 1, -1)
        self.buscarBtn.pressed.connect(self.consulta)

        # Lista de opciones para número de búsquedas.

        self.listaDeOpciones = QtGui.QGroupBox("Selecciona la cantidad de videos a buscar:", self)
        self.listaLayout = QtGui.QVBoxLayout(self)

        self.layoutPrincipal.addWidget(self.listaDeOpciones, 3, 4, 1, 2)

        self.opción1 = QtGui.QRadioButton("1 video.", self)
        self.opción2 = QtGui.QRadioButton("5 videos.", self)
        self.opción2.setChecked(True)
        self.opción3 = QtGui.QRadioButton("10 videos.", self)
        self.opción4 = QtGui.QRadioButton("Primera página.", self)

        self.listaLayout.addWidget(self.opción1)
        self.listaLayout.addWidget(self.opción2)
        self.listaLayout.addWidget(self.opción3)
        self.listaLayout.addWidget(self.opción4)

        self.listaDeOpciones.setLayout(self.listaLayout)

        # Label para mostrar el progreso de las operaciones
        self.aviso = QtGui.QLabel(self)
        self.aviso.setAlignment(QtCore.Qt.AlignCenter)
        self.layoutPrincipal.addWidget(self.aviso, 2, 4, 1, 2)

        # Widget para el reproductor de video.


        # Pop-up para elegir reproductor.
        self.popup = QtGui.QMessageBox(self)
        self.popup.setText("Es necesario elegir un reproductor instalado antes de proceder.")
        self.VLCPlayer = self.popup.addButton("VLC Media Player", QtGui.QMessageBox.ActionRole)
        self.MPVPlayer = self.popup.addButton("MPV Media Player", QtGui.QMessageBox.ActionRole)
        self.popup.exec()
        if "VLC" in self.popup.clickedButton().text():
            self.reproductorPreferido = "VLC"
        if "MPV" in self.popup.clickedButton().text():
            self.reproductorPreferido = "MPV"

        self.show()

    def consulta(self):

        self.aviso.setText("Buscando videos en YouTube. \n Sólo tomará unos sengundos.")
        QtGui.QApplication.processEvents()

        if self.opción1.isChecked() == True:
            self.cantidad = 1
        if self.opción2.isChecked() == True:
            self.cantidad = 5
        if self.opción3.isChecked() == True:
            self.cantidad = 10
        if self.opción4.isChecked() == True:
            self.cantidad = 20

        término = self.términoDeBúsqueda.text()
        objetoBúsqueda = BYT(término, self.cantidad)
        self.resultados = objetoBúsqueda.obtenerDatos()

        self.poblarLista(self.resultados, self.cantidad)

    def poblarLista(self, resultados, cantidad):

        tempWidget = QtGui.QWidget(self)
        tempLayout = QtGui.QVBoxLayout(self)
        tempWidget.setLayout(tempLayout)

        for i in range(0, cantidad):
            videoBlock = VideoWidget(resultados["Título" + str(i)], i,
                                    resultados["Duración" + str(i)],
                                    resultados["PlayVLC" + str(i)],
                                    resultados["PlayMPV" + str(i)],
                                    resultados["Descarga" + str(i)],
                                    self.reproductorPreferido)
            tempLayout.addWidget(videoBlock)
            self.aviso.setText("")
        self.scroll.setWidget(tempWidget)

    def limpiarCache(self):
        os.chdir(".thumbs")
        thumbs = glob("*.jpg")
        for i in thumbs:
            os.remove(i)

    def salir(self):
        elección = QtGui.QMessageBox.question(self,
                                    "Saliendo de la aplicación.",
                                    "¿Está seguro que quiere salir?",
                                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if elección == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def sobreGUIYoutube(self):
        pass


def run():
    app = QtGui.QApplication(sys.argv)
    win = Ventana()
    sys.exit(app.exec_())

run()