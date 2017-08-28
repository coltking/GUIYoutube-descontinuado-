# -*- encoding=utf-8 -*-

import urllib.request as U

class BusquedaDeLista():

    def __init__(self, datos, step):
        self.datos = datos
        self.numeroDeParametros = step

        self.titulos = []
        self.IDs = []
        self.duraciones = []

    def obtenerDatos(self):
        for i in range(0, len(self.datos), self.numeroDeParametros):
            if len(self.datos[i]) > 2:
                self.titulos.append(self.datos[i])

        for j in range(1, len(self.datos), self.numeroDeParametros):
            self.IDs.append(self.datos[j])

        for k in range(2, len(self.datos), self.numeroDeParametros):
            self.duraciones.append(self.datos[k])

        self.descargarthumb()

        #este for llena el diccionario
        self.lista = {}

        for i in range(0, len(self.duraciones)):
            tmp1 = "Titulo" + str(i)
            tmp2 = "ID" + str(i)
            tmp3 = "Duracion" + str(i)
            tmpPlayMPV = "PlayMPV" + str(i)
            tmpPlayVLC = "PlayVLC" + str(i)
            tmpDownload = "Descarga" + str(i)

            self.lista[tmp1] = self.titulos[i]
            self.lista[tmp2] = self.IDs[i]
            self.lista[tmp3] = self.duraciones[i]
            self.lista[tmpPlayMPV] = ["https://www.youtube.com/watch?v=" + self.IDs[i]]
            self.lista[tmpPlayVLC] = ["vlc","https://www.youtube.com/watch?v=" + self.IDs[i]]
            self.lista[tmpDownload] = ["https://www.youtube.com/watch?v=" + str(self.IDs[i])]

        # Este return debería devolver el diccionario.
        return self.lista

    def descargarthumb(self):
        for i in range(0, len(self.duraciones)):
            U.urlretrieve( "http://img.youtube.com/vi/"+self.IDs[i]+"/mqdefault.jpg", ".thumbs/" + str(i) + ".jpg")