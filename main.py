import sys
from ejemplo_ui import *

from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindowController(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSumar.clicked.connect(self.sumar)
        self.ui.btnRestar.clicked.connect(self.restar)

    def sumar(self):
        num1 = int(self.ui.txtNum1.toPlainText())
        num2 = int(self.ui.txtNum2.toPlainText())
        suma = num1 + num2
        self.ui.label.setText(f'La suma es: {suma}')

    def restar(self):
        num1 = int(self.ui.txtNum1.toPlainText())
        num2 = int(self.ui.txtNum2.toPlainText())
        resta= num1 - num2
        self.ui.label.setText(f'La resta es: {resta}')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindowController()
    MainWindow.show()
    sys.exit(app.exec_())