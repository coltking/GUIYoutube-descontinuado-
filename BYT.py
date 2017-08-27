# -*- encoding=utf-8 -*-
import subprocess
import sys
import os
import urllib.request as U
import urllib.parse
sys.path.append(os.getcwd() + "bs4")
sys.path.append(os.getcwd() + "youtube")
import bs4 as bs
from youtube_dl import YoutubeDL as YT


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
        self.lista = {}
        for i in range(len(self.duraciones)):
            tmp1 = "Titulo"+str(i)
            tmp2 = "ID"+str(i)
            tmp3 = "Duracion"+str(i)
            tmpPlayMPV = "PlayMPV"+str(i)
            tmpPlayVLC = "PlayVLC"+str(i)
            tmpDownload = "Descarga"+str(i)
            self.lista[tmp1] = self.titulos[i]
            self.lista[tmp2] = self.IDs[i]
            self.lista[tmp3] = self.duraciones[i]
            self.lista[tmpPlayMPV] = ["https://www.youtube.com/watch?v=" + self.IDs[i]]
            self.lista[tmpPlayVLC] = ["vlc","https://www.youtube.com/watch?v=" + self.IDs[i]]
            self.lista[tmpDownload] = ["https://www.youtube.com/watch?v=" + str(self.IDs[i])]
        # Este return deberia devolver el diccionario.
        return self.lista


    def descargarthumb(self):
        for i in range(0, len(self.duraciones)):
            U.urlretrieve( "http://img.youtube.com/vi/"+self.IDs[i]+"/mqdefault.jpg", ".thumbs/" + str(i) + ".jpg")

            #print("http://img.youtube.com/vi/"+self.IDs[i][9:]+"/mqdefault.jpg")
        # Esto de aqui ya esta demas. Lo dejo por si sirve de guia en el futuro.
        #for i in range(0, len(self.titulos)):
            #print("Video", str(i), ":", self.titulos[i], ". Duration:",
            #self.duraciones[i], "Mns. ID:", '"',
            #self.IDs[i], '".')


            #Lo que sigue a continuacion sirve unicamente para testeo de este script.
        #Para la version final ha de eliminarse/comentarse para que no interfiera.



if __name__ == "__main__":
    conn = BYT("hola mundo",10)
    hola = conn.obtenerDatos()
    subprocess.Popen(conn.lista["PlayVLC0"])



# Nuevo objeto BYT() - Toma dos parametros, terminoDeBusqueda y numeroDeResultados.
#nuevaBusqueda = BYT("Godot Engine", 2)
# Llamada al metodo obtenerDatos del objeto BYT()
#resultado = nuevaBusqueda.obtenerDatos()
# Print
#print(resultado)