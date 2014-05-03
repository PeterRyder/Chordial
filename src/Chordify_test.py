from music21 import corpus, roman, key
from transitions import *
from os import path

import sys
from PyQt4.QtGui import QApplication, QDialog, QMainWindow
from MainWindow import Ui_mainWindow
from sip import *

def main():
    app = QApplication(sys.argv)
    window = QDialog()
    mainmenu = QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainmenu)
    
    mainmenu.show()
    sys.exit(app.exec_())
    
    
if __name__ == "__main__":
    main()


