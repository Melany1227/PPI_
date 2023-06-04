from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFontDatabase, QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, \
    QPushButton, QMainWindow, QToolBar, QAction, QGridLayout, QHBoxLayout
import sys  # Funcionalidades del sistema
class Ventana7_1(QMainWindow): #Cuadriceps

    def __init__(self, anterior):
        super(Ventana7_1, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.setWindowTitle("Cuadriceps")

        self.setStyleSheet('background-color: black;')

        self.ancho = 1000
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)


        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)



        self.interna = QWidget()
        self.interna.setContentsMargins(0, 0, 0, 20)

        self.setCentralWidget(self.interna)

        self.cuadricula = QGridLayout()

        self.interna.setLayout(self.cuadricula)


        self.interna.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; border-radius:2px;"
                                   "border: 3px solid 	#000000;")

        self.label = QLabel("CUADRICEPS")
        self.label.setAlignment(Qt.AlignHCenter)  # Centra horizontalmente el contenido interno
        self.label.setStyleSheet('font-size: 60px;color: white; border: 5px double lightcoral; text-stroke: 2px gold;')
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.cuadricula.addWidget(self.widget, 0, 2, 1, 6)

        # Crea la barra de herramientas
        self.barraHerramientas = QToolBar("Barra de herramientas")
        # Agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)

        self.barraHerramientas.setOrientation(Qt.Vertical)

        self.barraHerramientas.setStyleSheet("color: white; font-size: 25px;border-radius:2px; "
                                             "border: 1px solid lightcoral;")
        # Tamaño de los iconos
        self.barraHerramientas.setIconSize(QSize(80, 100))

        # Creamos la opcion para la expresión 1
        self.exp1 = QAction(QIcon("imagenes/principiante.png"), "PRINCIPIANTE", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp2 = QAction(QIcon("imagenes/intermedio.png"), "INTERMEDIO", self)
        self.barraHerramientas.addAction(self.exp2)

        self.exp3 = QAction(QIcon("imagenes/avanzado2.png"), "AVANZADO", self)
        self.barraHerramientas.addAction(self.exp3)

        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)

        self.cuadricula.addWidget(self.barraHerramientas, 0, 0, 5, 4)



        self.cuadricula.addWidget(QLabel("Fortalece y tonifica tus cuádriceps con sentadillas efectivas:"
                                         "\n el ejercicio clave para unas piernas fuertes y esculpidas."
                                         "\n Las sentadillas son una excelente manera de trabajar"
                                         "\n los músculos de tus piernas, especialmente los cuádriceps."), 1, 2, 1, 6)





        self.cuadricula.addWidget(QLabel("Selecciona el nivel de dificultad"
                                         "\n sugerido"
                                         "\n(Puedes escoger cualquier nivel)"), 2, 2, 1, 6)



        self.imagenSentadilla = QLabel()
        self.imagenSentadilla.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/ejercicio_sentadilla.png")
        self.imagenSentadilla.setFixedSize(400, 250)
        self.imagenSentadilla.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagenSentadilla, 2, 7, 3, 1)



        self.botonVolver = QPushButton("VOLVER")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.volver)



        self.cuadricula.addWidget(self.botonVolver, 4, 2)
    def accion_barraHerramientas(self, opcion):
        self.hide()

        if opcion.text() == "Exp 1":
            pass

        #  self.ventana2 = Ventana2(self)
        # self.ventana2.show()

        if opcion.text() == "Exp 2":
            pass

        #   self.ventana = Ventana3(self)
        #  self.ventana3.show()

        if opcion.text() == "Exp 3":
            pass

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()## u
class Ventana7_2(QMainWindow):

    def __init__(self, anterior):
        super(Ventana7_2, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.setWindowTitle("Glúteo")

        self.setStyleSheet('background-color: black;')

        self.ancho = 1000
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)


        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)



        self.interna = QWidget()
        self.interna.setContentsMargins(0, 0, 0, 20)

        self.setCentralWidget(self.interna)

        self.cuadricula = QGridLayout()

        self.interna.setLayout(self.cuadricula)


        self.interna.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; border-radius:2px;"
                                   "border: 3px solid 	#000000;")

        self.label = QLabel("GLUTEO")
        self.label.setAlignment(Qt.AlignHCenter)  # Centra horizontalmente el contenido interno
        self.label.setStyleSheet('font-size: 60px;color: white; border: 5px double lightcoral; text-stroke: 2px gold;')
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.cuadricula.addWidget(self.widget, 0, 2, 1, 6)

        # Crea la barra de herramientas
        self.barraHerramientas = QToolBar("Barra de herramientas")
        # Agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)

        self.barraHerramientas.setOrientation(Qt.Vertical)

        self.barraHerramientas.setStyleSheet("color: white; font-size: 8px;border-radius:2px; "
                                             "border: 1px solid lightcoral;")
        # Tamaño de los iconos
        self.barraHerramientas.setIconSize(QSize(80, 100))

        # Creamos la opcion para la expresión 1
        self.exp1 = QAction(QIcon("imagenes/principiante.png"), "PRINCIPIANTE", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp2 = QAction(QIcon("imagenes/intermedio.png"), "INTERMEDIO", self)
        self.barraHerramientas.addAction(self.exp2)

        self.exp3 = QAction(QIcon("imagenes/avanzado2.png"), "AVANZADO", self)
        self.barraHerramientas.addAction(self.exp3)
        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)
        self.cuadricula.addWidget(self.barraHerramientas, 0, 0, 5, 4)
        self.cuadricula.addWidget(QLabel("Elevación de cadera o Puente de glúteos: Colócate en el suelo"
                                         "\n boca arriba, con las rodillas flexionadas y los pies"
                                         "\n apoyados en el suelo, separados al ancho de las caderas."
                                         "\n Asegúrate de que los brazos estén extendidos a lo largo"
                                         "\n del cuerpo. Desde esta posición, presiona "
                                         "\n los talones en el suelo y levanta lentamente las caderas"
                                         "\n hacia arriba, contrayendo los glúteos. "), 1, 2, 1, 6)
        self.cuadricula.addWidget(QLabel("Selecciona el nivel de dificultad"
                                         "\n sugerido"
                                         "\n(Puedes escoger cualquier nivel)"), 2, 2, 1, 6)
        self.imagenSentadilla = QLabel()
        self.imagenSentadilla.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/sentadilla.png")
        self.imagenSentadilla.setFixedSize(400, 250)
        self.imagenSentadilla.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagenSentadilla, 2, 7, 3, 1)



        self.botonVolver = QPushButton("VOLVER")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px; text-decoration: underline #ff6565;")
        self.botonVolver.clicked.connect(self.volver)



        self.cuadricula.addWidget(self.botonVolver, 4, 2)





    def accion_barraHerramientas(self, opcion):
        self.hide()

        if opcion.text() == "Exp 1":
            pass

        #  self.ventana2 = Ventana2(self)
        # self.ventana2.show()

        if opcion.text() == "Exp 2":
            pass

        #   self.ventana = Ventana3(self)
        #  self.ventana3.show()

        if opcion.text() == "Exp 3":
            pass

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()
class Ventana7_3(QMainWindow):

    def __init__(self, anterior):
        super(Ventana7_3, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.setWindowTitle("Cuadriceps")

        self.setStyleSheet('background-color: black;')

        self.ancho = 1000
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)


        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)



        self.interna = QWidget()
        self.interna.setContentsMargins(0, 0, 0, 20)

        self.setCentralWidget(self.interna)

        self.cuadricula = QGridLayout()

        self.interna.setLayout(self.cuadricula)


        self.interna.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; border-radius:2px;"
                                   "border: 3px solid 	#000000;")

        self.label = QLabel("CUADRICEPS")
        self.label.setAlignment(Qt.AlignHCenter)  # Centra horizontalmente el contenido interno
        self.label.setStyleSheet('font-size: 60px;color: white; border: 5px double lightcoral; text-stroke: 2px gold;')
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.cuadricula.addWidget(self.widget, 0, 2, 1, 6)

        # Crea la barra de herramientas
        self.barraHerramientas = QToolBar("Barra de herramientas")
        # Agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)

        self.barraHerramientas.setOrientation(Qt.Vertical)

        self.barraHerramientas.setStyleSheet("color: white; font-size: 25px;border-radius:2px; "
                                             "border: 1px solid lightcoral;")
        # Tamaño de los iconos
        self.barraHerramientas.setIconSize(QSize(80, 100))

        # Creamos la opcion para la expresión 1
        self.exp1 = QAction(QIcon("imagenes/principiante.png"), "PRINCIPIANTE", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp2 = QAction(QIcon("imagenes/intermedio.png"), "INTERMEDIO", self)
        self.barraHerramientas.addAction(self.exp2)

        self.exp3 = QAction(QIcon("imagenes/avanzado2.png"), "AVANZADO", self)
        self.barraHerramientas.addAction(self.exp3)

        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)

        self.cuadricula.addWidget(self.barraHerramientas, 0, 0, 5, 4)



        self.cuadricula.addWidget(QLabel("Fortalece y tonifica tus cuádriceps con sentadillas efectivas:"
                                         "\n el ejercicio clave para unas piernas fuertes y esculpidas."
                                         "\n Las sentadillas son una excelente manera de trabajar"
                                         "\n los músculos de tus piernas, especialmente los cuádriceps."), 1, 2, 1, 6)





        self.cuadricula.addWidget(QLabel("Selecciona el nivel de dificultad"
                                         "\n sugerido"
                                         "\n(Puedes escoger cualquier nivel)"), 2, 2, 1, 6)



        self.imagenSentadilla = QLabel()
        self.imagenSentadilla.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/sentadilla.png")
        self.imagenSentadilla.setFixedSize(400, 250)
        self.imagenSentadilla.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagenSentadilla, 2, 7, 3, 1)



        self.botonVolver = QPushButton("VOLVER")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.volver)



        self.cuadricula.addWidget(self.botonVolver, 4, 2)





    def accion_barraHerramientas(self, opcion):
        self.hide()

        if opcion.text() == "Exp 1":
            pass

        #  self.ventana2 = Ventana2(self)
        # self.ventana2.show()

        if opcion.text() == "Exp 2":
            pass

        #   self.ventana = Ventana3(self)
        #  self.ventana3.show()

        if opcion.text() == "Exp 3":
            pass

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()
class Ventana7_4(QMainWindow):

    def __init__(self, anterior):
        super(Ventana7_4, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.setWindowTitle("Cuadriceps")

        self.setStyleSheet('background-color: black;')

        self.ancho = 1000
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)


        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)



        self.interna = QWidget()
        self.interna.setContentsMargins(0, 0, 0, 20)

        self.setCentralWidget(self.interna)

        self.cuadricula = QGridLayout()

        self.interna.setLayout(self.cuadricula)


        self.interna.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; border-radius:2px;"
                                   "border: 3px solid 	#000000;")

        self.label = QLabel("CUADRICEPS")
        self.label.setAlignment(Qt.AlignHCenter)  # Centra horizontalmente el contenido interno
        self.label.setStyleSheet('font-size: 60px;color: white; border: 5px double lightcoral; text-stroke: 2px gold;')
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.cuadricula.addWidget(self.widget, 0, 2, 1, 6)

        # Crea la barra de herramientas
        self.barraHerramientas = QToolBar("Barra de herramientas")
        # Agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)

        self.barraHerramientas.setOrientation(Qt.Vertical)

        self.barraHerramientas.setStyleSheet("color: white; font-size: 25px;border-radius:2px; "
                                             "border: 1px solid lightcoral;")
        # Tamaño de los iconos
        self.barraHerramientas.setIconSize(QSize(80, 100))

        # Creamos la opcion para la expresión 1
        self.exp1 = QAction(QIcon("imagenes/principiante.png"), "PRINCIPIANTE", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp2 = QAction(QIcon("imagenes/intermedio.png"), "INTERMEDIO", self)
        self.barraHerramientas.addAction(self.exp2)

        self.exp3 = QAction(QIcon("imagenes/avanzado2.png"), "AVANZADO", self)
        self.barraHerramientas.addAction(self.exp3)

        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)

        self.cuadricula.addWidget(self.barraHerramientas, 0, 0, 5, 4)



        self.cuadricula.addWidget(QLabel("Fortalece y tonifica tus cuádriceps con sentadillas efectivas:"
                                         "\n el ejercicio clave para unas piernas fuertes y esculpidas."
                                         "\n Las sentadillas son una excelente manera de trabajar"
                                         "\n los músculos de tus piernas, especialmente los cuádriceps."), 1, 2, 1, 6)





        self.cuadricula.addWidget(QLabel("Selecciona el nivel de dificultad"
                                         "\n sugerido"
                                         "\n(Puedes escoger cualquier nivel)"), 2, 2, 1, 6)



        self.imagenSentadilla = QLabel()
        self.imagenSentadilla.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/sentadilla.png")
        self.imagenSentadilla.setFixedSize(400, 250)
        self.imagenSentadilla.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagenSentadilla, 2, 7, 3, 1)



        self.botonVolver = QPushButton("VOLVER")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.volver)



        self.cuadricula.addWidget(self.botonVolver, 4, 2)





    def accion_barraHerramientas(self, opcion):
        self.hide()

        if opcion.text() == "Exp 1":
            pass

        #  self.ventana2 = Ventana2(self)
        # self.ventana2.show()

        if opcion.text() == "Exp 2":
            pass

        #   self.ventana = Ventana3(self)
        #  self.ventana3.show()

        if opcion.text() == "Exp 3":
            pass

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()
class Ventana7_5(QMainWindow):

    def __init__(self, anterior):
        super(Ventana7_5, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.setWindowTitle("Cuadriceps")

        self.setStyleSheet('background-color: black;')

        self.ancho = 1000
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)


        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)



        self.interna = QWidget()
        self.interna.setContentsMargins(0, 0, 0, 20)

        self.setCentralWidget(self.interna)

        self.cuadricula = QGridLayout()

        self.interna.setLayout(self.cuadricula)


        self.interna.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; border-radius:2px;"
                                   "border: 3px solid 	#000000;")

        self.label = QLabel("CUADRICEPS")
        self.label.setAlignment(Qt.AlignHCenter)  # Centra horizontalmente el contenido interno
        self.label.setStyleSheet('font-size: 60px;color: white; border: 5px double lightcoral; text-stroke: 2px gold;')
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.cuadricula.addWidget(self.widget, 0, 2, 1, 6)

        # Crea la barra de herramientas
        self.barraHerramientas = QToolBar("Barra de herramientas")
        # Agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)

        self.barraHerramientas.setOrientation(Qt.Vertical)

        self.barraHerramientas.setStyleSheet("color: white; font-size: 25px;border-radius:2px; "
                                             "border: 1px solid lightcoral;")
        # Tamaño de los iconos
        self.barraHerramientas.setIconSize(QSize(80, 100))

        # Creamos la opcion para la expresión 1
        self.exp1 = QAction(QIcon("imagenes/principiante.png"), "PRINCIPIANTE", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp2 = QAction(QIcon("imagenes/intermedio.png"), "INTERMEDIO", self)
        self.barraHerramientas.addAction(self.exp2)

        self.exp3 = QAction(QIcon("imagenes/avanzado2.png"), "AVANZADO", self)
        self.barraHerramientas.addAction(self.exp3)

        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)

        self.cuadricula.addWidget(self.barraHerramientas, 0, 0, 5, 4)



        self.cuadricula.addWidget(QLabel("Fortalece y tonifica tus cuádriceps con sentadillas efectivas:"
                                         "\n el ejercicio clave para unas piernas fuertes y esculpidas."
                                         "\n Las sentadillas son una excelente manera de trabajar"
                                         "\n los músculos de tus piernas, especialmente los cuádriceps."), 1, 2, 1, 6)





        self.cuadricula.addWidget(QLabel("Selecciona el nivel de dificultad"
                                         "\n sugerido"
                                         "\n(Puedes escoger cualquier nivel)"), 2, 2, 1, 6)



        self.imagenSentadilla = QLabel()
        self.imagenSentadilla.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/sentadilla.png")
        self.imagenSentadilla.setFixedSize(400, 250)
        self.imagenSentadilla.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagenSentadilla, 2, 7, 3, 1)



        self.botonVolver = QPushButton("VOLVER")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.volver)



        self.cuadricula.addWidget(self.botonVolver, 4, 2)





    def accion_barraHerramientas(self, opcion):
        self.hide()

        if opcion.text() == "Exp 1":
            pass

        #  self.ventana2 = Ventana2(self)
        # self.ventana2.show()

        if opcion.text() == "Exp 2":
            pass

        #   self.ventana = Ventana3(self)
        #  self.ventana3.show()

        if opcion.text() == "Exp 3":
            pass

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()
class Ventana7_6(QMainWindow):

    def __init__(self, anterior):
        super(Ventana7_6, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.setWindowTitle("Cuadriceps")

        self.setStyleSheet('background-color: black;')

        self.ancho = 1000
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)


        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)



        self.interna = QWidget()
        self.interna.setContentsMargins(0, 0, 0, 20)

        self.setCentralWidget(self.interna)

        self.cuadricula = QGridLayout()

        self.interna.setLayout(self.cuadricula)


        self.interna.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; border-radius:2px;"
                                   "border: 3px solid 	#000000;")

        self.label = QLabel("CUADRICEPS")
        self.label.setAlignment(Qt.AlignHCenter)  # Centra horizontalmente el contenido interno
        self.label.setStyleSheet('font-size: 60px;color: white; border: 5px double lightcoral; text-stroke: 2px gold;')
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.cuadricula.addWidget(self.widget, 0, 2, 1, 6)

        # Crea la barra de herramientas
        self.barraHerramientas = QToolBar("Barra de herramientas")
        # Agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)

        self.barraHerramientas.setOrientation(Qt.Vertical)

        self.barraHerramientas.setStyleSheet("color: white; font-size: 25px;border-radius:2px; "
                                             "border: 1px solid lightcoral;")
        # Tamaño de los iconos
        self.barraHerramientas.setIconSize(QSize(80, 100))

        # Creamos la opcion para la expresión 1
        self.exp1 = QAction(QIcon("imagenes/principiante.png"), "PRINCIPIANTE", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp2 = QAction(QIcon("imagenes/intermedio.png"), "INTERMEDIO", self)
        self.barraHerramientas.addAction(self.exp2)

        self.exp3 = QAction(QIcon("imagenes/avanzado2.png"), "AVANZADO", self)
        self.barraHerramientas.addAction(self.exp3)

        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)

        self.cuadricula.addWidget(self.barraHerramientas, 0, 0, 5, 4)



        self.cuadricula.addWidget(QLabel("Fortalece y tonifica tus cuádriceps con sentadillas efectivas:"
                                         "\n el ejercicio clave para unas piernas fuertes y esculpidas."
                                         "\n Las sentadillas son una excelente manera de trabajar"
                                         "\n los músculos de tus piernas, especialmente los cuádriceps."), 1, 2, 1, 6)





        self.cuadricula.addWidget(QLabel("Selecciona el nivel de dificultad"
                                         "\n sugerido"
                                         "\n(Puedes escoger cualquier nivel)"), 2, 2, 1, 6)



        self.imagenSentadilla = QLabel()
        self.imagenSentadilla.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/sentadilla.png")
        self.imagenSentadilla.setFixedSize(400, 250)
        self.imagenSentadilla.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagenSentadilla, 2, 7, 3, 1)



        self.botonVolver = QPushButton("VOLVER")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.volver)



        self.cuadricula.addWidget(self.botonVolver, 4, 2)





    def accion_barraHerramientas(self, opcion):
        self.hide()

        if opcion.text() == "Exp 1":
            pass

        #  self.ventana2 = Ventana2(self)
        # self.ventana2.show()

        if opcion.text() == "Exp 2":
            pass

        #   self.ventana = Ventana3(self)
        #  self.ventana3.show()

        if opcion.text() == "Exp 3":
            pass

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()
class Ventana7_7(QMainWindow):

    def __init__(self, anterior):
        super(Ventana7_7, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.setWindowTitle("Cuadriceps")

        self.setStyleSheet('background-color: black;')

        self.ancho = 1000
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)


        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)



        self.interna = QWidget()
        self.interna.setContentsMargins(0, 0, 0, 20)

        self.setCentralWidget(self.interna)

        self.cuadricula = QGridLayout()

        self.interna.setLayout(self.cuadricula)


        self.interna.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; border-radius:2px;"
                                   "border: 3px solid 	#000000;")

        self.label = QLabel("CUADRICEPS")
        self.label.setAlignment(Qt.AlignHCenter)  # Centra horizontalmente el contenido interno
        self.label.setStyleSheet('font-size: 60px;color: white; border: 5px double lightcoral; text-stroke: 2px gold;')
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.cuadricula.addWidget(self.widget, 0, 2, 1, 6)

        # Crea la barra de herramientas
        self.barraHerramientas = QToolBar("Barra de herramientas")
        # Agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)

        self.barraHerramientas.setOrientation(Qt.Vertical)

        self.barraHerramientas.setStyleSheet("color: white; font-size: 25px;border-radius:2px; "
                                             "border: 1px solid lightcoral;")
        # Tamaño de los iconos
        self.barraHerramientas.setIconSize(QSize(80, 100))

        # Creamos la opcion para la expresión 1
        self.exp1 = QAction(QIcon("imagenes/principiante.png"), "PRINCIPIANTE", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp2 = QAction(QIcon("imagenes/intermedio.png"), "INTERMEDIO", self)
        self.barraHerramientas.addAction(self.exp2)

        self.exp3 = QAction(QIcon("imagenes/avanzado2.png"), "AVANZADO", self)
        self.barraHerramientas.addAction(self.exp3)

        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)

        self.cuadricula.addWidget(self.barraHerramientas, 0, 0, 5, 4)



        self.cuadricula.addWidget(QLabel("Fortalece y tonifica tus cuádriceps con sentadillas efectivas:"
                                         "\n el ejercicio clave para unas piernas fuertes y esculpidas."
                                         "\n Las sentadillas son una excelente manera de trabajar"
                                         "\n los músculos de tus piernas, especialmente los cuádriceps."), 1, 2, 1, 6)





        self.cuadricula.addWidget(QLabel("Selecciona el nivel de dificultad"
                                         "\n sugerido"
                                         "\n(Puedes escoger cualquier nivel)"), 2, 2, 1, 6)



        self.imagenSentadilla = QLabel()
        self.imagenSentadilla.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/sentadilla.png")
        self.imagenSentadilla.setFixedSize(400, 250)
        self.imagenSentadilla.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagenSentadilla, 2, 7, 3, 1)



        self.botonVolver = QPushButton("VOLVER")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.volver)



        self.cuadricula.addWidget(self.botonVolver, 4, 2)





    def accion_barraHerramientas(self, opcion):
        self.hide()

        if opcion.text() == "Exp 1":
            pass

        #  self.ventana2 = Ventana2(self)
        # self.ventana2.show()

        if opcion.text() == "Exp 2":
            pass

        #   self.ventana = Ventana3(self)
        #  self.ventana3.show()

        if opcion.text() == "Exp 3":
            pass

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()
class Ventana7_8(QMainWindow):

    def __init__(self, anterior):
        super(Ventana7_8, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.setWindowTitle("Cuadriceps")

        self.setStyleSheet('background-color: black;')

        self.ancho = 1000
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)


        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)



        self.interna = QWidget()
        self.interna.setContentsMargins(0, 0, 0, 20)

        self.setCentralWidget(self.interna)

        self.cuadricula = QGridLayout()

        self.interna.setLayout(self.cuadricula)


        self.interna.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; border-radius:2px;"
                                   "border: 3px solid 	#000000;")

        self.label = QLabel("CUADRICEPS")
        self.label.setAlignment(Qt.AlignHCenter)  # Centra horizontalmente el contenido interno
        self.label.setStyleSheet('font-size: 60px;color: white; border: 5px double lightcoral; text-stroke: 2px gold;')
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.cuadricula.addWidget(self.widget, 0, 2, 1, 6)

        # Crea la barra de herramientas
        self.barraHerramientas = QToolBar("Barra de herramientas")
        # Agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)

        self.barraHerramientas.setOrientation(Qt.Vertical)

        self.barraHerramientas.setStyleSheet("color: white; font-size: 25px;border-radius:2px; "
                                             "border: 1px solid lightcoral;")
        # Tamaño de los iconos
        self.barraHerramientas.setIconSize(QSize(80, 100))

        # Creamos la opcion para la expresión 1
        self.exp1 = QAction(QIcon("imagenes/principiante.png"), "PRINCIPIANTE", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp2 = QAction(QIcon("imagenes/intermedio.png"), "INTERMEDIO", self)
        self.barraHerramientas.addAction(self.exp2)

        self.exp3 = QAction(QIcon("imagenes/avanzado2.png"), "AVANZADO", self)
        self.barraHerramientas.addAction(self.exp3)

        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)

        self.cuadricula.addWidget(self.barraHerramientas, 0, 0, 5, 4)



        self.cuadricula.addWidget(QLabel("Fortalece y tonifica tus cuádriceps con sentadillas efectivas:"
                                         "\n el ejercicio clave para unas piernas fuertes y esculpidas."
                                         "\n Las sentadillas son una excelente manera de trabajar"
                                         "\n los músculos de tus piernas, especialmente los cuádriceps."), 1, 2, 1, 6)





        self.cuadricula.addWidget(QLabel("Selecciona el nivel de dificultad"
                                         "\n sugerido"
                                         "\n(Puedes escoger cualquier nivel)"), 2, 2, 1, 6)



        self.imagenSentadilla = QLabel()
        self.imagenSentadilla.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/sentadilla.png")
        self.imagenSentadilla.setFixedSize(400, 250)
        self.imagenSentadilla.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagenSentadilla, 2, 7, 3, 1)



        self.botonVolver = QPushButton("VOLVER")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.volver)



        self.cuadricula.addWidget(self.botonVolver, 4, 2)





    def accion_barraHerramientas(self, opcion):
        self.hide()

        if opcion.text() == "Exp 1":
            pass

        #  self.ventana2 = Ventana2(self)
        # self.ventana2.show()

        if opcion.text() == "Exp 2":
            pass

        #   self.ventana = Ventana3(self)
        #  self.ventana3.show()

        if opcion.text() == "Exp 3":
            pass

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()
class Ventana7_9(QMainWindow):

    def __init__(self, anterior):
        super(Ventana7_9, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.setWindowTitle("Cuadriceps")

        self.setStyleSheet('background-color: black;')

        self.ancho = 1000
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)


        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)



        self.interna = QWidget()
        self.interna.setContentsMargins(0, 0, 0, 20)

        self.setCentralWidget(self.interna)

        self.cuadricula = QGridLayout()

        self.interna.setLayout(self.cuadricula)


        self.interna.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; border-radius:2px;"
                                   "border: 3px solid 	#000000;")

        self.label = QLabel("CUADRICEPS")
        self.label.setAlignment(Qt.AlignHCenter)  # Centra horizontalmente el contenido interno
        self.label.setStyleSheet('font-size: 60px;color: white; border: 5px double lightcoral; text-stroke: 2px gold;')
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.cuadricula.addWidget(self.widget, 0, 2, 1, 6)

        # Crea la barra de herramientas
        self.barraHerramientas = QToolBar("Barra de herramientas")
        # Agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)

        self.barraHerramientas.setOrientation(Qt.Vertical)

        self.barraHerramientas.setStyleSheet("color: white; font-size: 25px;border-radius:2px; "
                                             "border: 1px solid lightcoral;")
        # Tamaño de los iconos
        self.barraHerramientas.setIconSize(QSize(80, 100))

        # Creamos la opcion para la expresión 1
        self.exp1 = QAction(QIcon("imagenes/principiante.png"), "PRINCIPIANTE", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp2 = QAction(QIcon("imagenes/intermedio.png"), "INTERMEDIO", self)
        self.barraHerramientas.addAction(self.exp2)

        self.exp3 = QAction(QIcon("imagenes/avanzado2.png"), "AVANZADO", self)
        self.barraHerramientas.addAction(self.exp3)

        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)

        self.cuadricula.addWidget(self.barraHerramientas, 0, 0, 5, 4)



        self.cuadricula.addWidget(QLabel("Fortalece y tonifica tus cuádriceps con sentadillas efectivas:"
                                         "\n el ejercicio clave para unas piernas fuertes y esculpidas."
                                         "\n Las sentadillas son una excelente manera de trabajar"
                                         "\n los músculos de tus piernas, especialmente los cuádriceps."), 1, 2, 1, 6)





        self.cuadricula.addWidget(QLabel("Selecciona el nivel de dificultad"
                                         "\n sugerido"
                                         "\n(Puedes escoger cualquier nivel)"), 2, 2, 1, 6)



        self.imagenSentadilla = QLabel()
        self.imagenSentadilla.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/sentadilla.png")
        self.imagenSentadilla.setFixedSize(400, 250)
        self.imagenSentadilla.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagenSentadilla, 2, 7, 3, 1)



        self.botonVolver = QPushButton("VOLVER")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.volver)



        self.cuadricula.addWidget(self.botonVolver, 4, 2)





    def accion_barraHerramientas(self, opcion):
        self.hide()

        if opcion.text() == "Exp 1":
            pass

        #  self.ventana2 = Ventana2(self)
        # self.ventana2.show()

        if opcion.text() == "Exp 2":
            pass

        #   self.ventana = Ventana3(self)
        #  self.ventana3.show()

        if opcion.text() == "Exp 3":
            pass

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()
class Ventana7_10(QMainWindow):

    def __init__(self, anterior):
        super(Ventana7_10, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.setWindowTitle("Cuadriceps")

        self.setStyleSheet('background-color: black;')

        self.ancho = 1000
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)


        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)



        self.interna = QWidget()
        self.interna.setContentsMargins(0, 0, 0, 20)

        self.setCentralWidget(self.interna)

        self.cuadricula = QGridLayout()

        self.interna.setLayout(self.cuadricula)


        self.interna.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; border-radius:2px;"
                                   "border: 3px solid 	#000000;")

        self.label = QLabel("CUADRICEPS")
        self.label.setAlignment(Qt.AlignHCenter)  # Centra horizontalmente el contenido interno
        self.label.setStyleSheet('font-size: 60px;color: white; border: 5px double lightcoral; text-stroke: 2px gold;')
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.cuadricula.addWidget(self.widget, 0, 2, 1, 6)

        # Crea la barra de herramientas
        self.barraHerramientas = QToolBar("Barra de herramientas")
        # Agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)

        self.barraHerramientas.setOrientation(Qt.Vertical)

        self.barraHerramientas.setStyleSheet("color: white; font-size: 25px;border-radius:2px; "
                                             "border: 1px solid lightcoral;")
        # Tamaño de los iconos
        self.barraHerramientas.setIconSize(QSize(80, 100))

        # Creamos la opcion para la expresión 1
        self.exp1 = QAction(QIcon("imagenes/principiante.png"), "PRINCIPIANTE", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp2 = QAction(QIcon("imagenes/intermedio.png"), "INTERMEDIO", self)
        self.barraHerramientas.addAction(self.exp2)

        self.exp3 = QAction(QIcon("imagenes/avanzado2.png"), "AVANZADO", self)
        self.barraHerramientas.addAction(self.exp3)

        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)

        self.cuadricula.addWidget(self.barraHerramientas, 0, 0, 5, 4)



        self.cuadricula.addWidget(QLabel("Fortalece y tonifica tus cuádriceps con sentadillas efectivas:"
                                         "\n el ejercicio clave para unas piernas fuertes y esculpidas."
                                         "\n Las sentadillas son una excelente manera de trabajar"
                                         "\n los músculos de tus piernas, especialmente los cuádriceps."), 1, 2, 1, 6)





        self.cuadricula.addWidget(QLabel("Selecciona el nivel de dificultad"
                                         "\n sugerido"
                                         "\n(Puedes escoger cualquier nivel)"), 2, 2, 1, 6)



        self.imagenSentadilla = QLabel()
        self.imagenSentadilla.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/sentadilla.png")
        self.imagenSentadilla.setFixedSize(400, 250)
        self.imagenSentadilla.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagenSentadilla, 2, 7, 3, 1)



        self.botonVolver = QPushButton("VOLVER")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.volver)



        self.cuadricula.addWidget(self.botonVolver, 4, 2)





    def accion_barraHerramientas(self, opcion):
        self.hide()

        if opcion.text() == "Exp 1":
            pass

        #  self.ventana2 = Ventana2(self)
        # self.ventana2.show()

        if opcion.text() == "Exp 2":
            pass

        #   self.ventana = Ventana3(self)
        #  self.ventana3.show()

        if opcion.text() == "Exp 3":
            pass

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()
class Ventana7_11(QMainWindow):

    def __init__(self, anterior):
        super(Ventana7_11, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.setWindowTitle("Cuadriceps")

        self.setStyleSheet('background-color: black;')

        self.ancho = 1000
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)


        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)



        self.interna = QWidget()
        self.interna.setContentsMargins(0, 0, 0, 20)

        self.setCentralWidget(self.interna)

        self.cuadricula = QGridLayout()

        self.interna.setLayout(self.cuadricula)


        self.interna.setStyleSheet("color: white; font-size: 25px; font-family: Poppins; border-radius:2px;"
                                   "border: 3px solid 	#000000;")

        self.label = QLabel("CUADRICEPS")
        self.label.setAlignment(Qt.AlignHCenter)  # Centra horizontalmente el contenido interno
        self.label.setStyleSheet('font-size: 60px;color: white; border: 5px double lightcoral; text-stroke: 2px gold;')
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.cuadricula.addWidget(self.widget, 0, 2, 1, 6)

        # Crea la barra de herramientas
        self.barraHerramientas = QToolBar("Barra de herramientas")
        # Agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)

        self.barraHerramientas.setOrientation(Qt.Vertical)

        self.barraHerramientas.setStyleSheet("color: white; font-size: 25px;border-radius:2px; "
                                             "border: 1px solid lightcoral;")
        # Tamaño de los iconos
        self.barraHerramientas.setIconSize(QSize(80, 100))

        # Creamos la opcion para la expresión 1
        self.exp1 = QAction(QIcon("imagenes/principiante.png"), "PRINCIPIANTE", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp2 = QAction(QIcon("imagenes/intermedio.png"), "INTERMEDIO", self)
        self.barraHerramientas.addAction(self.exp2)

        self.exp3 = QAction(QIcon("imagenes/avanzado2.png"), "AVANZADO", self)
        self.barraHerramientas.addAction(self.exp3)

        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)

        self.cuadricula.addWidget(self.barraHerramientas, 0, 0, 5, 4)



        self.cuadricula.addWidget(QLabel("Fortalece y tonifica tus cuádriceps con sentadillas efectivas:"
                                         "\n el ejercicio clave para unas piernas fuertes y esculpidas."
                                         "\n Las sentadillas son una excelente manera de trabajar"
                                         "\n los músculos de tus piernas, especialmente los cuádriceps."), 1, 2, 1, 6)





        self.cuadricula.addWidget(QLabel("Selecciona el nivel de dificultad"
                                         "\n sugerido"
                                         "\n(Puedes escoger cualquier nivel)"), 2, 2, 1, 6)



        self.imagenSentadilla = QLabel()
        self.imagenSentadilla.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("imagenes/sentadilla.png")
        self.imagenSentadilla.setFixedSize(400, 250)
        self.imagenSentadilla.setPixmap(self.pixmap)
        self.cuadricula.addWidget(self.imagenSentadilla, 2, 7, 3, 1)



        self.botonVolver = QPushButton("VOLVER")
        self.botonVolver.setFixedWidth(250)
        self.botonVolver.setStyleSheet(
            "color: white; font-size: 18px; font-family: Poppins; padding: 10px; border-radius:10px; "
            "border: 1px solid #FFFFFF; width:10px; height:20px;")
        self.botonVolver.clicked.connect(self.volver)



        self.cuadricula.addWidget(self.botonVolver, 4, 2)





    def accion_barraHerramientas(self, opcion):
        self.hide()

        if opcion.text() == "Exp 1":
            pass

        #  self.ventana2 = Ventana2(self)
        # self.ventana2.show()

        if opcion.text() == "Exp 2":
            pass

        #   self.ventana = Ventana3(self)
        #  self.ventana3.show()

        if opcion.text() == "Exp 3":
            pass

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()
