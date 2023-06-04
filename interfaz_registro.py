from PyQt5 import QtWidgets, QtCore, QtGui
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
        self.alto = 700
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

        self.user_label = QtWidgets.QLabel('Usuario')
        self.user_label.setAlignment(Qt.AlignCenter)
        self.user_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.user_label, 2, 0, 1, 1)

        self.user_edit = QtWidgets.QLineEdit(self)
        self.user_edit.setAlignment(Qt.AlignCenter)
        self.user_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.user_edit, 2, 1)

        self.email_label = QtWidgets.QLabel('Correo electrónico')
        self.email_label.setAlignment(Qt.AlignCenter)
        self.email_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.email_label, 3, 0, 1, 1)

        self.email_edit = QtWidgets.QLineEdit(self)
        self.email_edit.setAlignment(Qt.AlignCenter)
        self.email_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.email_edit, 3, 1)

        self.password_label = QtWidgets.QLabel('Contraseña')
        self.password_label.setAlignment(Qt.AlignCenter)
        self.password_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins; ")
        self.cuadricula.addWidget(self.password_label, 4, 0)

        self.password_edit = QtWidgets.QLineEdit(self)
        self.password_edit.setAlignment(Qt.AlignCenter)
        self.password_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.password_edit, 4, 1)
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.password2_label = QtWidgets.QLabel('Confirmar contraseña')
        self.password2_label.setAlignment(Qt.AlignCenter)
        self.password2_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins; ")
        self.cuadricula.addWidget(self.password2_label, 5, 0)

        self.password2_edit = QtWidgets.QLineEdit(self)
        self.password2_edit.setAlignment(Qt.AlignCenter)
        self.password2_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.password2_edit, 5, 1)
        self.password2_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.registro2_button = QtWidgets.QPushButton('Registrarse')
        self.registro2_button.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.registro2_button, 6, 0, 2, 4)
        self.registro2_button.clicked.connect(self.registrar)

        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(250)
        self.botonLimpiar.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.botonLimpiar, 7, 1)
        self.botonLimpiar.clicked.connect(self.limpiar)

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.botonVolver.clicked.connect(self.volver)
        self.cuadricula.addWidget(self.botonVolver, 7, 0)

        self.datosCorrectos = True
    def volver(self):
        self.hide()
        self.ventanaAnterior.show()

    def limpiar(self):
        if (
                self.fullname_edit.text() == ''
                or self.user_edit.text() == ''
                or self.password_edit.text() == ''
                or self.password2_edit.text() == ''
                or self.email_edit.text() == ''

        ):
            self.fullname_edit.setText('')
            self.user_edit.setText('')
            self.password_edit.setText('')
            self.password3_edit.setText('')
            self.email_edit.setText('')


    def registrar(self):

        self.datosCorrectos = True

        # validamos que las contra sean iguales
        if (
            self.password_edit.text() != self.password2_edit.text()
        ):
            self.datosCorrectos = False
            self.mensaje.setText("Las contraseñas no son iguales")
            self.ventanaDialogo.exec_()
            self.ventanaAnterior.show()

        # Validamos que se ingresen todos los campos
        if (
                self.fullname_edit.text() == ''
                or self.user_edit.text() == ''
                or self.password_edit.text() == ''
                or self.password2_edit.text() == ''
                or self.email_edit.text() == ''

        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debe llenar todos los campos")
            self.ventanaDialogo.exec_()
            self.ventanaAnterior.show()

        # Si los datos están correctos:
        if self.datosCorrectos:

            # Abrimos el archivo en modo agregar escribiendo datos en binario.
            self.file = open('datos/users.txt', 'ab')

            # traer el texto de los QLineEdit() y los agrega concatenandolos.
            # para escribirlos en el archivo en formato binario utf-8
            self.file.write(bytes(
                self.fullname_edit.text() + ";"
                + self.user_edit.text() + ";"
                + self.password2_edit.text() + ";"
                + self.password_edit.text() + ";"
                + self.email_edit.text() + "\n"
                , encoding='UTF-8'))
            self.file.close()

            self.file = open('datos/users.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

            self.mensaje.setText("Se ha registrado correctamente.")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()
            self.ventanaAnterior.show()

            self.fullname_edit.setText('')
            self.user_edit.setText('')
            self.password2_edit.setText('')
            self.password_edit.setText('')
            self.email_edit.setText('')
