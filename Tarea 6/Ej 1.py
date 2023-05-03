# - Crear Vista para ingresar los datos del problema que les corresponde
# - Crear Modelo de los datos del problema  que corresponde
# - Conectar la Vista con el Modelo creando una lista correspondiente al tema.
# Grupos de 4 a 5 integrantes.

# Integrantes: Antoine Briones, Sebastian Adriazola, Crsitopher González y Benjamin Burgos

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QMessageBox, QGridLayout, QPushButton, \
    QStackedLayout, QVBoxLayout, QHBoxLayout, QWidget, QListWidget

class Pokemon:

    def __init__(self, nombre, especie, tipo, habilidad):
        self.nombre = nombre
        self.tipo = tipo
        self.habilidad = habilidad
        self.especie = especie

    def __str__(self) -> str:
        return f"El Pokemon es: {self.nombre}, de especie {self.especie}, de tipo(s) {self.tipo}, su habilidad es {self.habilidad}"



class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.clicks = 0
        self.setWindowTitle("Listado Pokemons")
        self.setFixedSize(QSize(600, 200))
        caja_grande = QVBoxLayout()
        caja_superior = QHBoxLayout()
        self.caja_inferior = QStackedLayout()


        #Principal:
        btn1 = QPushButton("Registrar Pokemons")
        btn2 = QPushButton("Lista de Ingresados")
        caja_superior.addWidget(btn1)
        caja_superior.addWidget(btn2)

        btn1.clicked.connect(self.cambiolayout1)
        btn2.clicked.connect(self.cambiolayout2)

        contenedor = QWidget()
        layout = QVBoxLayout(contenedor)
        contenedor2 = QWidget()
        layout2 = QVBoxLayout(contenedor2)



        #layout
        txt = QLabel("Registre su pokemon")
        formReg = QGridLayout()
        registNombre = QLabel("Nombre:")
        self.intNombre = QLineEdit()
        registEspecie = QLabel("Especie:")
        self.intEspecie = QLineEdit()
        registTipo = QLabel("Tipo:")
        self.intTipo = QLineEdit()
        registHabilidad = QLabel("Habilidad:")
        self.intHabilidad = QLineEdit()
        registBTN = QPushButton("Registrar")
        registBTN.clicked.connect(self.RegisterPKN)


        formReg.addWidget(registNombre, 0, 0)
        formReg.addWidget(self.intNombre, 0, 1)
        formReg.addWidget(registEspecie, 0, 2)
        formReg.addWidget(self.intEspecie, 0, 3)
        formReg.addWidget(registTipo, 1, 0)
        formReg.addWidget(self.intTipo, 1, 1)
        formReg.addWidget(registHabilidad, 1, 2)
        formReg.addWidget(self.intHabilidad, 1, 3)
        formReg.addWidget(registBTN, 2, 0 , 1, 4)

        layout.addWidget(txt)
        layout.addLayout(formReg)


        #layout 2

        self.txt2 = QLabel("Lista de Pokemons Ingresados")
        layout2.addWidget(self.txt2)
        self.lista = QListWidget()
        layout2.addWidget(self.lista)



        #Organizacion de cajas

        self.caja_inferior.addWidget(contenedor)
        self.caja_inferior.addWidget(contenedor2)

        caja_grande.addLayout(caja_superior)
        caja_grande.addLayout(self.caja_inferior)

        ventana = QWidget()
        ventana.setLayout(caja_grande)
        self.setCentralWidget(ventana)



    def cambiolayout1(self):
        self.caja_inferior.setCurrentIndex(0)

    def cambiolayout2(self):
        self.caja_inferior.setCurrentIndex(1)


    def RegisterPKN(self):
        self.clicks += 1
        nombre = self.intNombre.text()
        especie = self.intEspecie.text()
        tipo = self.intTipo.text()
        habilidad = self.intHabilidad.text()
        Poke = f'El Pokemon N°{self.clicks}: De nombre: "{nombre}" - Especie: "{especie}" - Tipo(s): "{tipo}" - Habilidad: "{habilidad}"'
        self.intNombre.setText("")
        self.intTipo.setText("")
        self.intEspecie.setText("")
        self.intHabilidad.setText("")
        self.lista.addItem(Poke)



    pass
# Main
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()