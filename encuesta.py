import sys

from PyQt5.QtGui import QPixmap, QFont, QFontDatabase
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QVBoxLayout, QDialog, QDialogButtonBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt



class Ventana1(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        self.setWindowTitle("Formulario de Registro")
        self.setStyleSheet("background-color: black;")
        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon("imagenes/img.png"))

        QFontDatabase.addApplicationFont("fonts/Poppins-ExtraLight.ttf")

        self.ancho = 900
        self.alto = 800


        self.resize(self.ancho, self.alto)


        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedSize(self.ancho, self.alto)

        # ventana en el centro

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())


        self.setFixedSize(self.ancho, self.alto)

        # ventana en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # para que la ventana no se pueda cambiar de tamaño
        # se fija el ancho y alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)


        # establecemos la ventana fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribuccion de los elementos en Layout horizontal
        self.horizontal = QHBoxLayout()
        # Le ponemos las margenes:
        self.horizontal.setContentsMargins(50, 50, 30, 50)


        # *****************Layout IZQUIERDO******************


        # ******Layout IZQUIERDO*******


        # ***Layout IZQUIERDO**

        # creamos el layout del lado izquierdo:
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("Registro de usuario")

        # Le asignamos el tipo de letra
        self.letrero1.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; font-weight: bold;")


        # Agregamos el letrero en la primera fila:
        self.ladoIzquierdo.addRow(self.letrero1)

        # Agregamos el layout ladoIzquierdo al layout horizontal:
        self.horizontal.addLayout(self.ladoIzquierdo)

        # Hacemos el letrero:
        self.letrero2 = QLabel()

        # Establecemos el ancho del label:
        self.letrero2.setFixedWidth(340)

        # Les escribimos el e¿texto
        self.letrero2.setText("")

        # Le asignamos el tipo de letra
        self.letrero2.setFont(QFont("Andalem Mono", 3))

        # Le ponemos el color del texto y margenes:
        self.letrero2.setStyleSheet("color: #000000; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el campo para ingresar el nombre
        self.fullname_edit = QLineEdit()
        self.fullname_edit.setFixedWidth(250)
        self.fullname_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")

        self.fullname = QLabel('Nombre completo')
        self.fullname.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")

        self.ladoIzquierdo.addRow(self.fullname)
        self.ladoIzquierdo.addRow(self.fullname_edit)


        self.user_edit = QLineEdit()
        self.user_edit.setFixedWidth(250)

        self.ladoIzquierdo.addRow(self.user_edit)

        # Hacemos el campo para ingresar la contraseña:
        self.contra = QLineEdit()
        self.contra.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Contraseña*", self.contra)

        # Hacemos el campo para ingresar la contraseña2:
        self.contra2 = QLineEdit()
        self.contra2.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Contraseña*", self.contra2)

        # Hacemos el campo para agregar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        # Hacemos el botón para registrar los datos:
        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(90)
        self.botonRegistrar.setStyleSheet("background-color: #000000;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        # Hacemos el botón para limpiar los datos:
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)
        self.botonLimpiar.setStyleSheet("background-color: #000000;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        # Agregamos los botones al Layout ladoIzquierdo:
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        # Agregamos el layout ladoIzquierdo al layout horizontal:
        self.horizontal.addLayout(self.ladoIzquierdo)

        # *****************Layout DERECHO******************

        # ***Layout DERECHO**


        # creamos el layout del lado izquierdo:
        self.ladoDerecho = QFormLayout()

        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        # Hacemos el letrero
        self.letrero3 = QLabel()

        # Le escribimos el texto:
        self.letrero3.setText("Recuperar Contraseña")

        # Le asignamos el tipo de letra
        self.letrero3.setFont(QFont("Andalem Mono", 20))

        # Le ponemos el color del texto:
        self.letrero3.setStyleSheet("color: #000000;")

        # Agregamos el letrero en la primera fila:
        self.ladoDerecho.addRow(self.letrero3)

        # Hacemos el letrero:
        self.letrero4 = QLabel()

        # Establecemos el ancho del label:
        self.letrero4.setFixedWidth(340)

        # Les escribimos el e¿texto
        self.letrero4.setText("Por favor ingrese la información para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra
        self.letrero4.setFont(QFont("Andalem Mono", 10))

        # Le ponemos el color del texto y margenes:
        self.letrero4.setStyleSheet("color: #000000; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.letrero4)

        # --- 1

        # Hacemos el letrero de la pregunta 1
        self.labelPregunta1 = QLabel("Pregunta de verificación 1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta1)


        # Hacemos el campo para ingresar la pregunta1:
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow(self.pregunta1)

        # Hacemos el letrero de la respuesta 1
        self.labelRespuesta1 = QLabel("Respuesta de verificación 1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta1)

        # Hacemos el campo para ingresar la respuesta1:
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow(self.respuesta1)


        # --- 2

        # Hacemos el letrero de la pregunta 2
        self.labelPregunta2 = QLabel("Pregunta de verificación 2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta2)

        # Hacemos el campo para ingresar la pregunta2:
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow(self.pregunta2)

        # Hacemos el letrero de la respuesta 2
        self.labelRespuesta2 = QLabel("Respuesta de verificación 2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta2)

        # Hacemos el campo para ingresar la respuesta2:
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow(self.respuesta2)

        # --- 3

        # Hacemos el letrero de la pregunta 3
        self.labelPregunta3 = QLabel("Pregunta de verificación 3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta3)

        # Hacemos el campo para ingresar la pregunta1:
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow(self.pregunta3)

        # Hacemos el letrero de la respuesta 1
        self.labelRespuesta3 = QLabel("Respuesta de verificación 3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta3)

        # Hacemos el campo para ingresar la respuesta3:
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow(self.respuesta3)

        # Hacemos el botón para buscar las preguntas:
        self.botonBuscar = QPushButton("Buscar")
        self.botonBuscar.setFixedWidth(90)
        self.botonBuscar.setStyleSheet("background-color: #000000;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        # Hacemos el botón para recuperar la contraseña:
        self.botonRecuperar = QPushButton("Recuperar")
        self.botonRecuperar.setFixedWidth(90)
        self.botonRecuperar.setStyleSheet("background-color: #000000;"
                                            "color: #FFFFFF;"
                                            "padding: 10px;"
                                            "margin-top: 40px;")

        # Hacemos el botón para continuar en la ventana sigueinte:
        self.botonContinuar = QPushButton("Continuar")
        self.botonContinuar.setFixedWidth(90)
        self.botonContinuar.setStyleSheet("background-color: #000000;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        # Agregamos los botones al Layout ladoIzquierdo:
        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)
        self.ladoDerecho.addRow(self.botonContinuar)

        # Agregamos el layout ladoDerecho al layout horizontal:
        self.horizontal.addLayout(self.ladoDerecho)

        # ---------------OJO IMPORTANTE PONER AL FINAL-----------
        # Indicamos que el layout principal del fondo es horizontal:
        self.fondo.setLayout(self.horizontal)

        # -----------Construccion de la ventana emergente----------------

        # Creamos la ventana de diálogo:
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.resize(300, 150)
        # Poner el icono:
        self.ventanaDialogo.setWindowIcon(QtGui.QIcon("imagenes/img.png"))

        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # Establecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        # Configuramos la ventana para que sea modal:
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # Creamos un layout vertical:
        self.vertical = QVBoxLayout()

        # Creamos un label para los mensajes:
        self.mensaje = QLabel("")

        # Le ponemos estilo al label mensaje:
        self.mensaje.setStyleSheet("background-color: #000000; color: #FFFFFF; padding: 10px;")

        # agregamos el label de mensajes
        self.vertical.addWidget(self.mensaje)

        # Agregamos las opciones de los botones.
        self.vertical.addWidget(self.opciones)

        # Establecemos el layout para la ventana de dialogo:
        self.ventanaDialogo.setLayout(self.vertical)

        # Creamos una variable para validar si los datos estan correctos
        self.datosCorrectos = True



if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre de ventana1
    ventana1 = Ventana1()
    # hacer que objeto ventana 1 se vea
    ventana1.show()

    sys.exit(app.exec_())