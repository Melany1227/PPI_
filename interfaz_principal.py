import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, \
    QHBoxLayout

from datos import Ventana6
from ejercicios import Ventana5
from interfaz_perfil import Ventana8


class Ventana3 (QMainWindow):

    def __init__(self, anterior, nombre_usuario):
        super(Ventana3, self).__init__(anterior)

        self.ventanaAnterior = anterior
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

        self.horizontal = QHBoxLayout()
        self.interna = QWidget()
        self.interna.setContentsMargins(50, 50, 50, 50)

        self.setCentralWidget(self.interna)
        self.vertical = QVBoxLayout()

        self.cuadricula = QGridLayout()
        self.interna.setLayout(self.cuadricula)

        self.botonrutina = QPushButton("Mi perfil")
        self.botonrutina.setFixedWidth(250)
        self.botonrutina.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonrutina.clicked.connect(self.metodo_perfil)
        self.cuadricula.addWidget(self.botonrutina, 0, 0)

        self.botonplan = QPushButton("Plan")
        self.botonplan.setFixedWidth(250)
        self.botonplan.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonplan.clicked.connect(self.plan)
        self.cuadricula.addWidget(self.botonplan, 1, 0)

        self.imagen = QLabel()
        self.imagen.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/img_1.png")
        self.imagen.setFixedWidth(360)
        self.imagen.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagen, 0, 1, 6, 1)

        self.botondatos_estadisticas = QPushButton("Datos y Estadisticas")
        self.botondatos_estadisticas.setFixedWidth(250)
        self.botondatos_estadisticas.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botondatos_estadisticas.clicked.connect(self.datos_estadisticas)
        self.cuadricula.addWidget(self.botondatos_estadisticas, 2, 0)

        self.botonejercicio = QPushButton("Ejercicios")
        self.botonejercicio.setFixedWidth(250)
        self.botonejercicio.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonejercicio.clicked.connect(self.ejercicios)
        self.cuadricula.addWidget(self.botonejercicio, 3, 0)

        self.botonacercade = QPushButton("Acerca de")
        self.botonacercade.setFixedWidth(250)
        self.botonacercade.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonacercade.clicked.connect(self.acercade)
        self.cuadricula.addWidget(self.botonacercade, 4, 0)

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.volver)
        self.cuadricula.addWidget(self.botonVolver, 5, 0)

        self.botoncerrarsesion = QPushButton("Cerrar sesión")
        self.botoncerrarsesion.setFixedWidth(250)
        self.botoncerrarsesion.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botoncerrarsesion.clicked.connect(self.cerrarsesion)
        self.cuadricula.addWidget(self.botoncerrarsesion, 6, 0)



    def plan(self):
        pass
    def datos_estadisticas(self):
        self.datos = Ventana6(self)
        self.datos.show()
        self.hide()

    def ejercicios(self):
        self.ejercicios = Ventana5(self)
        self.ejercicios.show()
        self.hide()

    def acercade(self):
        pass

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()

    def cerrarsesion(self):
        sys.exit()

    def metodo_perfil(self):
        self.hide()
        self.interfaz_perfil = Ventana8(self, self.nombreUsuario)
        self.interfaz_perfil.show()
