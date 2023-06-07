import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QTabWidget, QApplication, QLabel, \
    QGridLayout, QPushButton
from interfaz_principal import Ventana3
from datos import Ventana6

class Ventana2 (QMainWindow):

    def __init__(self, anterior, nombre_usuario):
        super(Ventana2, self).__init__(anterior)

        self.nombreUsuario = nombre_usuario
        self.setWindowTitle("HELP TRAINING")
        self.setWindowIcon(QIcon("imagenes/img_1.png"))
        self.setStyleSheet("background-color: black;")
        self.ancho = 1000
        self.alto = 600
        self.resize(self.ancho, self.alto)

        #aparece la ventana centrada
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.interna = QWidget()
        self.interna.setContentsMargins(50, 60, 50, 50)

        self.setCentralWidget(self.interna)
        self.vertical = QVBoxLayout()

        self.cuadricula = QGridLayout()
        self.interna.setLayout(self.cuadricula)

        self.cuadricula.addWidget(QLabel(""), 0, 0)

        self.cuadricula.addWidget(QLabel(""), 0, 2)

        self.label = QLabel("¡Bienvenido " + self.nombreUsuario + "!")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: black; color: white; font-size: 30px; font-family: Poppins; font-weight: bold;")
        self.cuadricula.addWidget(self.label, 0, 1)

        self.frases = [
            "La fuerza no viene de una capacidad física.\n "
            "    Viene de una voluntad indomable. \n"
            "                                -Mahatma Gandhi",
            "  No puedes poner un limite a nada. \n"
            "mientras mas sueñas, mas lejos llegas \n "
            "                                -Michael Phelps",
            "La motivacion es lo que te pone en marcha,\n"
            "  y el habito es lo que hace que sigas. \n "
            "                                 -Robert Collier",
            "Lo que no te mata, te hace más fuerte. \n"
            "                                 -Friedrich Nietzsche"
        ]
        self.frases_aleatorias = random.choice(self.frases)
        self.label = QLabel(self.frases_aleatorias)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: black; color: white; font-size: 18px; font-family: Poppins;")
        self.cuadricula.addWidget(self.label, 2, 1)

        self.imagen = QLabel()
        self.imagen.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/img_1.png")
        self.imagen.setFixedSize(300, 236)
        self.imagen.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagen, 1, 1)


        self.botoninicio = QPushButton("Comenzar")
        self.botoninicio.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")

        self.botoninicio.clicked.connect(self.comenzar)
        self.cuadricula.setAlignment(Qt.AlignCenter)

        self.cuadricula.addWidget(self.botoninicio, 3, 1)

    def comenzar(self):
        self.interfaz_principal = Ventana3(self, self.nombreUsuario)
        self.interfaz_principal.show()
        self.hide()