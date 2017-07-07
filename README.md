# proyecto GUIYoutube

Este proyecto fue inicializado por ColTKinG (@JuanRosario en telegram) en plan de crear
una aplicacion de escritorio para buscar, ver, y descargar contenido de youtube...

El archivo sobre el que se va a trabajar es GUIYoutube.py ya que es el archivo que
tiene el codigo principal.

- Los widgets para cada entrada de video se crean con objetos instanciados de VideoWidget.py.
- Las consultas a la web y la construcción de enlaces se efectúan todos dentro del módulo BYT.py.
- Las miniaturas se almacenan en .thumbs.
- Las descargas irán a la carpeta "Descargas" (pendiente).

# Dependencias:

PyQt4
VLC o MPV para reproducción. youtube-dl para descargar.