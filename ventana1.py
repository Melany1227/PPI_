import sys


from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QFontDatabase, QIcon
from PyQt5.QtWidgets import QLabel, QDesktopWidget, QMainWindow, QWidget, QFormLayout, QVBoxLayout, QGridLayout, \
    QDialog, QDialogButtonBox, QPushButton

from users import Usuarios
from interfaz_bienvenido import Ventana2
from interfaz_registro import Ventana4


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)

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

        self.label = QLabel("Inicio de sesión")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; font-weight: bold;")
        self.cuadricula.addWidget(self.label, 0, 0, 1, 3)

        self.username_label = QtWidgets.QLabel('Usuario')
        self.username_label.setAlignment(Qt.AlignCenter)
        self.username_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.username_label, 1, 0, 1, 1)


        self.imgUser = QLabel(self.username_label)
        self.imgUser.setPixmap(QPixmap("imagenes/perfil.png").scaled(35,35,35,35))
        self.cuadricula.addWidget(self.imgUser, 1, 1, 1, 1)



        self.user_edit = QtWidgets.QLineEdit(self)
        self.user_edit.setAlignment(Qt.AlignCenter)
        self.user_edit.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.user_edit, 1, 2)


        self.password_label = QtWidgets.QLabel('Contraseña')
        self.password_label.setAlignment(Qt.AlignCenter)
        self.password_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins; ")
        self.cuadricula.addWidget(self.password_label, 2, 0)



        self.imgPwd = QLabel(self.password_label)
        self.imgPwd.setPixmap(QPixmap("imagenes/contrasena.png").scaled(35, 35, 35, 35))
        self.cuadricula.addWidget(self.imgPwd, 2, 1)


        self.password_edit = QtWidgets.QLineEdit(self)
        self.password_edit.setAlignment(Qt.AlignCenter)
        self.password_edit.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.password_edit, 2, 2)
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)


        self.login_button = QtWidgets.QPushButton('Iniciar sesión')
        self.login_button.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; ")
        self.login_button.clicked.connect(self.login)
        self.cuadricula.addWidget(self.login_button, 3, 0, 2, 4)

        self.registro_button = QtWidgets.QPushButton('Registrarse')
        self.registro_button.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
                                        "border: 1px solid #FFFFFF; ")
        self.registro_button.clicked.connect(self.registrar)
        self.cuadricula.addWidget(self.registro_button, 4, 0, 2, 4)


    def login(self):

        self.datosCorrectos = True

        if (self.user_edit.text() == '' or self.password_edit.text() == ''):
            self.datosCorrectos = False
            self.ventanaDialogo = QDialog()

            self.ventanaDialogo.resize(300, 150)

            self.botonAceptar = QDialogButtonBox.Ok
            self.opcionesBotones = QDialogButtonBox(self.botonAceptar)
            self.opcionesBotones.accepted.connect(self.ventanaDialogo.accept)

            self.ventanaDialogo.setWindowTitle("HELP TRAINING")
            self.ventanaDialogo.setWindowIcon(QtGui.QIcon("imagenes/img_1.png"))

            self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

            self.vertical = QVBoxLayout()
            self.mensaje = QLabel("")
            self.mensaje.setStyleSheet("background-color: #000000; color: #FFFFFF; font-size: 18px; "
                                       "font-family: Poppins; padding: 10px; border-radius:10px;")

            self.vertical.addWidget(self.mensaje)
            self.vertical.addWidget(self.opcionesBotones)

            self.ventanaDialogo.setLayout(self.vertical)
            self.mensaje.setText("Contraseña y/o usuario incorrecto, por favor intente de nuevo.")
            self.ventanaDialogo.exec_()

        if self.datosCorrectos:

            # Abrimos el archivo en modo agregar escribiendo datos en binario.
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

            existeDocumento = False

            for u in usuario:
                if u.user_edit == self.user_edit.text() and u.password_edit == (self.password_edit.text()):
                    self.hide()
                    self.interfaz_bienvenido = Ventana2(self)
                    self.interfaz_bienvenido.show()

                    existeDocumento = True
                    break

        if (not existeDocumento):
            self.ventanaDialogo = QDialog()

            self.ventanaDialogo.resize(300, 150)

            self.botonAceptar = QDialogButtonBox.Ok
            self.opcionesBotones = QDialogButtonBox(self.botonAceptar)
            self.opcionesBotones.accepted.connect(self.ventanaDialogo.accept)

            self.ventanaDialogo.setWindowTitle("HELP TRAINING")
            self.ventanaDialogo.setWindowIcon(QtGui.QIcon("imagenes/img_1.png"))

            self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

            self.vertical = QVBoxLayout()
            self.mensaje = QLabel("")
            self.mensaje.setStyleSheet("background-color: #000000; color: #FFFFFF; font-size: 18px; "
                                       "font-family: Poppins; padding: 10px; border-radius:10px;")

            self.vertical.addWidget(self.mensaje)
            self.vertical.addWidget(self.opcionesBotones)

            self.ventanaDialogo.setLayout(self.vertical)
            self.mensaje.setText("Contraseña y/o usuario incorrecto, por favor intente de nuevo.")
            self.ventanaDialogo.exec_()


    def registrar(self):
        self.ventana1 = Ventana4(self)
        self.ventana1.show()
        self.hide()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
