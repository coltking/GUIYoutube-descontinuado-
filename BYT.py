# -*- encoding=utf-8 -*-
import subprocess
import sys
import os
import urllib.request as U
import urllib.parse
path = os.path.abspath(os.path.join(os.getcwd(), "lib"))
sys.path.append(path)
sys.path.append(os.getcwd() + "bs4")
import bs4 as bs


class BYT():

    def __init__(self, terminoDeBusqueda, numeroDeResultados):

        self.numeroDeParametros = 3
        self.termino = terminoDeBusqueda
        self.resultados = numeroDeResultados

        self.titulos = []
        self.IDs = []
        self.duraciones = []

        # Pequeño loop para armar el termino de busqueda.
        self.termSplit = self.termino.split()
        self.termFull = ""
        for i in range(0, len(self.termSplit)):
            self.termFull= self.termFull + self.termSplit[i] + "+"

    def obtenerDatos(self):

        # Enconding link
        self.term = urllib.parse.quote(self.termFull)
        self.datos = U.urlopen("https://www.youtube.com/results?search_query=" + self.term)
        self.soup = bs.BeautifulSoup(self.datos, "html.parser")

        for i in self.soup.body.find_all("a", class_= "yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "):
            self.titulos.append(i.get("title"))
            self.IDs.append(i.get("href")[9:20])

        for i in self.soup.body.find_all("span", class_= "video-time"):
            self.duraciones.append(i.text)

        self.descargarthumb()

        #este for llena el diccionario
        #
        #IMPORTANTE: Ahora se retorna una lista de diccionarios en vez de
        #un sólo diccionario enorme.
        #
        self.lista = []

        for i in range(0, len(self.duraciones)):
            self.dict = {}
            self.dict["Título"] = self.titulos[i]
            self.dict["ID"] = self.IDs[i]
            self.dict["Duración"] = self.duraciones[i]
            self.dict["PlayMPV"] = ["https://www.youtube.com/watch?v=" + self.IDs[i]]
            self.dict["PlayVLC"] = ["vlc","https://www.youtube.com/watch?v=" + self.IDs[i]]
            self.dict["Descarga"] = ["https://www.youtube.com/watch?v=" + str(self.IDs[i])]

            self.lista.append(self.dict)

        # Este return debería devolver el diccionario.
        return self.lista

    def descargarthumb(self):
        for i in range(0, len(self.duraciones)):
            U.urlretrieve( "http://img.youtube.com/vi/"+self.IDs[i]+"/mqdefault.jpg", ".thumbs/" + str(i) + ".jpg")