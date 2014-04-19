import sys
from PyQt4.QtGui import QApplication, QMainWindow, QWidget
from PyQt4 import QtCore
from Gui import Ui_MainWindow
from QArrow import QArrow

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowFlags(window.windowFlags() | QtCore.Qt.FramelessWindowHint)
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())