import math
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFormLayout, QApplication, QLineEdit, QDialog, \
    QDialogButtonBox, QVBoxLayout, QPushButton, QWidget, QButtonGroup, QScrollArea, QGridLayout


class Ventana7_1(QMainWindow):

    def __init__(self,anterior):
        super(Ventana7_1, self).__init__(anterior)
        self.ventanaAnterior = anterior


        self.setWindowTitle("HELP TRAINING")
        self.setWindowIcon(QIcon("imagenes/img_1.png"))
        self.setStyleSheet("background-color: black;")

        self.ancho = 1000
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.interna = QWidget()
        self.interna.setContentsMargins(50, 50, 50, 50)

        self.setCentralWidget(self.interna)

        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("Ejercicios")

        self.letrero1.setFont(QFont("Poppins", 25))

        self.letrero1.setAlignment(Qt.AlignCenter)

        self.letrero1.setStyleSheet("color: white; font-size: 25px; font-family: Poppins;")

        self.vertical.addWidget(self.letrero1)

        self.vertical.addStretch()

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.volver)
        self.vertical.addWidget(self.botonVolver)

        self.vertical.addStretch()
        self.interna.setLayout(self.vertical)


    def volver(self):
        self.hide()
        self.ventanaAnterior.show()