import math
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFormLayout, QApplication, QLineEdit, QDialog, \
    QDialogButtonBox, QVBoxLayout, QPushButton, QWidget, QButtonGroup, QScrollArea, QGridLayout

from lista_ejercicio import Ventana7_1


class Ventana5(QMainWindow):

    def __init__(self,anterior):
        super(Ventana5, self).__init__(anterior)
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

        self.letrero1.setText("Menú de ejercicios")

        self.letrero1.setFont(QFont("Poppins", 25))

        self.letrero1.setAlignment(Qt.AlignCenter)

        self.letrero1.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; font-weight: bold;")

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

        self.scrollArea = QScrollArea()

        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()

        self.cuadricula = QGridLayout(self.contenedora)
        self.scrollArea.setWidget(self.contenedora)
        self.vertical.addWidget(self.scrollArea)

        self.numeroElementos = 4

        self.contador = 0

        self.elementosPorColumna = 4

        self.numeroFilas = math.ceil(self.numeroElementos / self.elementosPorColumna)

        self.interna.setLayout(self.vertical)

        self.botones = QButtonGroup()

        self.botones.setExclusive(False)

        self.listamusculos = ["Pierna", "Abdomen", "Biceps", "Pecho"]
        self.imagenesmusculos = ['imagenes/pierna.png','imagenes/abdomen.png', 'imagenes/biceps.png', 'imagenes/pecho.png']



        for fila in range(1, self.numeroFilas + 1):
            for columna in range(1, self.elementosPorColumna + 1):
                if self.contador < self.numeroElementos:
                    self.ventanaAux = QWidget()
                    self.ventanaAux.setFixedHeight(200)
                    self.ventanaAux.setFixedWidth(200)

                    self.verticalCuadricula = QVBoxLayout()

                    self.labelImagen = QLabel()
                    self.labelImagen.setFixedWidth(130)
                    self.labelImagen.setFixedHeight(130)
                    self.imagen = QPixmap(self.imagenesmusculos[self.contador])
                    self.labelImagen.setPixmap(self.imagen)
                    self.labelImagen.setScaledContents(True)

                    self.verticalCuadricula.addWidget(self.labelImagen)

                    self.verticalCuadricula.addStretch()

                    self.labelNombre = QLabel('Ejercicio ' + str(self.contador + 1))

                    self.labelNombre.setStyleSheet("color: white; font-size: 15px; font-family: Poppins;")

                    self.verticalCuadricula.addWidget(self.labelNombre)

                    self.verticalCuadricula.addStretch()

                    self.botonAccion = QPushButton(self.listamusculos[self.contador])

                    self.botonAccion.setStyleSheet(
                        "color: white; font-size: 15px; font-family: Poppins; padding: 5px; border-radius:5px; "
                        "border: 1px solid #FFFFFF; ")

                    self.botonAccion.setFixedWidth(150)

                    self.verticalCuadricula.addWidget(self.botonAccion)

                    self.botones.addButton(self.botonAccion, self.contador + 1)

                    self.ventanaAux.setLayout(self.verticalCuadricula)

                    self.cuadricula.addWidget(self.ventanaAux, fila, columna)

                    self.contador += 1

        self.botones.idClicked.connect(self.metodo_accion_boton)



    def metodo_accion_boton(self, idBoton):
        print(idBoton)
        if (idBoton == 1):
            self.lista_ejercicio = Ventana7_1(self)
            self.lista_ejercicio.show()
            self.hide()

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()

