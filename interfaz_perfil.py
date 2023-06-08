import math
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFormLayout, QApplication, QLineEdit, QDialog, \
    QDialogButtonBox, QVBoxLayout, QPushButton, QWidget, QButtonGroup, QScrollArea, QGridLayout, QHBoxLayout, QComboBox

from lista_ejercicio import Ventana7_1, Ventana7_2, Ventana7_3, Ventana7_4, Ventana7_5, Ventana7_6, Ventana7_7, \
    Ventana7_8, Ventana7_9, Ventana7_10, Ventana7_11
from users import Usuarios


class Ventana8(QMainWindow):

    def __init__(self, anterior, nombre_usuario):
        super(Ventana8, self).__init__(anterior)

        self.ventanaAnterior = anterior
        self.nombreUsuario = nombre_usuario

        self.setWindowTitle("HELP TRAINING")
        self.setWindowIcon(QIcon("imagenes/img_1.png"))
        self.setStyleSheet("background-color: black;")

        self.ancho = 1000
        self.alto = 800
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.interna = QWidget()
        self.interna.setContentsMargins(20, 20, 20, 20)

        self.setCentralWidget(self.interna)

        self.horizontal = QHBoxLayout()

        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText(self.nombreUsuario)

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


        self.horizontal.addLayout(self.vertical)
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()

        self.scrollArea.setContentsMargins(5, 5, 5, 5)


        self.cuadricula = QGridLayout(self.contenedora)
        self.scrollArea.setWidget(self.contenedora)
        self.horizontal.addWidget(self.scrollArea)


        self.interna.setLayout(self.horizontal)

        self.ventanaAux = QWidget()
        self.ventanaAux.setFixedHeight(1000)
        self.ventanaAux.setFixedWidth(600)
        self.verticalCuadricula = QVBoxLayout()

        self.imagen = QLabel()
        self.pixmap = QPixmap("imagenes/img_1.png")
        self.imagen.setAlignment(QtCore.Qt.AlignCenter)
        self.imagen.setFixedHeight(300)
        self.imagen.setFixedWidth(600)
        self.imagen.setPixmap(self.pixmap)

        self.verticalCuadricula.addWidget(self.imagen)

        self.texto = QLabel('En Help Training te queremos hablar de un viaje,\n'
                            'un viaje que cambiará tu vida de una manera\n'
                            'extraordinaria. Es un viaje hacia la mejor versión\n'
                            'de ti mismo/a, un camino que te llevará a alcanzar\n'
                            'metas que tal vez nunca pensaste posibles. Estamos \n'
                            'hablando del camino hacia una vida activa y saludable.')
        self.texto.setStyleSheet("color: white; font-size: 20px; font-family: Poppins; border: 2px solid #FFFFFF; "
                                 "border-left: none;"
                                 "border-right: none;"
                                 "border-top: none;"
                                 )
        self.texto.setFixedHeight(250)
        self.texto.setFixedWidth(600)
        self.verticalCuadricula.addWidget(self.texto)
        self.ventanaAux.setLayout(self.verticalCuadricula)

        self.lab = QLabel("Percepción semanal")
        self.lab.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        #self.lab.setFixedHeight(100)
        #self.lab.setFixedWidth(500)
        self.verticalCuadricula.addWidget(self.lab)
        self.ventanaAux.setLayout(self.verticalCuadricula)

        self.percepcion = QComboBox()

        self.botonDatos = QPushButton("Actualizar Datos")
        self.botonDatos.setFixedWidth(250)
        self.botonDatos.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonDatos.clicked.connect(self.actualizar)
        self.verticalCuadricula.addWidget(self.botonDatos)
        self.ventanaAux.setLayout(self.verticalCuadricula)

        self.cuadricula.addWidget(self.ventanaAux)

        self.horizontal.addLayout(self.vertical)


        self.file = open('datos/users.txt', 'rb')
        usuario = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")
            if linea == '':
                break

            u = Usuarios(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9]
            )
            usuario.append(u)
        self.file.close()

        # Dentro de la clase Ventana2, después de cargar los datos de usuarios
        with open("datos/users.txt", "r") as file:
            for line in file:
                # Separar los campos de la línea por punto y coma (;)
                lista = line.strip().split(";")
                if lista[2] == self.nombreUsuario:
                    # Aquí puedes acceder a los datos adicionales del usuario
                    self.peso = lista[6]
                    self.enfermedad = lista[9]
                    # Hacer algo con los datos obtenidos
                    print(self.peso, self.enfermedad)
                    break




    def volver(self):
        self.hide()
        self.ventanaAnterior.show()


    def actualizar(self):
        pass