import sys
import random
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, \
    QWidget, QVBoxLayout, QLabel, QLineEdit

# VENTANA:
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Número aleatorio")
        self.setFixedSize(QSize(400,200))
        caja = QVBoxLayout()

        self.title = QLabel("Presione para mostrar un numero aleatorio")
        self.texto = QLabel("")
        self.entrada = QLineEdit("")
        self.boton = QPushButton("Botón")
        self.boton.clicked.connect(self.reaccionar)

        caja.addWidget(self.title)
        caja.addWidget(self.boton)
        caja.addWidget(self.texto)

        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
    def reaccionar(self):
        n = int(random.randint(1, 1000000))
        self.texto.setText(f"Número aleatorio: {n}")
        self.entrada.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    app.exec()