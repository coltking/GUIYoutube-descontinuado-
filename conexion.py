import subprocess
#import re

class Conexion():
    def __init__(self,RESULTADOS, STRING):
        self.numberOfParameters = 3
        self.string = STRING
        self.resultados = RESULTADOS
        self.titles = []
        self.IDs = []
        self.duration = []

    def obtenerDatos(self):
        

        with subprocess.Popen('youtube-dl \"ytsearch'+str(self.resultados)+':'+self.string+'\" --get-id --get-title --get-duration', stdout=subprocess.PIPE, shell=True) as process:
            members = []
            clean = []
            while process.poll() is None:
                results = process.stdout.readline()
                members.append(str(results))

            for i in range(0, len(members)):
                if len(members[i]) > 5:
                    clean.append(members[i][2:-3])

        for i in range(0, len(clean), self.numberOfParameters):
            self.titles.append(clean[i])
        for i in range(1, len(clean), self.numberOfParameters):
            self.IDs.append(clean[i])
        for i in range(2, len(clean), self.numberOfParameters):
            self.duration.append(clean[i])

        #print(titles, "\n", IDs, "\n", duration)

        for i in range(0, len(self.titles)):
            print("Video", str(i), ":", self.titles[i], ". Duration:", self.duration[i], "Mns. ID:", '"', self.IDs[i], '".')