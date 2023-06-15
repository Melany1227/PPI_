import math
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QDate
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

        self.horizontal = QHBoxLayout()
        self.horizontal.addLayout(self.vertical)
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()

        self.scrollArea.setContentsMargins(10, 10, 10, 10)


        self.cuadricula = QGridLayout(self.contenedora)
        self.scrollArea.setWidget(self.contenedora)
        self.horizontal.addWidget(self.scrollArea)

        self.interna.setLayout(self.horizontal)

        self.ventanaAux = QWidget()
        self.ventanaAux.setFixedHeight(1500)
        self.ventanaAux.setFixedWidth(600)
        self.verticalCuadricula = QVBoxLayout()

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
                lista[9],
                lista[10],
                lista[11]
            )
            usuario.append(u)
        self.file.close()

        # Dentro de la clase Ventana2, después de cargar los datos de usuarios
        with open("datos/users.txt", "r") as file:
            for line in file:
                # Separar los campos de la línea por punto y coma (;)
                lista = line.strip().split(";")
                if lista[2] == self.nombreUsuario:
                    self.alturaU = lista[5]
                    self.imcU = lista[10]
                    self.levelU = lista[11]
                    self.peso = lista[6]
                    self.fullname = lista[1]
                    self.user = lista[2]
                    self.password = lista[3]
                    self.password2 = lista[4]
                    self.vecesEntreno = lista[7]
                    self.plan = lista[8]
                    self.disease = lista[9]
                    break

        self.imagen = QLabel()
        self.pixmap = QPixmap("imagenes/img_1.png")
        self.imagen.setAlignment(QtCore.Qt.AlignCenter)
        self.imagen.setFixedHeight(300)
        self.imagen.setFixedWidth(600)
        self.imagen.setPixmap(self.pixmap)

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

        self.verticalCuadricula.addWidget(self.imagen)

        self.texto = QLabel('En Help Training te queremos hablar de un viaje,\n'
                            'un viaje que cambiará tu vida de una manera\n'
                            'extraordinaria. Es un viaje hacia la mejor versión\n'
                            'de ti mismo/a, un camino que te llevará a alcanzar\n'
                            'metas que tal vez nunca pensaste posibles. Estamos \n'
                            'hablando del camino hacia una vida activa y saludable.\n\n')
        self.texto.setStyleSheet("color: white; font-size: 20px; font-family: Poppins; border: 2px solid #FFFFFF; "
                                 "border-left: none;"
                                 "border-right: none;"
                                 "border-top: none;"
                                 )
        self.texto.setFixedHeight(250)
        self.texto.setFixedWidth(600)
        self.verticalCuadricula.addWidget(self.texto)
        self.ventanaAux.setLayout(self.verticalCuadricula)

        self.ladoIzquierdo = QFormLayout()

        self.lab = QLabel("Datos")
        self.lab.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; font-weight: bold;")
        self.lab.setAlignment(Qt.AlignCenter)
        # self.lab.setFixedHeight(100)
        # self.lab.setFixedWidth(500)
        self.verticalCuadricula.addWidget(self.lab)
        self.ventanaAux.setLayout(self.verticalCuadricula)

        self.label = QLabel("Fecha del registro ", self)
        self.label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.verticalCuadricula.addWidget(self.label)

        self.now = QDate.currentDate()
        self.date = (self.now.toString(Qt.ISODate))

        self.fecha = QtWidgets.QLineEdit(self)
        self.fecha.setFixedWidth(250)
        self.fecha.setFixedHeight(50)
        self.fecha.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.verticalCuadricula.addWidget(self.fecha)

        self.height = QLabel('Estatura')
        self.height.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.verticalCuadricula.addWidget(self.height)

        self.height_edit = QtWidgets.QLineEdit(self)
        self.height_edit.setFixedWidth(250)
        self.height_edit.setFixedHeight(50)
        self.height_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.verticalCuadricula.addWidget(self.height_edit)
        self.height_edit.setToolTip('cm')

        self.weight = QLabel('Peso')
        self.weight.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.verticalCuadricula.addWidget(self.weight)

        self.weight_edit = QtWidgets.QLineEdit(self)
        self.weight_edit.setFixedWidth(250)
        self.weight_edit.setFixedHeight(50)
        self.weight_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.verticalCuadricula.addWidget(self.weight_edit)
        self.height_edit.setToolTip('kg')

        self.imc = QLabel('IMC')
        self.imc.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.verticalCuadricula.addWidget(self.imc)

        self.imc_edit = QtWidgets.QLineEdit(self)
        self.imc_edit.setFixedWidth(250)
        self.imc_edit.setFixedHeight(50)
        self.imc_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.verticalCuadricula.addWidget(self.imc_edit)

        self.nivel = QLabel('Nivel recomendado')
        self.nivel.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.verticalCuadricula.addWidget(self.nivel)

        self.nivel_edit = QtWidgets.QLineEdit(self)
        self.nivel_edit.setFixedWidth(250)
        self.nivel_edit.setFixedHeight(50)
        self.nivel_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.verticalCuadricula.addWidget(self.nivel_edit)

        self.entreno = QtWidgets.QLabel('¿Cuántas veces realizó actividad física esta semana?')
        self.entreno.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.verticalCuadricula.addWidget(self.entreno)

        self.entreno_resp = QComboBox()
        self.entreno_resp.setFixedWidth(250)
        self.entreno_resp.setFixedHeight(50)
        self.entreno_resp.addItems(["", "0", "1", "2", "3", "4", "5", "6", "7"])
        self.entreno_resp.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF;")
        self.verticalCuadricula.addWidget(self.entreno_resp)


        self.percepcion = QtWidgets.QLabel('¿Cuál fue tu percepción sobre el entrenamiento\nde esta semana?')
        self.percepcion.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.verticalCuadricula.addWidget(self.percepcion)

        self.percepcion_edit = QComboBox()
        self.percepcion_edit.setFixedWidth(250)
        self.percepcion_edit.setFixedHeight(50)
        self.percepcion_edit.addItems(["", "Muy fácil", "Adecuado", "Muy difícil"])
        self.percepcion_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF;")
        self.verticalCuadricula.addWidget(self.percepcion_edit)


        self.botonDatos = QPushButton("Actualizar Datos")
        self.botonDatos.setFixedWidth(250)
        self.botonDatos.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF;")
        self.botonDatos.clicked.connect(self.actualizar)
        self.verticalCuadricula.addWidget(self.botonDatos)
        self.ventanaAux.setLayout(self.verticalCuadricula)

        self.cuadricula.addWidget(self.ventanaAux)
        self.horizontal.addLayout(self.ladoIzquierdo)

        self.horizontal.addLayout(self.vertical)

        self.cargar_datos()


    def volver(self):
        self.hide()
        self.ventanaAnterior.show()


    def cargar_datos(self):
        self.file = open('datos/users.txt', 'rb')

        usuarios = []

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
                lista[9],
                lista[10],
                lista[11]
            )
            # metemos el objeto en la lista de usuarios:
            usuarios.append(u)

            # cerramos el archivo
        self.file.close()

        # Buscamos en la lista users por users para ver si existe la cedula:
        for u in usuarios:
                self.fecha.setText(u.fecha)
                self.fecha.setReadOnly(True)
                self.height_edit.setText(self.alturaU)
                # Con esto el nombre no se puede editar
                self.height_edit.setReadOnly(True)
                self.weight_edit.setText(self.peso)
                self.imc_edit.setText(self.imcU)
                self.imc_edit.setReadOnly(True)
                self.nivel_edit.setText(self.levelU)
                self.nivel_edit.setReadOnly(True)
                # indicamos que encontramos el dodumento:
                existeDocumento = True
                # paramos el for
                break





    def actualizar(self):
        self.datosCorrectos = True

        if (
                self.weight_edit.text() == ''
                or self.percepcion_edit.currentText() == ''
                or self.entreno_resp.currentText() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText("No puede dejar ningún espacio en blanco")
            self.ventanaDialogo.exec_()


        if (
                not self.weight_edit.text().isnumeric()
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("El peso debe ser numérico.")

            # hacemos que la ventanaDIalogo se vea:
            self.ventanaDialogo.exec_()

            # limpiamos el campo del documento:
            self.weight_edit.setText('')


        if self.datosCorrectos:

            self.file = open('datos/users.txt', 'rb')
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(";")
                # Separa si ya no hay mas registros en el archivo
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
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
                    lista[9],
                    lista[10],
                    lista[11]
                )
                # metemos el objeto en la lista de usuarios:
                usuarios.append(u)

            # cerramos el archivo
            self.file.close()

            existeDocumento = False

            for u in usuarios:
                self.peso = self.weight_edit.text()
                existeDocumento = True
                break

            self.peso2 = float(self.weight_edit.text())
            self.altura = float(self.height_edit.text())
            self.imc = float(self.peso2 / ((self.altura / 100) ** 2))
            self.imc = (f"{self.imc:.2f}")

            self.contadorPri = 0
            self.contadorInt = 0
            self.contadorAv = 0

            self.vecesEntrenoAnterior = self.vecesEntreno

            self.file = open('datos/users.txt', 'wb')

            for u in usuarios:
                self.file.write(bytes(self.fecha.text() + ";"
                + self.fullname + ";"
                + self.user + ";"
                + self.password + ";"
                + self.password2 + ";"
                + self.alturaU + ";"
                + self.peso + ";"
                + self.vecesEntrenoAnterior + ";"
                + self.plan + ";"
                + self.disease + ";"
                + self.imc + ";"
                + self.levelU, encoding='UTF-8'))
            self.file.close()

            if (self.vecesEntrenoAnterior < self.vecesEntreno):
                self.mensaje.setText("Recuerda, lo más importante es no desanimarte por los\n" 
                                     "contratiempos. Cada día es una nueva oportunidad para\n"
                                     "retomar tu compromiso y esforzarte un poco más.\n"
                                     "¡Confía en ti mismo/a y sigue adelante!\n"
                                     "¡Tú puedes hacerlo!")
                self.ventanaDialogo.exec_()

            if (self.vecesEntrenoAnterior == self.vecesEntreno):
                self.mensaje.setText("Tu dedicación y disciplina son realmente admirables.\n"
                                     "Cada sesión de entrenamiento que completas es un paso\n"
                                     "adelante hacia una versión más fuerte y saludable de ti mismo/a.")


                self.ventanaDialogo.exec_()

            if (self.vecesEntrenoAnterior > self.vecesEntreno):
                self.mensaje.setText("Tu determinación y pasión por superarte son dignas\n"
                                     "de admiración. Al entrenar cada vez más duro, estás\n"
                                     "desafiando tus propios límites y creando un camino\n"
                                     "hacia tu mejor versión.")
                self.ventanaDialogo.exec_()

            if (self.percepcion_edit.currentText() == "Muy fácil" and self.levelU != "Avanzado"):
                self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

                self.ventanaDialogoEliminar.setWindowTitle("HELP TRAINING")
                self.ventanaDialogoEliminar.setWindowIcon(QtGui.QIcon("imagenes/img_1.png"))

                # Definimos el tamaño de la ventana:
                self.ventanaDialogoEliminar.resize(300, 150)

                # Configuramos la ventana para que sea modal:
                self.ventanaDialogoEliminar.setWindowModality(Qt.ApplicationModal)

                # Creamos un layout vertical:
                self.verticalEliminar = QVBoxLayout()

                # Creamos un label para los mensajes:
                self.mensajeEliminar = QLabel("¿Desea subir de nivel?")

                # Le ponemos estilo al label mensaje:
                self.mensajeEliminar.setStyleSheet(
                    "background-color: #000000; color: #FFFFFF; font-size: 18px; font-family: Poppins; padding: 8px;")

                # agregamos el label de mensajes
                self.verticalEliminar.addWidget(self.mensajeEliminar)

                self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
                self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

                self.opcionesBox.accepted.connect(self.ok_opcion)
                self.opcionesBox.rejected.connect(self.cancel_opcion)

                # Agregamos las opciones de los botones.
                self.verticalEliminar.addWidget(self.opcionesBox)

                # Establecemos el layout para la ventana de dialogo:
                self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)

                self.ventanaDialogoEliminar.exec_()


            if (self.percepcion_edit.currentText() == "Muy difícil" and self.levelU != "Principiante"):
                self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
                self.ventanaDialogoEliminar.setWindowTitle("HELP TRAINING")
                self.ventanaDialogoEliminar.setWindowIcon(QtGui.QIcon("imagenes/img_1.png"))

                # Definimos el tamaño de la ventana:
                self.ventanaDialogoEliminar.resize(300, 150)

                # Configuramos la ventana para que sea modal:
                self.ventanaDialogoEliminar.setWindowModality(Qt.ApplicationModal)

                # Creamos un layout vertical:
                self.verticalEliminar = QVBoxLayout()

                # Creamos un label para los mensajes:
                self.mensajeEliminar = QLabel("¿Desea bajar de nivel?")

                # Le ponemos estilo al label mensaje:
                self.mensajeEliminar.setStyleSheet(
                    "background-color: #000000; color: #FFFFFF; font-size: 18px; font-family: Poppins; padding: 8px;")

                # agregamos el label de mensajes
                self.verticalEliminar.addWidget(self.mensajeEliminar)

                self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
                self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

                self.opcionesBox.accepted.connect(self.ok_opcion2)
                self.opcionesBox.rejected.connect(self.cancel_opcion)

                # Agregamos las opciones de los botones.
                self.verticalEliminar.addWidget(self.opcionesBox)

                # Establecemos el layout para la ventana de dialogo:
                self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)

                self.ventanaDialogoEliminar.exec_()



            if (
                    existeDocumento
            ):
                # escribimos el texto explicativo:
                self.mensaje.setText("Información actualizada correctamente!")

                self.ventanaDialogo.exec_()

            self.file = open('datos/users.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                if linea == '':
                    break
            self.file.close()

            self.hide()
            self.ventanaAnterior.show()

    def ok_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.levelActualizadoInter = "Avanzado"
        self.levelActualizadoPrin = "Intermedio"

        if (self.levelU == "Intermedio"):
            self.file = open('datos/users.txt', 'rb')
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(";")
                # Separa si ya no hay mas registros en el archivo
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
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
                    lista[9],
                    lista[10],
                    lista[11]
                )
                # metemos el objeto en la lista de usuarios:
                usuarios.append(u)

            # cerramos el archivo
            self.file.close()

            self.file = open('datos/users.txt', 'wb')

            for u in usuarios:
                self.file.write(bytes(self.fecha.text() + ";"
                                      + self.fullname + ";"
                                      + self.user + ";"
                                      + self.password + ";"
                                      + self.password2 + ";"
                                      + self.alturaU + ";"
                                      + self.peso + ";"
                                      + self.vecesEntrenoAnterior + ";"
                                      + self.plan + ";"
                                      + self.disease + ";"
                                      + self.imc + ";"
                                      + self.levelActualizadoInter, encoding='UTF-8'))
            self.file.close()

            self.mensaje.setText("Puedes continuar tu entrenamiento en el nivel AVANZADO.\n"
                                 "Recuerda escuchar a tu cuerpo y ajustar la intensidad según tus\n"
                                 "necesidades y comodidad. ¡Estamos aquí para apoyarte en tu \n"
                                 "camino hacia un estilo de vida saludable!")
            self.ventanaDialogo.exec_()

        if (self.levelU == "Principiante"):
            self.file = open('datos/users.txt', 'rb')
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(";")
                # Separa si ya no hay mas registros en el archivo
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
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
                    lista[9],
                    lista[10],
                    lista[11]
                )
                # metemos el objeto en la lista de usuarios:
                usuarios.append(u)

            # cerramos el archivo
            self.file.close()

            self.file = open('datos/users.txt', 'wb')

            for u in usuarios:
                self.file.write(bytes(self.fecha.text() + ";"
                                      + self.fullname + ";"
                                      + self.user + ";"
                                      + self.password + ";"
                                      + self.password2 + ";"
                                      + self.alturaU + ";"
                                      + self.peso + ";"
                                      + self.vecesEntrenoAnterior + ";"
                                      + self.plan + ";"
                                      + self.disease + ";"
                                      + self.imc + ";"
                                      + self.levelActualizadoPrin, encoding='UTF-8'))
            self.file.close()

            self.mensaje.setText("Puedes continuar tu entrenamiento en el nivel INTERMEDIO.\n"
                                 "Recuerda escuchar a tu cuerpo y ajustar la intensidad según tus\n"
                                 "necesidades y comodidad. ¡Estamos aquí para apoyarte en tu \n"
                                 "camino hacia un estilo de vida saludable!")
            self.ventanaDialogo.exec_()

    def ok_opcion2(self):
        self.ventanaDialogoEliminar.close()
        self.levelActualizadoInter = "Principante"
        self.levelActualizadoAvan = "Intermedio"

        if (self.levelU == "Intermedio"):
            self.file = open('datos/users.txt', 'rb')
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(";")
                # Separa si ya no hay mas registros en el archivo
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
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
                    lista[9],
                    lista[10],
                    lista[11]
                )
                # metemos el objeto en la lista de usuarios:
                usuarios.append(u)

            # cerramos el archivo
            self.file.close()

            self.file = open('datos/users.txt', 'wb')

            for u in usuarios:
                self.file.write(bytes(self.fecha.text() + ";"
                                      + self.fullname + ";"
                                      + self.user + ";"
                                      + self.password + ";"
                                      + self.password2 + ";"
                                      + self.alturaU + ";"
                                      + self.peso + ";"
                                      + self.vecesEntrenoAnterior + ";"
                                      + self.plan + ";"
                                      + self.disease + ";"
                                      + self.imc + ";"
                                      + self.levelActualizadoInter, encoding='UTF-8'))
            self.file.close()

            self.mensaje.setText("Puedes continuar tu entrenamiento en el nivel PRINCIPIANTE.\n"
                                 "Recuerda escuchar a tu cuerpo y ajustar la intensidad según tus\n"
                                 "necesidades y comodidad. ¡Estamos aquí para apoyarte en tu \n"
                                 "camino hacia un estilo de vida saludable!")
            self.ventanaDialogo.exec_()

        if (self.levelU == "Avanzado"):
            self.file = open('datos/users.txt', 'rb')
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(";")
                # Separa si ya no hay mas registros en el archivo
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
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
                    lista[9],
                    lista[10],
                    lista[11]
                )
                # metemos el objeto en la lista de usuarios:
                usuarios.append(u)

            # cerramos el archivo
            self.file.close()

            self.file = open('datos/users.txt', 'wb')

            for u in usuarios:
                self.file.write(bytes(self.fecha.text() + ";"
                                      + self.fullname + ";"
                                      + self.user + ";"
                                      + self.password + ";"
                                      + self.password2 + ";"
                                      + self.alturaU + ";"
                                      + self.peso + ";"
                                      + self.vecesEntrenoAnterior + ";"
                                      + self.plan + ";"
                                      + self.disease + ";"
                                      + self.imc + ";"
                                      + self.levelActualizadoAvan, encoding='UTF-8'))
            self.file.close()

            self.mensaje.setText("Puedes continuar tu entrenamiento en el nivel INTERMEDIO.\n"
                                 "Recuerda escuchar a tu cuerpo y ajustar la intensidad según tus\n"
                                 "necesidades y comodidad. ¡Estamos aquí para apoyarte en tu \n"
                                 "camino hacia un estilo de vida saludable!")
            self.ventanaDialogo.exec_()

    def cancel_opcion(self):
        self.ventanaDialogoEliminar.close()