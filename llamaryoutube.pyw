import sys
import os
import subprocess
import time
from youtube import *
from conexion import *

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
        conn = BYT(texto,5)
        hola = conn.obtenerDatos()
        for i in range(5):
            print(hola["Título"+str(i)])


        













if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MiFormulario()
    myapp.show()
    sys.exit(app.exec_())