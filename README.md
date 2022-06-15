# proyecto GUIYoutube

Este proyecto fue inicializado en plan de aprender a desarrollar una GUI (Graphical User Interface) en python con PyQT
la idea es lograr una aplicacion de escritorio para buscar, ver, y descargar contenido de YouTube de forma nativa en sistemas que soporten QT y python.

El archivo sobre el que se va a trabajar es GUIYoutube.py, ya que es el archivo que
tiene el código principal.

- Los widgets para cada entrada de video se crean con objetos instanciados de VideoWidget.py.
- Las consultas a la web y la construcción de enlaces se efectúan todos dentro del módulo BYT.py.
- Las miniaturas se almacenan en .thumbs.
- Las descargas terminan en la carpeta "Descargas".

# Dependencias:

- Qt4. 
- PyQt4. 
- VLC o MPV para reproducción.
