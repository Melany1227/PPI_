import math
import sys

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFormLayout, QApplication, QLineEdit, QDialog, \
    QDialogButtonBox, QVBoxLayout, QPushButton, QWidget, QButtonGroup, QScrollArea, QGridLayout, QTableWidgetItem, \
    QTableWidget

from interfaz_plan_espalda import Ventana9_3
from interfaz_plan_pecho import Ventana9_2
from interfaz_plan_pierna import Ventana9_1
from lista_ejercicio import Ventana7_1, Ventana7_2, Ventana7_3, Ventana7_4, Ventana7_5, Ventana7_6, Ventana7_7, \
    Ventana7_8, Ventana7_9, Ventana7_10, Ventana7_11


class Ventana9(QMainWindow):

    def __init__(self, anterior, nombre_usuario):
        super(Ventana9, self).__init__(anterior)
        self.ventanaAnterior = anterior

        self.nombreUsuario = nombre_usuario

        self.setWindowTitle("HELP TRAINING")
        self.setWindowIcon(QIcon("imagenes/img_1.png"))
        self.setStyleSheet("background-color: black;")

        self.ancho = 1000
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

        self.letrero1 = QLabel()

        self.letrero1.setText("Plan Mensual")

        self.letrero1.setFont(QFont("Poppins", 30))

        self.letrero1.setAlignment(Qt.AlignCenter)

        self.letrero1.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; font-weight: bold;")

        self.vertical.addWidget(self.letrero1)

        # AGREGAR LA TABLA AQUÍ
        self.tableWidget = QTableWidget(7, 7)  # Cambiar el número de filas a 7
        self.tableWidget.setColumnCount(7)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setHorizontalHeaderLabels(
            ['Jueves', 'Viernes', 'Sábado', 'Domingo', 'Lunes', 'Martes', 'Miercoles'])
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)

        date = QDate.currentDate()
        day = 1
        for row in range(7):  # Cambiar el número de filas a 7
            for col in range(7):
                # Crear un QTableWidgetItem para cada celda
                item = QTableWidgetItem()
                item.setTextAlignment(Qt.AlignCenter)

                # Obtener el nombre del día de la semana y el número del día del mes
                dayOfMonth = str(date.addDays(day - 1).day())

                # Agregar texto y botón a la celda
                text = dayOfMonth

                # Definir las etiquetas personalizadas para cada botón de la semana
                if col == 0:
                    button_text = "Pierna"
                    # self.col.clicked.connect(self.abrirVentanaPierna)
                elif col == 1:
                    button_text = "Pecho"
                elif col == 2:
                    button_text = "Espalda"
                elif col == 3:
                    button_text = "Pecho"
                elif col == 4:
                    button_text = "Pierna"
                elif col == 5:
                    button_text = "Espalda"
                elif col == 6:
                    button_text = "Aleatorio"
                else:
                    button_text = " "

                # Agregar texto y botón a la celda
                # Agregar texto y botón a la celda
                button = QPushButton(button_text)
                button.setObjectName(f"button-{row}-{col}")  # Establecer un nombre de objeto para el QPushButton
                button.setFixedSize(99, 30)  # Establecer el tamaño fijo del botón

                layout = QVBoxLayout()
                label_day = QLabel(text)
                label_day.setObjectName("day-label")  # Establecer un nombre de objeto para el QLabel
                layout.addWidget(label_day)
                if button_text == "Pierna":
                    button.clicked.connect(self.abrirVentanaPierna)
                elif button_text == "Pecho":
                    button.clicked.connect(self.abrirVentanaPecho)
                elif button_text == "Espalda":
                    button.clicked.connect(self.abrirVentanaEspalda)
                layout.addWidget(button)

                widget = QWidget()
                widget.setLayout(layout)
                self.tableWidget.setCellWidget(row, col, widget)

                day += 1

        self.vertical.addWidget(self.tableWidget)

        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()

        self.tableWidget.setStyleSheet("""
            QLabel#day-label {
                font-family: Poppins;
                font-size: 20px;
                color: white;
            }
            QPushButton {
                color: white;
                font-size: 14px;
                font-family: Poppins;
                background-color: #334455;
                border: 1px solid #FFFFFF;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                color: red;
            }
        """)

        '''
        # Crear una QTableWidget con 7 columnas (días de la semana) y 4 filas (semanas)
        self.tableWidget = QTableWidget(4,  7)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setColumnWidth(0, 123)
        self.tableWidget.setColumnWidth(1, 123)
        self.tableWidget.setColumnWidth(2, 124)
        self.tableWidget.setColumnWidth(3, 123)
        self.tableWidget.setColumnWidth(4, 123)
        self.tableWidget.setColumnWidth(5, 124)
        self.tableWidget.setColumnWidth(6, 124)
        self.tableWidget.setHorizontalHeaderLabels(['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)

        date = QDate.currentDate()
        day = 1
        for row in range(4):
            for col in range(7):
                # Crear un QTableWidgetItem para cada celda
                item = QTableWidgetItem()
                item.setTextAlignment(Qt.AlignCenter)


                # Obtener el nombre del día de la semana y el número del día del mes
                dayOfWeek = date.addDays(day - 1).toString("dddd")
                dayOfMonth = str(date.addDays(day - 1).day())

                # Agregar texto y botón a la celda
                text = f"{dayOfWeek}\n{dayOfMonth}"
                button = QLabel("Botón")

                layout = QVBoxLayout()
                label_day = QLabel(text)
                label_day.setObjectName("day-label")  # Establecer un nombre de objeto para el QLabel
                layout.addWidget(label_day)
                layout.addWidget(button)

                widget = QWidget()
                widget.setLayout(layout)
                self.tableWidget.setCellWidget(row, col, widget)

                day += 1
        self.vertical.addWidget(self.tableWidget)

        self.tableWidget.resizeRowToContents(row)

        self.tableWidget.resizeColumnToContents(col)
        self.tableWidget.setStyleSheet("""
            QLabel#day-label {
                font-family: Poppins;
                font-size: 20px;
                color: white;

            }
        """)


        self.vertical.addStretch()
        '''

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.volver)

        self.vertical.addWidget(self.botonVolver)
        self.interna.setLayout(self.vertical)

    def abrirVentanaPierna(self):
        self.interfaz_plan_pierna = Ventana9_1(self)
        self.interfaz_plan_pierna.show()
        self.hide()

    def abrirVentanaPecho(self):
        self.interfaz_plan_pecho = Ventana9_2(self)
        self.interfaz_plan_pecho.show()
        self.hide()

    def abrirVentanaEspalda(self):
        self.interfaz_plan_espalda = Ventana9_3(self)
        self.interfaz_plan_espalda.show()
        self.hide()

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()