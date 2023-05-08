from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QFontDatabase, QIcon
from PyQt5.QtWidgets import QLabel, QDesktopWidget, QMainWindow, QWidget, QFormLayout, QVBoxLayout, QGridLayout, \
    QDialog, QDialogButtonBox, QPushButton


class Ventana4 (QMainWindow):

    def __init__(self, anterior):
        super(Ventana4, self).__init__(anterior)
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

        self.interna = QWidget()
        self.interna.setContentsMargins(50, 50, 50, 50)

        self.setCentralWidget(self.interna)
        self.vertical = QVBoxLayout()

        self.cuadricula = QGridLayout()
        self.interna.setLayout(self.cuadricula)

        self.register_label = QLabel("Registro de usuario")
        self.register_label.setAlignment(Qt.AlignCenter)
        self.register_label.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; font-weight: bold;")
        self.cuadricula.addWidget(self.register_label, 0, 0, 1, 3)

        self.fullname_label = QtWidgets.QLabel('Nombre completo')
        self.fullname_label.setAlignment(Qt.AlignCenter)
        self.fullname_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.fullname_label, 1, 0, 1, 1)

        self.fullname_edit = QtWidgets.QLineEdit(self)
        self.fullname_edit.setAlignment(Qt.AlignCenter)
        self.fullname_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.fullname_edit, 1, 1)

        self.email_label = QtWidgets.QLabel('Correo electrónico')
        self.email_label.setAlignment(Qt.AlignCenter)
        self.email_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.email_label, 2, 0, 1, 1)

        self.email_edit = QtWidgets.QLineEdit(self)
        self.email_edit.setAlignment(Qt.AlignCenter)
        self.email_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.email_edit, 2, 1)

        self.password2_label = QtWidgets.QLabel('Contraseña')
        self.password2_label.setAlignment(Qt.AlignCenter)
        self.password2_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins; ")
        self.cuadricula.addWidget(self.password2_label, 3, 0)

        self.password2_edit = QtWidgets.QLineEdit(self)
        self.password2_edit.setAlignment(Qt.AlignCenter)
        self.password2_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.password2_edit, 3, 1)
        self.password2_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.registro2_button = QtWidgets.QPushButton('Registrarse')
        self.registro2_button.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.registro2_button, 4, 0, 2, 4)

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.botonVolver.clicked.connect(self.volver)
        self.cuadricula.addWidget(self.botonVolver, 5, 0)


    def volver(self):
        self.hide()
        self.ventanaAnterior.show()