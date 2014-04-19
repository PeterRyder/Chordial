# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Thu Apr 17 03:16:32 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from QArrow import *

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(False)
        MainWindow.resize(1600, 900)
        MainWindow.setMouseTracking(False)
        self.Main = QtGui.QWidget(MainWindow)
        self.Main.setStyleSheet(_fromUtf8("background-image: background.jpg;"))
        self.Main.setObjectName(_fromUtf8("Main"))
        self.arrow = QArrow(3,MainWindow)
        self.arrow.setGeometry(QtCore.QRect(150, 150, 50, 50))
        #self.arrow.rotate(45)
        self.I = QtGui.QFrame(self.Main)
        self.I.setGeometry(QtCore.QRect(40, 460, 150, 150))
        self.I.setAutoFillBackground(False)
        self.I.setStyleSheet(_fromUtf8("background-color:red;border-radius:10px;"))
        self.I.setFrameShape(QtGui.QFrame.StyledPanel)
        self.I.setFrameShadow(QtGui.QFrame.Raised)
        self.I.setObjectName(_fromUtf8("I"))
        self.II = QtGui.QFrame(self.Main)
        self.II.setGeometry(QtCore.QRect(1040, 670, 150, 150))
        self.II.setAutoFillBackground(False)
        self.II.setStyleSheet(_fromUtf8("background-color:red;border-radius:10px;"))
        self.II.setFrameShape(QtGui.QFrame.StyledPanel)
        self.II.setFrameShadow(QtGui.QFrame.Raised)
        self.II.setObjectName(_fromUtf8("II"))
        self.III = QtGui.QFrame(self.Main)
        self.III.setGeometry(QtCore.QRect(370, 80, 150, 150))
        self.III.setAutoFillBackground(False)
        self.III.setStyleSheet(_fromUtf8("background-color:red;border-radius:10px;"))
        self.III.setFrameShape(QtGui.QFrame.StyledPanel)
        self.III.setFrameShadow(QtGui.QFrame.Raised)
        self.III.setObjectName(_fromUtf8("III"))
        self.Block3 = QtGui.QTextEdit(self.III)
        self.Block3.setGeometry(QtCore.QRect(25, 25, 100, 100))
        self.Block3.setAutoFillBackground(False)
        self.Block3.setStyleSheet(_fromUtf8("color:black;"))
        self.Block3.setObjectName(_fromUtf8("Block3"))
        self.IV = QtGui.QFrame(self.Main)
        self.IV.setGeometry(QtCore.QRect(940, 380, 150, 150))
        self.IV.setAutoFillBackground(False)
        self.IV.setStyleSheet(_fromUtf8("background-color:red;border-radius:10px;"))
        self.IV.setFrameShape(QtGui.QFrame.StyledPanel)
        self.IV.setFrameShadow(QtGui.QFrame.Raised)
        self.IV.setObjectName(_fromUtf8("IV"))
        self.G = QtGui.QFrame(self.Main)
        self.G.setGeometry(QtCore.QRect(480, 660, 150, 150))
        self.G.setAutoFillBackground(False)
        self.G.setStyleSheet(_fromUtf8("background-color:red;border-radius:10px;"))
        self.G.setFrameShape(QtGui.QFrame.StyledPanel)
        self.G.setFrameShadow(QtGui.QFrame.Raised)
        self.G.setObjectName(_fromUtf8("G"))
        self.VI = QtGui.QFrame(self.Main)
        self.VI.setGeometry(QtCore.QRect(590, 300, 150, 150))
        self.VI.setAutoFillBackground(False)
        self.VI.setStyleSheet(_fromUtf8("background-color:red;border-radius:10px;"))
        self.VI.setFrameShape(QtGui.QFrame.StyledPanel)
        self.VI.setFrameShadow(QtGui.QFrame.Raised)
        self.VI.setObjectName(_fromUtf8("VI"))
        self.VII = QtGui.QFrame(self.Main)
        self.VII.setGeometry(QtCore.QRect(1050, 50, 150, 150))
        self.VII.setAutoFillBackground(False)
        self.VII.setStyleSheet(_fromUtf8("background-color:red;border-radius:10px;"))
        self.VII.setFrameShape(QtGui.QFrame.StyledPanel)
        self.VII.setFrameShadow(QtGui.QFrame.Raised)
        self.VII.setObjectName(_fromUtf8("VII"))
        self.V = QtGui.QFrame(self.Main)
        self.V.setGeometry(QtCore.QRect(1430, 440, 150, 150))
        self.V.setAutoFillBackground(False)
        self.V.setStyleSheet(_fromUtf8("background-color:red;border-radius:10px;"))
        self.V.setFrameShape(QtGui.QFrame.StyledPanel)
        self.V.setFrameShadow(QtGui.QFrame.Raised)
        self.V.setObjectName(_fromUtf8("V"))
        MainWindow.setCentralWidget(self.Main)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #MainWindow.setTabOrder(MainWindow.Block3_2, self.Block3)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.I.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>I</p></body></html>", None))
        self.II.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>I</p></body></html>", None))
        self.III.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>I</p></body></html>", None))
        self.Block3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">III</span></p></body></html>", None))
        self.IV.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>I</p></body></html>", None))
        self.G.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>I</p></body></html>", None))
        self.VI.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>I</p></body></html>", None))
        self.VII.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>I</p></body></html>", None))
        self.V.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>I</p></body></html>", None))

