# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1121, 874)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Youtube.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Youtube.ico")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(1.0)
        self.Button1 = QtGui.QPushButton(Dialog)
        self.Button1.setGeometry(QtCore.QRect(0, 0, 171, 141))
        self.Button1.setAutoFillBackground(False)
        self.Button1.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Youtube.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button1.setIcon(icon1)
        self.Button1.setIconSize(QtCore.QSize(160, 140))
        self.Button1.setObjectName(_fromUtf8("Button1"))
        self.Button2 = QtGui.QPushButton(Dialog)
        self.Button2.setGeometry(QtCore.QRect(0, 140, 171, 141))
        self.Button2.setText(_fromUtf8(""))
        self.Button2.setIcon(icon1)
        self.Button2.setIconSize(QtCore.QSize(160, 140))
        self.Button2.setObjectName(_fromUtf8("Button2"))
        self.Button3 = QtGui.QPushButton(Dialog)
        self.Button3.setGeometry(QtCore.QRect(0, 280, 171, 141))
        self.Button3.setText(_fromUtf8(""))
        self.Button3.setIcon(icon1)
        self.Button3.setIconSize(QtCore.QSize(160, 140))
        self.Button3.setObjectName(_fromUtf8("Button3"))
        self.Button4 = QtGui.QPushButton(Dialog)
        self.Button4.setGeometry(QtCore.QRect(0, 420, 171, 141))
        self.Button4.setText(_fromUtf8(""))
        self.Button4.setIcon(icon1)
        self.Button4.setIconSize(QtCore.QSize(160, 140))
        self.Button4.setObjectName(_fromUtf8("Button4"))
        self.Button5 = QtGui.QPushButton(Dialog)
        self.Button5.setGeometry(QtCore.QRect(0, 560, 171, 141))
        self.Button5.setText(_fromUtf8(""))
        self.Button5.setIcon(icon1)
        self.Button5.setIconSize(QtCore.QSize(160, 140))
        self.Button5.setObjectName(_fromUtf8("Button5"))
        self.label1 = QtGui.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(170, 20, 411, 91))
        self.label1.setText(_fromUtf8(""))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.label2 = QtGui.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(170, 160, 411, 91))
        self.label2.setText(_fromUtf8(""))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.label3 = QtGui.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(170, 300, 411, 91))
        self.label3.setText(_fromUtf8(""))
        self.label3.setObjectName(_fromUtf8("label3"))
        self.label4 = QtGui.QLabel(Dialog)
        self.label4.setGeometry(QtCore.QRect(170, 440, 411, 91))
        self.label4.setText(_fromUtf8(""))
        self.label4.setObjectName(_fromUtf8("label4"))
        self.label5 = QtGui.QLabel(Dialog)
        self.label5.setGeometry(QtCore.QRect(170, 590, 411, 91))
        self.label5.setText(_fromUtf8(""))
        self.label5.setObjectName(_fromUtf8("label5"))
        self.labelBuscar = QtGui.QLabel(Dialog)
        self.labelBuscar.setGeometry(QtCore.QRect(840, 20, 59, 18))
        self.labelBuscar.setObjectName(_fromUtf8("labelBuscar"))
        self.lineBuscar = QtGui.QLineEdit(Dialog)
        self.lineBuscar.setGeometry(QtCore.QRect(890, 10, 231, 32))
        self.lineBuscar.setObjectName(_fromUtf8("lineBuscar"))
        self.ButtonBuscar = QtGui.QPushButton(Dialog)
        self.ButtonBuscar.setGeometry(QtCore.QRect(970, 50, 88, 34))
        self.ButtonBuscar.setObjectName(_fromUtf8("ButtonBuscar"))
        self.ButtonDescargar1 = QtGui.QPushButton(Dialog)
        self.ButtonDescargar1.setGeometry(QtCore.QRect(600, 50, 88, 34))
        self.ButtonDescargar1.setObjectName(_fromUtf8("ButtonDescargar1"))
        self.ButtonDescargar2 = QtGui.QPushButton(Dialog)
        self.ButtonDescargar2.setGeometry(QtCore.QRect(600, 190, 88, 34))
        self.ButtonDescargar2.setObjectName(_fromUtf8("ButtonDescargar2"))
        self.ButtonDescargar3 = QtGui.QPushButton(Dialog)
        self.ButtonDescargar3.setGeometry(QtCore.QRect(600, 330, 88, 34))
        self.ButtonDescargar3.setObjectName(_fromUtf8("ButtonDescargar3"))
        self.ButtonDescargar4 = QtGui.QPushButton(Dialog)
        self.ButtonDescargar4.setGeometry(QtCore.QRect(600, 470, 88, 34))
        self.ButtonDescargar4.setObjectName(_fromUtf8("ButtonDescargar4"))
        self.ButtonDescargar5 = QtGui.QPushButton(Dialog)
        self.ButtonDescargar5.setGeometry(QtCore.QRect(600, 610, 88, 34))
        self.ButtonDescargar5.setObjectName(_fromUtf8("ButtonDescargar5"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 730, 1101, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLineWidth(4)
        self.label.setText(_fromUtf8(""))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName(_fromUtf8("label"))
        self.label1.setBuddy(self.Button1)
        self.label2.setBuddy(self.Button2)
        self.label3.setBuddy(self.Button3)
        self.label4.setBuddy(self.Button4)
        self.label5.setBuddy(self.Button5)
        self.labelBuscar.setBuddy(self.lineBuscar)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.lineBuscar, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.ButtonBuscar.click)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "GUIYoutube", None))
        self.labelBuscar.setText(_translate("Dialog", "B&uscar", None))
        self.ButtonBuscar.setText(_translate("Dialog", "Buscar", None))
        self.ButtonDescargar1.setText(_translate("Dialog", "Descargar", None))
        self.ButtonDescargar2.setText(_translate("Dialog", "Descargar", None))
        self.ButtonDescargar3.setText(_translate("Dialog", "Descargar", None))
        self.ButtonDescargar4.setText(_translate("Dialog", "Descargar", None))
        self.ButtonDescargar5.setText(_translate("Dialog", "Descargar", None))

