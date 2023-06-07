from PyQt5.QtGui import QIcon, QFontDatabase, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QGridLayout
from PyQt5 import QtWidgets

class Acercade(QMainWindow):
    def __init__(self, anterior):
        super(Acercade, self).__init__(anterior)

        self.ventanaAnterior = anterior

        self.setWindowTitle("HELP TRAINING")
        self.setWindowIcon(QIcon("imagenes/img_1.png"))
        self.setStyleSheet("background-color: black;")
        self.ancho = 600
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        QFontDatabase.addApplicationFont("fonts/Poppins-ExtraLight.ttf")
        self.letra1 = QFont()
        self.letra1.setFamily("Poppins")
        self.letra1.setPointSize(25)

        self.interna = QWidget()
        self.interna.setContentsMargins(50, 50, 50, 50)

        self.setCentralWidget(self.interna)
        self.vertical = QVBoxLayout()

        self.cuadricula = QGridLayout()
        self.interna.setLayout(self.cuadricula)

        self.volver_button = QtWidgets.QPushButton('Volver')
        self.volver_button.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.volver_button.clicked.connect(self.volver)
        self.cuadricula.addWidget(self.volver_button, 4, 0, 2, 4)


    def volver(self):
        self.hide()
        self.ventanaAnterior.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    acercade = Acercade()
    acercade.show()
    app.exec_()