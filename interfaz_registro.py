from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPixmap, QFont, QFontDatabase, QIcon
from PyQt5.QtWidgets import QLabel, QDesktopWidget, QMainWindow, QWidget, QFormLayout, QVBoxLayout, QGridLayout, \
    QDialog, QDialogButtonBox, QPushButton, QComboBox



class Ventana4 (QMainWindow):

    def __init__(self, anterior):
        super(Ventana4, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.setWindowTitle("HELP TRAINING")
        self.setWindowIcon(QIcon("imagenes/img_1.png"))
        self.setStyleSheet("background-color: black;")
        self.ancho = 1200
        self.alto = 850
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

        self.fullname_label = QtWidgets.QLabel('Nombre completo')
        self.fullname_label.setAlignment(Qt.AlignCenter)
        self.fullname_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.fullname_label, 2, 0)

        self.fullname_edit = QtWidgets.QLineEdit(self)
        self.fullname_edit.setAlignment(Qt.AlignCenter)
        self.fullname_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.fullname_edit, 2, 1)

        self.user_label = QtWidgets.QLabel('Usuario')
        self.user_label.setAlignment(Qt.AlignCenter)
        self.user_label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.user_label, 3, 0)

        self.user_edit = QtWidgets.QLineEdit(self)
        self.user_edit.setAlignment(Qt.AlignCenter)
        self.user_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.user_edit, 3, 1)


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

        self.password2_label = QtWidgets.QLabel('Confirmar\ncontraseña')
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

        self.disease = QtWidgets.QLabel('¿Tienes alguna de estas\n'
                                        ' enfermedades ?')
        self.disease.setAlignment(Qt.AlignCenter)
        self.disease.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.disease, 5, 3)

        self.disease_resp = QComboBox()
        self.disease_resp.addItems(
            ["", "Enfermedades metabológicas", "Enfermedades respiratorias", "Enfermedades cardíacas",
             "Enfermedades neurológicas", "Enfermedades óseas", "Ninguna"])
        self.disease_resp.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.disease_resp, 5, 4)

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
        self.botonLimpiar.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
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

    def limpiar(self):
        self.fullname_edit.setText('')
        self.user_edit.setText('')
        self.password2_edit.setText('')
        self.password_edit.setText('')
        self.height_edit.setText('')
        self.weight_edit.setText('')
        self.nivel_resp.setCurrentText('')
        self.plan_resp.setCurrentText('')
        self.disease_resp.setCurrentText('')


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
                or self.height_edit.text() == ''
                or self.weight_edit.text() == ''
                or self.nivel_resp.currentText() == ''
                or self.plan_resp.currentText() == ''
                or self.disease_resp.currentText() == ''


        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debe llenar todos los campos")
            self.ventanaDialogo.exec_()
            self.ventanaAnterior.show()


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

        if (
                not self.height_edit.text().isnumeric()
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("La altura debe ser numérica.")

            # hacemos que la ventanaDIalogo se vea:
            self.ventanaDialogo.exec_()

            # limpiamos el campo del documento:
            self.height_edit.setText('')


        # Si los datos están correctos:
        if self.datosCorrectos:

            # Abrimos el archivo en modo agregar escribiendo datos en binario.
            self.file = open('datos/users.txt', 'ab')

            # traer el texto de los QLineEdit() y los agrega concatenandolos.
            # para escribirlos en el archivo en formato binario utf-8
            self.file.write(bytes(
                self.fecha.text() + ";"
                + self.fullname_edit.text() + ";"
                + self.user_edit.text() + ";"
                + self.password2_edit.text() + ";"
                + self.password_edit.text() + ";"
                + self.height_edit.text() + ";"
                + self.weight_edit.text() + ";"
                + self.nivel_resp.currentText() + ";"
                + self.plan_resp.currentText() + ";"
                + self.disease_resp.currentText() + "\n"
                , encoding='UTF-8'))
            self.file.close()

            self.file = open('datos/users.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

            if (self.disease_resp.currentText() != 'Ninguna'):
                self.mensaje.setText("Antes de comenzar cualquier programa de actividad física, \n"
                                     "es fundamental que consulte a su médico o especialista. \n"
                                     "El médico podrá evaluar su condición de salud actual, \n"
                                     "los riesgos y las limitaciones específicas, y así, \n"
                                     "brindar recomendaciones personalizadas.")

                # Hacemos que la ventana de dialogo se vea:
                self.ventanaDialogo.exec_()

            # ---- CALCULAR IMC ----

            self.peso = float(self.weight_edit.text())

            self.altura = float(self.height_edit.text())

            self.imc = float(self.peso / ((self.altura / 100) ** 2))

            # ---- CONTADOR: NIVEL ----

            self.contadorPri = 0
            self.contadorInt = 0
            self.contadorAv = 0

            self.nv = int(self.nivel_resp.currentText())


            if (self.nv <= 2):
                self.contadorPri += 1

            if (self.nv == 3 or self.nv == 4):
                self.contadorInt += 1

            if (self.nv >= 5):
                self.contadorAv += 1

            self.planl = int(self.plan_resp.currentText())

            if (self.planl <= 2):
                self.contadorPri += 1

            if (self.planl == 3 or self.planl == 4):
                self.contadorInt += 1

            if (self.planl >= 5):
                self.contadorAv += 1

            # ---- MOSTRAR MENSAJE IMC ----

            if (self.imc < 18.5):
                self.mensaje.setText(f"Su indice de masa corporal es: {self.imc:.2f} \nBajo peso")
                self.ventanaDialogo.exec_()
                self.contadorPri += 1

            if (self.imc >= 18.5 and self.imc <= 24.9):
                self.mensaje.setText(f"Su indice de masa corporal es: {self.imc:.2f}\nFelicidades, tu IMC se encuentra dentro del rango saludable.\nContinúa manteniendo hábitos saludables para mantener tu bienestar.")
                self.ventanaDialogo.exec_()
                self.contadorInt += 1

            if (self.imc >= 25.0 and self.imc <= 29.9):
                self.mensaje.setText(f"Su indice de masa corporal es: {self.imc:.2f}\nSegún tu IMC, estás en la categoría de sobrepeso. Recuerda\nque llevar una alimentación equilibrada y realizar actividad\nfísica regularmente pueden ayudarte a mejorar tu salud.")
                self.ventanaDialogo.exec_()
                self.contadorPri += 1

            if (self.imc >= 30.0):
                self.mensaje.setText(f"Su indice de masa corporal es: {self.imc:.2f}\nDe acuerdo con tu IMC, estás en la categoría de obesidad.\nTe recomendamos consultar a un profesional de la salud para\nrecibir orientación personalizada y establecer metas de salud adecuadas.")
                self.ventanaDialogo.exec_()
                self.contadorPri += 1


            # ---- MENSAJE NIVEL ----

            if (self.contadorPri > self.contadorInt and self.contadorPri > self.contadorAv):
                self.mensaje.setText("Te recomendamos iniciar tu entrenamiento en el nivel PRINCIPIANTE.\n"
                                     "Recuerda escuchar a tu cuerpo y ajustar la intensidad según tus\n"
                                     "necesidades y comodidad. ¡Estamos aquí para apoyarte en tu \n"
                                     "camino hacia un estilo de vida saludable!")
                self.ventanaDialogo.exec_()

            if ((self.contadorInt > self.contadorPri and self.contadorInt > self.contadorAv)
                    or (self.contadorAv == self.contadorPri == self.contadorInt)):
                self.mensaje.setText("Te recomendamos iniciar tu entrenamiento en el nivel INTERMEDIO.\n"
                                     "Recuerda escuchar a tu cuerpo y ajustar la intensidad según tus\n"
                                     "necesidades y comodidad. ¡Estamos aquí para apoyarte en tu \n"
                                     "camino hacia un estilo de vida saludable!")
                self.ventanaDialogo.exec_()

            if (self.contadorAv > self.contadorPri and self.contadorAv > self.contadorInt):
                self.mensaje.setText("Te recomendamos iniciar tu entrenamiento en el nivel AVANZADO.\n"
                                     "Recuerda escuchar a tu cuerpo y ajustar la intensidad según tus\n"
                                     "necesidades y comodidad. ¡Estamos aquí para apoyarte en tu \n"
                                     "camino hacia un estilo de vida saludable!")
                self.ventanaDialogo.exec_()


            self.mensaje.setText("Se ha registrado correctamente.")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

            self.hide()
            self.ventanaAnterior.show()


