import sys
import os
import subprocess
import time
from youtube import *
from urllib.request import urlretrieve
from PIL import Image


class MiFormulario(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)




        QtCore.QObject.connect(self.ui.ButtonBuscar, QtCore.SIGNAL('clicked()'),self.cargardatos)
        QtCore.QObject.connect(self.ui.Button1, QtCore.SIGNAL('clicked()'), self.play1)
        QtCore.QObject.connect(self.ui.Button2, QtCore.SIGNAL('clicked()'), self.play2)
        QtCore.QObject.connect(self.ui.Button3, QtCore.SIGNAL('clicked()'), self.play3)
        QtCore.QObject.connect(self.ui.Button4, QtCore.SIGNAL('clicked()'), self.play4)
        QtCore.QObject.connect(self.ui.Button5, QtCore.SIGNAL('clicked()'), self.play5)
        QtCore.QObject.connect(self.ui.ButtonDescargar1, QtCore.SIGNAL('clicked()'),self.descargar1)







    def descargar1(self):

        self.ui.label.setText("Descarga iniciada, Espere por favor...")
        time.sleep(1)

        ########################### LECTURA DE ID
        file = open('id.txt', 'r')
        cadena = file.readline()
        temp = len(cadena)
        id1 = cadena[:temp - 1]
        file.close()
        ########################### FIN LECTURA ID


        ########################### LECTURA DE NOMBRE
        file = open('nombre.txt', 'r')
        cadena = file.readline()
        temp = len(cadena)
        nombre1 = cadena[:temp - 1]
        file.close()
        ########################### FIN LECTURA NOMBRE



        ########################### Ejecucion de comando y logeo...
        hola = subprocess.Popen('youtube-dl https://www.youtube.com/watch?v='+id1, shell=True,
                                stdout=subprocess.PIPE)
        while hola.poll() is None:
            output = hola.stdout.readline()
            self.ui.label.setText("Descarga Completa:\n"+nombre1)
        ########################### FIN Ejecucion de comando y logeo...




    def descargar2(self):


        ########################### LECTURA DE ID
        file = open('id.txt', 'r')
        cadena = file.readline()
        cadena = file.readline()
        temp = len(cadena)
        id1 = cadena[:temp - 1]
        file.close()
        ########################### FIN LECTURA ID


        ########################### LECTURA DE NOMBRE
        file = open('nombre.txt', 'r')
        cadena = file.readline()
        cadena = file.readline()
        temp = len(cadena)
        nombre1 = cadena[:temp - 1]
        file.close()
        ########################### FIN LECTURA NOMBRE

        self.ui.label.setText("Descarga iniciada, Espere por favor...")

        ########################### Ejecucion de comando y logeo...
        hola = subprocess.Popen('youtube-dl https://www.youtube.com/watch?v='+id1, shell=True,
                                stdout=subprocess.PIPE)
        while hola.poll() is None:
            output = hola.stdout.readline()
            self.ui.label.setText("Descarga Completa:\n"+nombre1)
        ########################### FIN Ejecucion de comando y logeo...



    def descargar3(self):

        self.ui.label.setText("Descarga iniciada, Espere por favor...")
        ########################### LECTURA DE ID
        file = open('id.txt', 'r')
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        temp = len(cadena)
        id1 = cadena[:temp - 1]
        file.close()
        ########################### FIN LECTURA ID


        ########################### LECTURA DE NOMBRE
        file = open('nombre.txt', 'r')
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        temp = len(cadena)
        nombre1 = cadena[:temp - 1]
        file.close()
        ########################### FIN LECTURA NOMBRE



        ########################### Ejecucion de comando y logeo...
        hola = subprocess.Popen('youtube-dl https://www.youtube.com/watch?v='+id1, shell=True,
                                stdout=subprocess.PIPE)
        while hola.poll() is None:
            output = hola.stdout.readline()
            self.ui.label.setText("Descarga Completa:\n"+nombre1)
        ########################### FIN Ejecucion de comando y logeo...

    def descargar4(self):

        self.ui.label.setText("Descarga iniciada, Espere por favor...")
        ########################### LECTURA DE ID
        file = open('id.txt', 'r')
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        temp = len(cadena)
        id1 = cadena[:temp - 1]
        file.close()
        ########################### FIN LECTURA ID


        ########################### LECTURA DE NOMBRE
        file = open('nombre.txt', 'r')
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        temp = len(cadena)
        nombre1 = cadena[:temp - 1]
        file.close()
        ########################### FIN LECTURA NOMBRE



        ########################### Ejecucion de comando y logeo...
        hola = subprocess.Popen('youtube-dl https://www.youtube.com/watch?v=' + id1, shell=True,
                                stdout=subprocess.PIPE)
        while hola.poll() is None:
            output = hola.stdout.readline()
            self.ui.label.setText("Descarga Completa:\n" + nombre1)
            ########################### FIN Ejecucion de comando y logeo...


    def descargar5(self):

        self.ui.label.setText("Descarga iniciada, Espere por favor...")
        ########################### LECTURA DE ID
        file = open('id.txt', 'r')
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        temp = len(cadena)
        id1 = cadena[:temp - 1]
        file.close()
        ########################### FIN LECTURA ID


        ########################### LECTURA DE NOMBRE
        file = open('nombre.txt', 'r')
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        temp = len(cadena)
        nombre1 = cadena[:temp - 1]
        file.close()
        ########################### FIN LECTURA NOMBRE



        ########################### Ejecucion de comando y logeo...
        hola = subprocess.Popen('youtube-dl https://www.youtube.com/watch?v=' + id1, shell=True,
                                stdout=subprocess.PIPE)
        while hola.poll() is None:
            output = hola.stdout.readline()
            self.ui.label.setText("Descarga Completa:\n" + nombre1)
            ########################### FIN Ejecucion de comando y logeo...



    def play1(self):
        file = open('id.txt','r')
        cadena = file.readline()
        temp = len(cadena)
        id1 = cadena[:temp -1]
        file.close()
        link = "https://www.youtube.com/watch?v="+id1
        os.system("mpv youtube-dl "+link)

    def play2(self):
        file = open('id.txt','r')
        cadena = file.readline()
        cadena = file.readline()
        temp = len(cadena)
        id1 = cadena[:temp -1]
        file.close()
        link = "https://www.youtube.com/watch?v="+id1
        os.system("mpv youtube-dl "+link)

    def play3(self):
        file = open('id.txt','r')
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        temp = len(cadena)
        id1 = cadena[:temp -1]
        link = "https://www.youtube.com/watch?v="+id1
        os.system("mpv youtube-dl "+link)

    def play4(self):
        file = open('id.txt','r')
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        temp = len(cadena)
        id1 = cadena[:temp -1]
        file.close()
        link = "https://www.youtube.com/watch?v="+id1
        os.system("mpv youtube-dl "+link)

    def play5(self):
        file = open('id.txt','r')
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        cadena = file.readline()
        temp = len(cadena)
        id1 = cadena[:temp -1]
        file.close()
        link = "https://www.youtube.com/watch?v="+id1
        os.system("mpv youtube-dl "+link)


    def cargardatos(self):
        #self.ui = Ui_Dialog()
        #self.ui.setupUi(self)
        if len(self.ui.lineBuscar.text()) != 0:
            texto = self.ui.lineBuscar.text()
        else:
            texto = "we are number one"
        ids = "youtube-dl \"ytsearch5:"+texto+"\" --get-id > id.txt"
        nombre = "youtube-dl \"ytsearch5:"+texto+"\" --get-title > nombre.txt"
        os.system(str(ids))
        os.system(str(nombre))

        file = open('nombre.txt', 'r')
        nombre1 = file.readline()
        nombre2 = file.readline()
        nombre3 = file.readline()
        nombre4 = file.readline()
        nombre5 = file.readline()
        file.close()
        self.ui.label1.setText(nombre1)
        self.ui.label2.setText(nombre2)
        self.ui.label3.setText(nombre3)
        self.ui.label4.setText(nombre4)
        self.ui.label5.setText(nombre5)
        file = open('id.txt', 'r')
        cadena = file.readline()
        temp = len(cadena)
        id1 = cadena[:temp -1]
        thumb = urlretrieve("https://img.youtube.com/vi/" + id1 + "/maxresdefault.jpg", "thumb_01.ico")
        thumb = Image.open("thumb_01.jpg")
        #os.system("wget https://img.youtube.com/vi/"+id1+"/maxresdefault.jpg -O 1.jpg")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap.load(thumb)
        self.ui.Button1.setIcon(icon1)

        cadena2 = file.readline()
        temp = len(cadena2)
        id2 = cadena2[:temp -1]
        os.system("wget https://img.youtube.com/vi/" + id2 + "/maxresdefault.jpg -O 2.jpg")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("2.jpg"))
        self.ui.Button2.setIcon(icon2)

        cadena3 = file.readline()
        temp = len(cadena3)
        id3 = cadena3[:temp -1]
        os.system("wget https://img.youtube.com/vi/" + id3 + "/maxresdefault.jpg -O 3.jpg")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("3.jpg"))
        self.ui.Button3.setIcon(icon3)

        cadena4 = file.readline()
        temp = len(cadena4)
        id4 = cadena4[:temp - 1]
        os.system("wget https://img.youtube.com/vi/" + id4 + "/maxresdefault.jpg -O 4.jpg")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("4.jpg"))
        self.ui.Button4.setIcon(icon4)

        cadena5 = file.readline()
        temp = len(cadena5)
        id5 = cadena5[:temp - 1]
        os.system("wget https://img.youtube.com/vi/" + id5 + "/maxresdefault.jpg -O 5.jpg")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("5.jpg"))
        self.ui.Button5.setIcon(icon5)
        file.close()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MiFormulario()
    myapp.show()
    sys.exit(app.exec_())