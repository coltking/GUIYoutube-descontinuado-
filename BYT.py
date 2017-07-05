# -*- encoding=utf-8 -*-
import subprocess
import youtube
import urllib.request


class BYT():

    def __init__(self, términoDeBúsqueda, númeroDeResultados):

        self.númeroDeParámetros = 3
        self.término = términoDeBúsqueda
        self.resultados = númeroDeResultados

        self.títulos = []
        self.IDs = []
        self.duraciones = []

    def obtenerDatos(self):

        comandoDeBúsqueda = 'youtube-dl \"ytsearch'+str(self.resultados)+':'+self.término+'\" --get-id --get-title --get-duration'
        with subprocess.Popen(comandoDeBúsqueda, stdout=subprocess.PIPE, shell=True) as proceso:

            miembros = []
            limpio = []

            while proceso.poll() is None:
                línea = proceso.stdout.readline()
                miembros.append(línea.decode())

            for i in range(0, len(miembros)):
                if len(miembros[i]) > 3:
                    limpio.append(miembros[i][0:-1])

        for i in range(0, len(limpio), self.númeroDeParámetros):
            self.títulos.append(limpio[i])
        for i in range(1, len(limpio), self.númeroDeParámetros):
            self.IDs.append(limpio[i])
        for i in range(2, len(limpio), self.númeroDeParámetros):
            self.duraciones.append(limpio[i])
        self.descargarThumb()

        #este for llena el diccionario
        self.lista = {}
        for i in range(0, len(self.IDs)):
            tmp1 = "Título"+str(i)
            tmp2 = "ID"+str(i)
            tmp3 = "Duración"+str(i)
            self.lista[tmp1] = self.títulos[i]
            self.lista[tmp2] = self.IDs[i]
            self.lista[tmp3] = self.duraciones[i]
        # Este return debería devolver el diccionario.
        return self.lista


    def descargarThumb(self):
        for i in range(self.resultados):
            url = "http://img.youtube.com/vi/"+self.IDs[i]+"/mqdefault.jpg"
            urllib.request.urlretrieve(url, "thumbs/" + str(i) + ".jpg")
            print(url)

        # Esto de aquí ya está demás. Lo dejo por si sirve de guía en el futuro.
        #for i in range(0, len(self.títulos)):
            #print("Video", str(i), ":", self.títulos[i], ". Duration:",
            #self.duraciones[i], "Mns. ID:", '"',
            #self.IDs[i], '".')


            #Lo que sigue a continuación sirve únicamente para testeo de este script.
        #Para la versión final ha de eliminarse/comentarse para que no interfiera.



if __name__ == "__main__":
    conn = BYT("hola mundo",5)
    hola = conn.obtenerDatos()
    print(conn.lista.get("Título0"))



# Nuevo objeto BYT() - Toma dos parámetros, términoDeBúsqueda y númeroDeResultados.
#nuevaBúsqueda = BYT("Godot Engine", 2)
# Llamada al método obtenerDatos del objeto BYT()
#resultado = nuevaBúsqueda.obtenerDatos()
# Print
#print(resultado)