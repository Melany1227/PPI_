from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QDate
from datetime import date
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QHBoxLayout, QWidget, QVBoxLayout, QGridLayout, QPushButton, \
    QFormLayout, QLineEdit, QLabel, QDateEdit, QDialog, QDialogButtonBox, QComboBox


class Ventana6 (QMainWindow):

    def __init__(self, anterior):
        super(Ventana6, self).__init__(anterior)

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

        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.resize(300, 150)
        # Creamos el boton de aceptar:
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)
        self.ventanaDialogo.setWindowTitle("HELP TRAINING")
        self.ventanaDialogo.setWindowIcon(QtGui.QIcon("imagenes/img_1.png"))

        # Configuramos la ventana para que sea modal:
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # Creamos un layout vertical:
        self.vertical = QVBoxLayout()

        # Creamos un label para los mensajes:
        self.mensaje = QLabel("")

        # Le ponemos estilo al label mensaje:
        self.mensaje.setStyleSheet(
            "background-color: #000000; color: #FFFFFF; font-size: 18px; font-family: Poppins; padding: 8px;")

        # agregamos el label de mensajes
        self.vertical.addWidget(self.mensaje)

        self.vertical.addWidget(self.opciones)

        # Establecemos el layout para la ventana de dialogo:
        self.ventanaDialogo.setLayout(self.vertical)

        self.register_label = QLabel("Registro de datos")
        self.register_label.setAlignment(Qt.AlignCenter)
        self.register_label.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; font-weight: bold;")
        self.cuadricula.addWidget(self.register_label, 0, 0, 1, 6)

        # ------ LADO IZQUIERDO ------

        self.label = QLabel("Fecha del registro ", self)
        self.label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.label.setAlignment(Qt.AlignCenter)
        self.cuadricula.addWidget(self.label, 1, 0)

        self.now = QDate.currentDate()
        self.date = (self.now.toString(Qt.ISODate))
        self.fecha = QtWidgets.QLabel(self.date)
        self.fecha.setAlignment(Qt.AlignCenter)
        self.fecha.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF;")
        self.cuadricula.addWidget(self.fecha, 1, 1)


        # ------ LADO DERECHO ----

        self.height = QtWidgets.QLabel('Estatura')
        self.height.setAlignment(Qt.AlignCenter)
        self.height.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.height, 1, 3)

        self.height_edit = QtWidgets.QLineEdit(self)
        self.height_edit.setAlignment(Qt.AlignCenter)
        self.height_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.height_edit, 1, 4)

        self.height_info = QtWidgets.QLabel('cm')
        self.height_info.setAlignment(Qt.AlignCenter)
        self.height_info.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.height_info, 1, 5)

        self.weight = QtWidgets.QLabel('Peso')
        self.weight.setAlignment(Qt.AlignCenter)
        self.weight.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.weight, 2, 3)

        self.weight_edit = QtWidgets.QLineEdit(self)
        self.weight_edit.setAlignment(Qt.AlignCenter)
        self.weight_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.weight_edit, 2, 4)

        self.weight_info = QtWidgets.QLabel('kg')
        self.weight_info.setAlignment(Qt.AlignCenter)
        self.weight_info.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.weight_info, 2, 5)

        self.nivel = QtWidgets.QLabel('¿Cuántas veces a la \nsemana '
                                      'realiza \nactividad física?')
        self.nivel.setAlignment(Qt.AlignCenter)
        self.nivel.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.nivel, 3, 3)

        self.nivel_resp = QComboBox()
        self.nivel_resp.addItems(["", "0", "1", "2", "3", "4", "5", "6", "7"])
        self.nivel_resp.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.nivel_resp, 3, 4)

        self.plan = QtWidgets.QLabel('¿Cuántas veces a la \nsemana '
                                     'desea realizar\nactividad física?')
        self.plan.setAlignment(Qt.AlignCenter)
        self.plan.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.plan, 4, 3)

        self.plan_resp = QComboBox()
        self.plan_resp.addItems(["", "1", "2", "3", "4", "5", "6", "7"])
        self.plan_resp.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.plan_resp, 4, 4)


        self.space = QtWidgets.QPushButton('')
        self.space.setStyleSheet(
            "color: white; font-size: 5px; font-family: Poppins;")
        self.cuadricula.addWidget(self.space, 6, 0)

        self.registro2_button = QtWidgets.QPushButton('Registrarse')
        self.registro2_button.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
            "border: 1px solid #FFFFFF;")
        self.cuadricula.addWidget(self.registro2_button, 7, 0)
        self.registro2_button.clicked.connect(self.registrar)

        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(250)
        self.botonLimpiar.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
            "border: 1px solid #FFFFFF;")
        self.cuadricula.addWidget(self.botonLimpiar, 8, 0)
        self.botonLimpiar.clicked.connect(self.limpiar)

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.botonVolver.clicked.connect(self.volver)
        self.cuadricula.addWidget(self.botonVolver, 9, 0)

        self.datosCorrectos = True

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()

    def registrar(self):
        pass

    def limpiar(self):
        pass