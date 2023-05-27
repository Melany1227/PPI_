from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from datetime import date
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QHBoxLayout, QWidget, QVBoxLayout, QGridLayout, QPushButton, \
    QFormLayout, QLineEdit, QLabel, QDateEdit


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

        self.UiComponents()

        self.title = QLabel("Registrar mis datos")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; font-weight: bold;")
        self.cuadricula.addWidget(self.title, 0, 0, 1, 3)

        self.height = QtWidgets.QLabel('Estatura')
        self.height.setAlignment(Qt.AlignCenter)
        self.height.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.height, 2, 0)

        self.height_edit = QtWidgets.QLineEdit(self)
        self.height_edit.setAlignment(Qt.AlignCenter)
        self.height_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.height_edit, 2, 1)

        self.weight = QtWidgets.QLabel('Peso')
        self.weight.setAlignment(Qt.AlignCenter)
        self.weight.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.weight, 3, 0)

        self.weight_edit = QtWidgets.QLineEdit(self)
        self.weight_edit.setAlignment(Qt.AlignCenter)
        self.weight_edit.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.cuadricula.addWidget(self.weight_edit, 3, 1)


        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
             "color: white; font-size: 18px; font-family: Poppins; padding: 8px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.botonVolver.clicked.connect(self.volver)
        self.cuadricula.addWidget(self.botonVolver, 5, 0)
        # method for components

    def UiComponents(self):

        # creating a label
        self.label = QLabel("Fecha del registro: ", self)
        self.label.setStyleSheet("color: white; font-size: 20px; font-family: Poppins;")
        self.label.setGeometry(100, 150, 200, 60)
        self.label.setAlignment(Qt.AlignCenter)
        self.cuadricula.addWidget(self.label, 1, 0)

        # creating a QDateEdit widget
        self.date = QDateEdit(self)
        # setting geometry of the date edit
        self.date.setGeometry(100, 100, 150, 40)
        self.date.setStyleSheet("color: white; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid #FFFFFF; ")
        self.date.setAlignment(Qt.AlignCenter)
        self.cuadricula.addWidget(self.date, 1, 1)

        # making label multiline
        self.label.setWordWrap(True)

        # adding action to the date when enter key is pressed
        self.date.editingFinished.connect(lambda: date_method())

        # method called by date edit
        def date_method():
            # getting the date
            self.value = self.date.date()



    def volver(self):
        self.hide()
        self.ventanaAnterior.show()
