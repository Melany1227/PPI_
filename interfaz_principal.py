import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, \
    QHBoxLayout

from datos import Ventana6
from ejercicios import Ventana5


class Ventana3 (QMainWindow):

    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)

        self.ventanaAnterior = anterior

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

        self.horizontal = QHBoxLayout()
        self.interna = QWidget()
        self.interna.setContentsMargins(50, 50, 50, 50)

        self.setCentralWidget(self.interna)
        self.vertical = QVBoxLayout()

        self.cuadricula = QGridLayout()
        self.interna.setLayout(self.cuadricula)

        self.botonrutina = QPushButton("Mi Perfil")
        self.botonrutina.setFixedWidth(250)
        self.botonrutina.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonrutina.clicked.connect(self.boton_rutina)
        self.cuadricula.addWidget(self.botonrutina, 0, 0)

        self.botonplan = QPushButton("Mi Rutina")
        self.botonplan.setFixedWidth(250)
        self.botonplan.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonplan.clicked.connect(self.boton_plan)
        self.cuadricula.addWidget(self.botonplan, 1, 0)

        self.imagen = QLabel()
        self.imagen.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/img_1.png")
        self.imagen.setFixedWidth(360)
        self.imagen.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagen, 0, 1, 6, 1)

        self.botondatos_estadisticas = QPushButton("Mis Datos y Estadisticas")
        self.botondatos_estadisticas.setFixedWidth(250)
        self.botondatos_estadisticas.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botondatos_estadisticas.clicked.connect(self.boton_datos_estadisticas)
        self.cuadricula.addWidget(self.botondatos_estadisticas, 2, 0)

        self.botonejercicio = QPushButton("Ejercicios")
        self.botonejercicio.setFixedWidth(250)
        self.botonejercicio.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonejercicio.clicked.connect(self.boton_ejercicios)
        self.cuadricula.addWidget(self.botonejercicio, 3, 0)

        self.botonacercade = QPushButton("Acerca de")
        self.botonacercade.setFixedWidth(250)
        self.botonacercade.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonacercade.clicked.connect(self.boton_acercade)
        self.cuadricula.addWidget(self.botonacercade, 4, 0)

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.boton_volver)
        self.cuadricula.addWidget(self.botonVolver, 5, 0)

        self.botoncerrarsesion = QPushButton("Cerrar sesión")
        self.botoncerrarsesion.setFixedWidth(250)
        self.botoncerrarsesion.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botoncerrarsesion.clicked.connect(self.boton_cerrarsesion)
        self.cuadricula.addWidget(self.botoncerrarsesion, 6, 0)




    def boton_rutina(self):
        pass
    def boton_plan(self):
        pass
    def boton_datos_estadisticas(self):
        self.datos = Ventana6(self)
        self.datos.show()
        self.hide()

    def boton_ejercicios(self):
        self.ejercicios = Ventana5(self)
        self.ejercicios.show()
        self.hide()

    def boton_acercade(self):
        pass

    def boton_volver(self):
        self.hide()
        self.ventanaAnterior.show()

    def boton_cerrarsesion(self):
        pass