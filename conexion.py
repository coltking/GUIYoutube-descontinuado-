# -*- encoding=utf-8 -*-
import subprocess
import youtube


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
                miembros.append(str(línea))

            for i in range(0, len(miembros)):
                if len(miembros[i]) > 5:
                    limpio.append(miembros[i][2:-3])

        for i in range(0, len(limpio), self.númeroDeParámetros):
            self.títulos.append(limpio[i])
        for i in range(1, len(limpio), self.númeroDeParámetros):
            self.IDs.append(limpio[i])
        for i in range(2, len(limpio), self.númeroDeParámetros):
            self.duraciones.append(limpio[i])

        # Esto de aquí ya está demás. Lo dejo por si sirve de guía en el futuro.
        #for i in range(0, len(self.títulos)):
            #print("Video", str(i), ":", self.títulos[i], ". Duration:",
            #self.duraciones[i], "Mns. ID:", '"',
            #self.IDs[i], '".')


            #Lo que sigue a continuación sirve únicamente para testeo de este script.
        #Para la versión final ha de eliminarse/comentarse para que no interfiera.

        self.lista = []
        self.lista.append(self.títulos)
        self.lista.append(self.IDs)
        self.lista.append(self.duraciones)
        # Este return debería devolver el diccionario.
        return self.lista

# Nuevo objeto BYT() - Toma dos parámetros, términoDeBúsqueda y númeroDeResultados.
nuevaBúsqueda = BYT("Godot Engine", 2)
# Llamada al método obtenerDatos del objeto BYT()
resultado = nuevaBúsqueda.obtenerDatos()
# Print
print(resultado)