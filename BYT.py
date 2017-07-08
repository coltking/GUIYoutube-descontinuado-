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

    def __init__(self, términoDeBúsqueda, númeroDeResultados):

        self.númeroDeParámetros = 3
        self.término = términoDeBúsqueda
        self.resultados = númeroDeResultados

        self.títulos = []
        self.IDs = []
        self.duraciones = []

        # Pequeño loop para armar el término de búsqueda.
        self.termSplit = self.término.split()
        self.termFull = ""
        for i in range(0, len(self.termSplit)):
            self.termFull= self.termFull + self.termSplit[i] + "+"

    def obtenerDatos(self):

        # Enconding link
        self.term = urllib.parse.quote(self.termFull)
        self.datos = U.urlopen("https://www.youtube.com/results?search_query=" + self.term)
        self.soup = bs.BeautifulSoup(self.datos, "html.parser")

        for i in self.soup.body.find_all("a", class_= "yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "):
            self.títulos.append(i.get("title"))
            self.IDs.append(i.get("href")[9:20])

        for i in self.soup.body.find_all("span", class_= "video-time"):
            self.duraciones.append(i.text)

        self.descargarthumb()

        #este for llena el diccionario
        self.lista = {}
        for i in range(len(self.duraciones)):
            tmp1 = "Título"+str(i)
            tmp2 = "ID"+str(i)
            tmp3 = "Duración"+str(i)
            tmpPlayMPV = "PlayMPV"+str(i)
            tmpPlayVLC = "PlayVLC"+str(i)
            tmpDownload = "Descarga"+str(i)
            self.lista[tmp1] = self.títulos[i]
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

            #print("http://img.youtube.com/vi/"+self.IDs[i][9:]+"/mqdefault.jpg")
        # Esto de aquí ya está demás. Lo dejo por si sirve de guía en el futuro.
        #for i in range(0, len(self.títulos)):
            #print("Video", str(i), ":", self.títulos[i], ". Duration:",
            #self.duraciones[i], "Mns. ID:", '"',
            #self.IDs[i], '".')


            #Lo que sigue a continuación sirve únicamente para testeo de este script.
        #Para la versión final ha de eliminarse/comentarse para que no interfiera.



if __name__ == "__main__":
    conn = BYT("hola mundo",10)
    hola = conn.obtenerDatos()
    subprocess.Popen(conn.lista["PlayVLC0"])



# Nuevo objeto BYT() - Toma dos parámetros, términoDeBúsqueda y númeroDeResultados.
#nuevaBúsqueda = BYT("Godot Engine", 2)
# Llamada al método obtenerDatos del objeto BYT()
#resultado = nuevaBúsqueda.obtenerDatos()
# Print
#print(resultado)