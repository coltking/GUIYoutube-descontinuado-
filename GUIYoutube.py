#! /usr/bin/env python3
# -*- encoding=utf-8 -*-

from PyQt4 import QtGui, QtCore
import os
import sys
from urllib.request import urlretrieve


# Importando clases propias

from VideoWidget import *
from BYT import *
from BLista import *
from youtube_dl import YoutubeDL as YT
from ReproductorDeMusica import reproductorDeMusica as RM


class Ventana(QtGui.QMainWindow):


    def __init__(self):
        super(Ventana, self).__init__()
        self.ver = "0.2 Alpha"
        self.setWindowTitle("GUIYoutube - "+self.ver)
        self.setWindowIcon(QtGui.QIcon("Youtube.ico"))
        self.setGeometry(100, 100, 1000, 500)
        self.setMaximumSize(1200, 670)
        self.cantidad = 5
        self.reproductorPreferido = "VLC"
        self.statusBar()
        self.statusBar().setStyleSheet("background-color:grey")
        self.setObjectName("Ventana Principal")

        self.reproductor = ""
        self.reproductorActivo = False
        self.indiceDePista = 0

        self.format = ""
        self.preferedformat = ""
        self.link = ""
        self.resultados = ""
        self.cantidad = ""

        self.paginaPrincipal()
        #self.poblarLista()

    def paginaPrincipal(self):

        # Barra de menu.
        self.menuBarra = self.menuBar()

        # Acciones.
        self.accionLimpiar = QtGui.QAction("Limpiar cache de miniaturas", self)
        self.accionLimpiar.setShortcut("Ctrl+Shift+L")
        self.accionLimpiar.setStatusTip("Limpiar el directorio de thumbnails. (Deshabilitado)")
        #self.accionLimpiar.triggered.connect(self.limpiarCache)

        self.accionSalir = QtGui.QAction("Salir de la aplicacion", self)
        self.accionSalir.setShortcut("Ctrl+Shift+E")
        self.accionSalir.setStatusTip("Salir de la aplicacion.")
        self.accionSalir.triggered.connect(self.salir)

        self.accionDescargarPorLink = QtGui.QAction("Descargar con link", self)
        self.accionDescargarPorLink.setShortcut("Ctrl+Shift+D")
        self.accionDescargarPorLink.triggered.connect(self.descargaporlinkparametros)

        self.accionAbout = QtGui.QAction("Acerca del proyecto GUIYoutube", self)
        self.accionAbout.setStatusTip("Informacion sobre este proyecto.")

        self.accionElegirCalidadDeVideo = QtGui.QAction("Elegir calidad de video", self)
        self.accionElegirCalidadDeVideo.setStatusTip("Seleccionar la calidad por defecto de los videos buscados (No implementado aún).")

        self.accionElegirCalidadDeAudio = QtGui.QAction("Elegir calidad de sonido", self)
        self.accionElegirCalidadDeAudio.setStatusTip("Seleccionar la calidad por defecto del sonido en los videos buscados (No implementado aún).")

        # Menú "Archivo".
        self.menuArchivo = self.menuBarra.addMenu("Archivo")
        self.menuArchivo.addAction(self.accionLimpiar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.accionSalir)

        # Menú "Preferencias".
        self.menuPreferencias = self.menuBarra.addMenu("Preferencias")
        self.menuPreferencias.addAction(self.accionElegirCalidadDeVideo)
        self.menuPreferencias.addAction(self.accionElegirCalidadDeAudio)

        # Menú "Herramientas".
        self.menuHerramientas = self.menuBarra.addMenu("Herramientas")
        self.menuHerramientas.addAction(self.accionDescargarPorLink)

        # Menú "About".
        self.menuAbout = self.menuBarra.addMenu("About")
        self.menuAbout.addAction(self.accionAbout)

        # Widget y Layout para el centro de la ventana.
        self.widgetPrincipal = QtGui.QWidget(self)
        self.widgetPrincipal.setMinimumSize(950, 500)
        self.layoutPrincipal = QtGui.QGridLayout(self)
        self.widgetPrincipal.setLayout(self.layoutPrincipal)
        self.setCentralWidget(self.widgetPrincipal)

        # Dummy para actualizar indice en la lista de reproducción
        self.dummy = QtGui.QPushButton(self)
        self.dummy.clicked.connect(self.actualizarIndiceSeleccionado)

        self.layoutPrincipal.addWidget(self.dummy, 1, 1, 1, 1)

        # Scrolled area para la lista de videos.

        self.scroll = QtGui.QScrollArea(self)
        self.scroll.setWidgetResizable(True)
        self.scroll.setMinimumWidth(600)
        self.layoutPrincipal.addWidget(self.scroll, 0, 0, 7, 4)

        # Scrolled are para la lista de reproducción
        self.listaScroll = QtGui.QScrollArea(self)
        self.listaScroll.setWidgetResizable(True)

        self.layoutPrincipal.addWidget(self.listaScroll, 5, 4, 1, 2)
        self.listaScroll.hide()

        # ListWidget para la lista de reproducción
        self.listaList = QtGui.QListWidget(self)
        self.listaList.itemDoubleClicked.connect(self.pistaActivada)

        self.listaScroll.setWidget(self.listaList)
        # LineEdit para el término de búsqueda.Ventana

        self.terminoDeBusqueda = QtGui.QLineEdit(self)
        self.terminoDeBusqueda.setPlaceholderText("Ingrese el término de búsqueda.")
        self.terminoDeBusqueda.returnPressed.connect(self.consulta)

        self.layoutPrincipal.addWidget(self.terminoDeBusqueda, 0, 4, 1, 2)

        # Boton Buscar para búsqueda.

        self.buscarBtn = QtGui.QPushButton("Buscar en YT", self)
        self.layoutPrincipal.addWidget(self.buscarBtn, 1, 5, 1, 1)
        self.buscarBtn.pressed.connect(self.consulta)

        # Boton para descargar por link

        self.descargarLinkBtn = QtGui.QPushButton("Descargar con link", self)
        self.layoutPrincipal.addWidget(self.descargarLinkBtn, 1, 4, 1, 1)
        self.descargarLinkBtn.pressed.connect(self.descargaporlinkparametros)

        # Lista de opciones para número de búsquedas.

        self.listaDeOpciones = QtGui.QGroupBox("Selecciona la cantidad de videos a buscar:", self)
        self.listaLayout = QtGui.QGridLayout(self)

        self.layoutPrincipal.addWidget(self.listaDeOpciones, 3, 4, 2, 2)

        self.opcion1 = QtGui.QRadioButton("1 video.", self)
        self.opcion2 = QtGui.QRadioButton("5 videos.", self)
        self.opcion2.setChecked(True)
        self.opcion3 = QtGui.QRadioButton("10 videos.", self)
        self.opcion4 = QtGui.QRadioButton("Primera página.", self)

        self.listaLayout.addWidget(self.opcion1, 0, 0, 1, 1)
        self.listaLayout.addWidget(self.opcion2, 0, 1, 1, 1)
        self.listaLayout.addWidget(self.opcion3, 1, 0, 1, 1)
        self.listaLayout.addWidget(self.opcion4, 1, 1, 1, 1)

        self.listaDeOpciones.setLayout(self.listaLayout)

        # Lista de Opciones para calidad de descargas.

        self.widgetCalidad = QtGui.QGroupBox(self)
        self.widgetCalidad.hide()
        self.layoutCalidad = QtGui.QGridLayout(self)
        self.layoutCalidad.setRowMinimumHeight(6, 20)
        self.layoutCalidad.setRowMinimumHeight(2, 20)
        self.widgetCalidad.setLayout(self.layoutCalidad)

        # Etiquetas para calidad de descarga

        self.etiquetaMp3 = QtGui.QLabel("Elija la calidad del archivo de audio:")
        self.etiquetaMp4 = QtGui.QLabel("Elija la calidad del archivo de video:")

        # Botones para Mp3

        self.calidad1 = QtGui.QPushButton("Más baja", self)
        self.calidad1.setCheckable(True)
        self.calidad1.clicked.connect(self.revisarCalidad1)

        self.calidad2 = QtGui.QPushButton("Más alta", self)
        self.calidad2.setCheckable(True)
        self.calidad2.clicked.connect(self.revisarCalidad2)

        # Botones para Mp4

        self.calidad240 = QtGui.QPushButton("240p", self)
        self.calidad240.setCheckable(True)
        self.calidad240.clicked.connect(self.revisar240)

        self.calidad480 = QtGui.QPushButton("480p", self)
        self.calidad480.setCheckable(True)
        self.calidad480.clicked.connect(self.revisar480)

        self.calidad720 = QtGui.QPushButton("720p", self)
        self.calidad720.setCheckable(True)
        self.calidad720.clicked.connect(self.revisar720)

        self.calidad1080 = QtGui.QPushButton("1080p", self)
        self.calidad1080.setCheckable(True)
        self.calidad1080.clicked.connect(self.revisar1080)

        # Boton de descarga

        self.botonDescarga = QtGui.QPushButton("Descargar", self)
        self.botonDescarga.clicked.connect(self.seleccionDeCantidad)

        # Agregando widgets al layout

        self.layoutCalidad.addWidget(self.etiquetaMp3, 0, 0, 1, 2)
        self.layoutCalidad.addWidget(self.calidad1, 1, 0, 1, 1)
        self.layoutCalidad.addWidget(self.calidad2, 1, 1, 1, 1)

        self.layoutCalidad.addWidget(self.etiquetaMp4, 3, 0, 1, 2)
        self.layoutCalidad.addWidget(self.calidad240, 4, 0, 1, 1)
        self.layoutCalidad.addWidget(self.calidad480, 4, 1, 1, 1)
        self.layoutCalidad.addWidget(self.calidad720, 5, 0, 1, 1)
        self.layoutCalidad.addWidget(self.calidad1080, 5, 1, 1, 1)

        self.layoutCalidad.addWidget(self.botonDescarga, 7, 0, 1, 2)

        self.layoutPrincipal.addWidget(self.widgetCalidad, 3, 4, 1, 2)

        # Label para mostrar el progreso de las operaciones
        self.aviso = QtGui.QLabel(self)
        self.aviso.setAlignment(QtCore.Qt.AlignCenter)
        self.layoutPrincipal.addWidget(self.aviso, 2, 4, 1, 2)

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
        self.limpiarThumbsTemporales()

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

    def consulta(self):

        self.aviso.setText("Buscando videos en YouTube. \n Solo tomará unos sengundos.")
        QtGui.QApplication.processEvents()
        # Es necesario duplicar las ordenes para que se actualice el label de aviso
        # de búsqueda cuando se usa enter, sino no responde.
        self.aviso.setText("Buscando videos en YouTube. \n Solo tomará unos sengundos.")
        QtGui.QApplication.processEvents()

        if self.opcion1.isChecked() == True:
            self.cantidad = 1
        if self.opcion2.isChecked() == True:
            self.cantidad = 5
        if self.opcion3.isChecked() == True:
            self.cantidad = 10
        if self.opcion4.isChecked() == True:
            self.cantidad = 20

        # Búsqueda de videos en listas de reproducción.
        if "//www.youtube.com/playlist" in self.terminoDeBusqueda.text():
            nuevaBusqueda = BusquedaDeLista()
            self.resultados = nuevaBusqueda.obtenerDatos(self.terminoDeBusqueda.text())

         #Búsqueda por térmio de búsqueda
        else:
            termino = self.terminoDeBusqueda.text()
            objetoBusqueda = BYT(termino, self.cantidad)
            self.resultados = objetoBusqueda.obtenerDatos()

        self.poblarLista(self.resultados, self.cantidad)

    def descargaporlinkparametros(self):
        if "//www.youtube.com/watch" in self.terminoDeBusqueda.text():
            self.listaDeOpciones.hide()
            self.widgetCalidad.show()
            self.link = self.terminoDeBusqueda.text()
        else:
            self.popup = QtGui.QMessageBox.information(self, "Informacion", """No ha ingresado una url valida""",QtGui.QMessageBox.Ok)


    def descargarPorLink(self):
        ydl_opts = {
                    'format': self.format,
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': self.preferedformat
                        }]
                    }
        with YT(ydl_opts) as yt:
            homedir = os.getenv("HOME")
            exdir = os.getcwd() #exdir es el directorio actual, se guarda para saber donde volver una vez completada la descarga
            #print(exdir)
            if not os.path.exists(homedir+ "/Descargas/GUIYoutube"): os.makedirs(homedir+"/Descargas/GUIYoutube")
            os.chdir(homedir+"/Descargas/GUIYoutube")
            #print(os.getcwd())
            yt.download([self.link])
            os.chdir(exdir)
            #self.popup = QtGui.QMessageBox.information(self, "Informacion", """Descarga finalizada (revise la carpeta Descargas)""",QtGui.QMessageBox.Ok)
            subprocess.Popen(["notify-send", "-t","4000", "Descarga finalizada (revise su carpeta de descargas)"])

    def poblarLista(self, resultados, cantidad):
        tempWidget = QtGui.QWidget(self)
        tempLayout = QtGui.QVBoxLayout(self)
        tempWidget.setLayout(tempLayout)

        for i in range(0, cantidad):
            videoBlock = VideoWidget(resultados[i]["Título"],
                                        i,
                                    resultados[i]["Duración"],
                                    resultados[i]["PlayVLC"],
                                    resultados[i]["PlayMPV"],
                                    resultados[i]["Descarga"],
                                    self.reproductorPreferido)
            tempLayout.addWidget(videoBlock)
            self.aviso.setText("")
        if self.reproductorActivo:
            self.scrollPequeno.setWidget(tempWidget)
        else:
            self.scroll.setWidget(tempWidget)

    def limpiarCache(self):
        os.chdir(".thumbs")
        thumbs = os.listdir()
        for i in thumbs:
            if i.endswith(".jpg"):
                os.remove(i)

    def salir(self):
        eleccion = QtGui.QMessageBox.question(self,
                                    "Saliendo de la aplicacion.",
                                    "¿Está seguro que quiere salir?",
                                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if eleccion == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def sobreGUIYoutube(self):
        pass

    def revisarCalidad1(self):
        self.calidad2.setChecked(False)
        self.format = "worstaudio"
        self.preferedformat = "mp3"

    def revisarCalidad2(self):
        self.calidad1.setChecked(False)
        self.format = "bestaudio"
        self.preferedformat = "mp3"

    def revisar240(self):
        self.calidad480.setChecked(False)
        self.calidad720.setChecked(False)
        self.calidad1080.setChecked(False)
        self.format = "bestvideo[height=240]+bestaudio"
        self.preferedformat = "mp4"

    def revisar480(self):
        self.calidad240.setChecked(False)
        self.calidad720.setChecked(False)
        self.calidad1080.setChecked(False)
        self.format = "bestvideo[height=480]+bestaudio"
        self.preferedformat = "mp4"

    def revisar720(self):
        self.calidad480.setChecked(False)
        self.calidad240.setChecked(False)
        self.calidad1080.setChecked(False)
        self.format = "bestvideo[height=720]+bestaudio"
        self.preferedformat = "mp4"

    def revisar1080(self):
        self.calidad480.setChecked(False)
        self.calidad720.setChecked(False)
        self.calidad240.setChecked(False)
        self.format = "bestvideo[height=1080]+bestaudio"
        self.preferedformat = "mp4"

    def seleccionDeCalidad(self):
        self.listaDeOpciones.hide()
        self.widgetCalidad.show()

    def seleccionDeCantidad(self):
        if self.format != "" or self.preferedformat != "":
            self.descargarPorLink()
            self.link = ""
            self.format = ""
            self.preferedformat = ""
            self.widgetCalidad.hide()
            self.listaDeOpciones.show()
        else:
            self.popup = QtGui.QMessageBox.information(self, "Informacion", """No se ha seleccionado una calidad de audio/video""",QtGui.QMessageBox.Ok)

    def crearReproductorDeMusica(self, descarga, thumbNumero, titulo):
        if not self.reproductorActivo:
            self.statusBar().showMessage("Creando reproductor y medios de audio")
            self.reproductor = RM(descarga, thumbNumero, titulo)

            self.reproductorActivo = True
            self.reconstruirScrolledArea()

            # Reproductor
            self.layoutPrincipal.addWidget(self.reproductor, 5, 0, 2, 4)
            self.listaScroll.show()

            QtGui.QApplication.processEvents()
            self.reproductor.construirMedio()
            self.statusBar().showMessage("")

            # Botones para lista de reproducción
            self.botonBorrar = QtGui.QPushButton("Eliminar", self)
            self.botonBorrar.clicked.connect(self.eliminarPista)
            self.botonGuardar = QtGui.QPushButton("Guardar Lista", self)

            self.botoneraLayout = QtGui.QHBoxLayout(self)
            self.botoneraLayout.addWidget(self.botonBorrar)
            self.botoneraLayout.addWidget(self.botonGuardar)

            self.layoutPrincipal.addLayout(self.botoneraLayout, 6, 4, 1, 1)

        elif self.reproductorActivo:
            self.statusBar().showMessage("Cambiando de medio de reproduccion", 2000)
            QtGui.QApplication.processEvents()
            hayMedioNuevo = self.reproductor.cambiarMedio(descarga, thumbNumero, titulo)


    def reconstruirScrolledArea(self):
        # Se elimina el scrolled area original.
        self.scroll.hide()

        # Nuevo y más pequeño scrolled area.
        self.scrollPequeno = QtGui.QScrollArea(self)
        self.scrollPequeno.setWidgetResizable(True)
        self.scrollPequeno.setMinimumWidth(600)
        self.layoutPrincipal.addWidget(self.scrollPequeno, 0, 0, 5, 4)

        # Recreando los widgets de video
        self.poblarLista(self.resultados, self.cantidad)

    def destruirReproductorDeMusica(self):
        self.reproductorActivo = False
        # Se elimina el scrolled area pequeno
        self.scrollPequeno.hide()
        self.reproductor.hide()

        # Se restaura el scrolled grande
        self.scroll.show()

        # Recreando widgets de video
        self.poblarLista(self.resultados, self.cantidad)

    def agregarALista(self, link, titulo, thumbNumero):
        self.reproductor.agregarALista(link, titulo, thumbNumero)

    def actualizarLista(self, lista):
        self.listaList.clear()
        for i in range(0, len(lista)):
            itemDeLista = QtGui.QListWidgetItem()
            itemDeLista.setText(lista[i]["titulo"])

            self.listaList.insertItem(i, itemDeLista)

    def actualizarIndiceDeLista(self, indice):
        self.indiceDePista = indice
        self.dummy.click()

    def actualizarIndiceSeleccionado(self):
        item = self.listaList.item(self.indiceDePista)
        self.listaList.setItemSelected(item, True)

    def limpiarThumbsTemporales(self):
        dir = os.path.join(os.getcwd(), ".thumbsTemporales")
        archivos = os.listdir(dir)
        for archivo in archivos:
            if archivo.endswith(".jpg"):
                os.remove(os.path.join(dir, archivo))

    def pistaActivada(self, item):
        indice = self.listaList.row(item)
        self.reproductor.reproducirCancionEn(indice)

    def eliminarPista(self):
        pista = self.listaList.currentRow()
        self.listaList.takeItem(pista)

        self.reproductor.eliminarPista(pista)

def run():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_X11InitThreads)
    app = QtGui.QApplication(sys.argv)
    win = Ventana()
    sys.exit(app.exec_())

run()
