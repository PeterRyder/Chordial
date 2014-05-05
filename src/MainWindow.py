# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon May 05 17:10:07 2014
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
        mainWindow.resize(935, 693)
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
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 834, 632))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 21))
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
            
            folder_path = ""
            
            work_name = file_name.split('.')
            work_name = work_name[0]
            print "work name: " + work_name
    
            
            temp = 0
            for i in folder:
                if (temp != len(folder) - 1):
                    folder_path  = str(folder_path) + i + '\\'
                else:
                    folder_path = str(folder_path) + i
                temp+=1
            
            
            print "Analyzing " + file_name
            print "File located here: " + folder_path       
            print ""
            
            corpus.addPath(folder_path)
            paths = corpus.getPaths()
            for i in paths:
                print i
            
            print corpus.getWork(work_name)
            b = corpus.parse(work_name)
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
                rn = roman.romanNumeralFromChord(c, key.Key('C'))
                stats.addNumeral(rn)
                c.addLyric(str(rn.figure))
            #bChords.measures(0, 2).show()
            #bChords.show('text')
            
            
            
            #prints the roman numerals, i.e. lyrics
            for c in bChords.measures(0,2).flat:
                if 'Chord' not in c.classes:
                    continue
                print c.lyric,
                
            print "\n"
            output = stats.getTransitions()
            
            stats.printTransitions()
            print ""
            stats.printTransInOrder()
            
            self.label1 = QtGui.QLabel(self.scrollAreaWidgetContents)
            self.label1.setObjectName(_fromUtf8("label1"))
            self.gridLayout_2.addWidget(self.label1, 0, 0, 1, 1)  
            self.label1.setText(_translate("mainWindow", stats.getTransInOrder(), None)) 
            
            temp = 1
            for i in output:
                
                
                self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
                self.label.setObjectName(_fromUtf8("label"))
                self.gridLayout_2.addWidget(self.label, temp, 0, 1, 1)
                self.label.setText(_translate("mainWindow", i[0] + "->" + i[1] + " : " + str(output[i]), None))    
                temp += 1

