import sys
from PyQt6.QtCore import QSize, Qt, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, \
    QWidget, QVBoxLayout, QLabel, QLineEdit, QListWidget
# VENTANA:
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.clicks = 0
        self.setWindowTitle("Lista de personas")
        self.setFixedSize(QSize(550,400))
        caja = QVBoxLayout()

        self.titleN = QLabel("Ingrese el nombre")
        self.entradaN = QLineEdit("")
        self.titleA = QLabel("Ingrese el apellido")
        self.entradaA = QLineEdit("")
        self.boton = QPushButton("Agregar")
        self.lista = QListWidget()
        self.boton.clicked.connect(self.reaccionar)

        caja.addWidget(self.titleN)
        caja.addWidget(self.entradaN)
        caja.addWidget(self.titleA)
        caja.addWidget(self.entradaA)
        caja.addWidget(self.lista)
        caja.addWidget(self.boton)

        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
    def reaccionar(self):

        self.clicks += 1
        N = self.entradaN.text()
        A = self.entradaA.text()
        individuo = f"N° {self.clicks}\tNombre: {N}\tApellido: {A}"
        self.lista.addItem(individuo)
        self.boton.setText("Agregar")
        self.entradaN.setText("")
        self.entradaA.setText("")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    app.exec()