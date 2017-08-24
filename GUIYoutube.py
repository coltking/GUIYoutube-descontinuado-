#! /usr/bin/env python3
# -*- encoding=utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
from urllib.request import urlretrieve
from glob import glob


# Importando clases propias

from VideoWidget import *
from BYT import *
from youtube_dl import YoutubeDL as YT
from ReproductorDeMusica import reproductorDeMusica as RM


class Ventana(QtGui.QMainWindow):


    def __init__(self):
        super(Ventana, self).__init__()
        self.ver = "0.1 Alpha"
        self.setWindowTitle("GUIYoutube - "+self.ver)
        self.setWindowIcon(QtGui.QIcon("Youtube.ico"))
        self.setGeometry(100, 100, 1000, 500)
        self.cantidad = 5
        self.reproductorPreferido = "VLC"
        self.statusBar()
        self.setObjectName("Ventana Principal")

        self.reproductor = ""
        self.reproductorActivo = False

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
        self.acciónLimpiar = QtGui.QAction("Limpiar cache de miniaturas", self)
        self.acciónLimpiar.setShortcut("Ctrl+Shift+L")
        self.acciónLimpiar.setStatusTip("Limpiar el directorio de thumbnails.")
        self.acciónLimpiar.triggered.connect(self.limpiarCache)

        self.acciónSalir = QtGui.QAction("Salir de la aplicación", self)
        self.acciónSalir.setShortcut("Ctrl+Shift+E")
        self.acciónSalir.setStatusTip("Salir de la aplicación.")
        self.acciónSalir.triggered.connect(self.salir)

        self.acciónDescargarPorLink = QtGui.QAction("Descargar con link", self)
        self.acciónDescargarPorLink.setShortcut("Ctrl+Shift+D")
        self.acciónDescargarPorLink.triggered.connect(self.descargaporlinkparametros)

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

        # Menú "Herramientas".
        self.menuHerramientas = self.menuBarra.addMenu("Herramientas")
        self.menuHerramientas.addAction(self.acciónDescargarPorLink)

        # Menú "About".
        self.menuAbout = self.menuBarra.addMenu("About")
        self.menuAbout.addAction(self.acciónAbout)

        # Widget y Layout para el centro de la ventana.
        self.widgetPrincipal = QtGui.QWidget(self)
        self.widgetPrincipal.setMinimumSize(950, 500)
        self.layoutPrincipal = QtGui.QGridLayout(self)
        self.widgetPrincipal.setLayout(self.layoutPrincipal)
        self.setCentralWidget(self.widgetPrincipal)

        # Scrolled area para la lista de videos.

        self.scroll = QtGui.QScrollArea(self)
        self.scroll.setWidgetResizable(True)
        self.scroll.setMinimumSize(570, 100)
        self.layoutPrincipal.addWidget(self.scroll, 0, 0, 6, 4)

        # LineEdit para el término de búsqueda.Ventana

        self.términoDeBúsqueda = QtGui.QLineEdit(self)
        self.términoDeBúsqueda.setPlaceholderText("Ingrese el término de búsqueda.")
        self.términoDeBúsqueda.returnPressed.connect(self.consulta)

        self.layoutPrincipal.addWidget(self.términoDeBúsqueda, 0, 4, 1, 2)

        # Botón Buscar para búsqueda.

        self.buscarBtn = QtGui.QPushButton("Buscar en YT", self)
        self.layoutPrincipal.addWidget(self.buscarBtn, 1, 5, 1, 1)
        self.buscarBtn.pressed.connect(self.consulta)

        # Botón para descargar por link

        self.descargarLinkBtn = QtGui.QPushButton("Descargar con link",self)
        self.layoutPrincipal.addWidget(self.descargarLinkBtn,1,4,1,1)
        self.descargarLinkBtn.pressed.connect(self.descargaporlinkparametros)

        # Lista de opciones para número de búsquedas.

        self.listaDeOpciones = QtGui.QGroupBox("Selecciona la cantidad de videos a buscar:", self)
        self.listaLayout = QtGui.QVBoxLayout(self)

        self.layoutPrincipal.addWidget(self.listaDeOpciones, 3, 4, 2, 2)

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

        # Botón de descarga

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

        self.layoutPrincipal.addWidget(self.widgetCalidad, 3, 4, 2, 2)

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

        self.aviso.setText("Buscando videos en YouTube. \n Sólo tomará unos sengundos.")
        QtGui.QApplication.processEvents()
        # Es necesario duplicar las órdenes para que se actualice el label de aviso
        # de búsqueda cuando se usa enter, sino no responde.
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

    def descargaporlinkparametros(self):
        if "//www.youtube.com/watch" in self.términoDeBúsqueda.text():
            self.listaDeOpciones.hide()
            self.widgetCalidad.show()
            self.link = self.términoDeBúsqueda.text()
        else:
            self.popup = QtGui.QMessageBox.information(self, "Informacion", """No ha ingresado una url valida""",QtGui.QMessageBox.Ok)

    #def descargaporlinkparametros(self):
        #tmp = QtGui.QInputDialog.getText(self, 'GUIYoutube', 'Ingrese link:')
        #if tmp[1]:
        	#self.listaDeOpciones.hide()
        	#self.widgetCalidad.show()
        	#self.link = tmp[0]
        #else:
        	#pass


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
            subprocess.Popen(["notify-send", "-t","4000", "\"Descarga finalizada (revise su carpeta de descargas)\""])


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
        if self.reproductorActivo:
            self.scrollPequeno.setWidget(tempWidget)
        else:
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
            self.reproductor = RM(descarga, thumbNumero, titulo)

            if not self.reproductorActivo:
                self.reproductorActivo = True
                self.reconstruirScrolledArea()

            self.layoutPrincipal.addWidget(self.reproductor, 3, 0, 2, 6)

        elif self.reproductorActivo:
            self.reproductor.cambiarMedio(descarga, thumbNumero, titulo)

    def reconstruirScrolledArea(self):
        # Se elimina el scrolled area original.
        self.layoutPrincipal.removeWidget(self.scroll)
        self.scroll.hide()

        # Nuevo y más pequeño scrolled area.
        self.scrollPequeno = QtGui.QScrollArea(self)
        self.scrollPequeno.setWidgetResizable(True)
        self.scrollPequeno.setMinimumSize(570, 100)
        self.layoutPrincipal.addWidget(self.scrollPequeno, 0, 0, 3, 4)

        # Recreando los widgets de video
        self.poblarLista(self.resultados, self.cantidad)



    #def printerFunc(self):
        #print("Yay!!...You've hit the sweet spot!!!!!!")



def run():
    app = QtGui.QApplication(sys.argv)
    win = Ventana()
    sys.exit(app.exec_())

run()
