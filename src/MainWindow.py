# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Fri May 02 21:04:16 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from music21 import corpus, roman, key, environment
from transitions import *

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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(380, 333)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ChooseFile = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChooseFile.sizePolicy().hasHeightForWidth())
        self.ChooseFile.setSizePolicy(sizePolicy)
        self.ChooseFile.setObjectName(_fromUtf8("ChooseFile"))
        self.gridLayout.addWidget(self.ChooseFile, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QObject.connect(self.ChooseFile, QtCore.SIGNAL(_fromUtf8("clicked()")), self.update)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Chordial", None))
        self.ChooseFile.setText(_translate("mainWindow", "Choose File", None))

    
    def update(self):
        file_path = str(QtGui.QFileDialog.getOpenFileName())
        print file_path
        
        file_path = file_path.strip('\n')
        folder = file_path.split('/')
        
        file_name = folder[-1]
        folder = folder[0:-1]
        
        #print file_name
        #print folder
        
        folder_path = ""

        
        temp = 0
        for i in folder:
            if (temp != len(folder) - 1):
                folder_path  = str(folder_path) + i + '/'
            else:
                folder_path = str(folder_path) + i
            temp+=1
        
        print folder_path
        
        us = environment.UserSettings()
        us['localCorpusPath'] = folder_path      
        
        b = corpus.parse(file_name)
        b.show('text')
        
        bChords = b.chordify()
        
        #adds chordify as another voice to show better
        for c in bChords.flat:
            if 'Chord' not in c.classes:
                continue
            c.closedPosition(forceOctave=4, inPlace=True)
        
        #b.measures(0,2).show()
        
        stats = TransitionGraph()
        
        #adds roman numerals at the bottom
        for c in bChords.flat.getElementsByClass('Chord'):
            rn = roman.romanNumeralFromChord(c, key.Key('A'))
            stats.addNumeral(rn)
            c.addLyric(str(rn.figure))
        #bChords.measures(0, 2).show()
        bChords.show('text')
        
        
        
        #prints the roman numerals, i.e. lyrics
        for c in bChords.measures(0,2).flat:
            if 'Chord' not in c.classes:
                continue
            print c.lyric,
            
        print "\n"
        stats.printTransitions()        
