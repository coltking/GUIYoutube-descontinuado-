# -*- encoding=utf-8 -*-

import urllib.request as U
import requests
import os
import sys
import time
sys.path.append(os.getcwd() + "bs4")
import bs4 as bs

class BusquedaDeLista():

    def __init__(self, datos=None, step=None):
        self.datos = datos
        self.numeroDeParametros = step

        self.titulos = []
        self.IDs = []
        self.duraciones = []

    def obtenerDatos(self, enlace):
        #userAgent = "Mozilla/5.0 Firefox/55.0"
        r = requests.get(enlace).content
        # Soup
        soup = bs.BeautifulSoup(r, "html.parser")

        for i in soup.body.table.find_all("tr", class_="pl-video yt-uix-tile "):
            self.titulos.append(i.get("data-title"))
            self.IDs.append(i.get("data-video-id"))

            for x in i.find("td", class_="pl-video-time"):
                self.duraciones.append(x.text[1:-1])

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