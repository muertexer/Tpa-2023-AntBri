import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, \
    QWidget, QVBoxLayout, QLabel, QLineEdit, QListWidget

# VENTANA:
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Listado de frutas")
        self.setFixedSize(QSize(300, 350))
        caja = QVBoxLayout()

        self.title = QLabel("Ingrese una fruta")
        self.lista = QListWidget()
        self.entrada = QLineEdit("")
        self.boton = QPushButton("Agregar")
        self.boton.clicked.connect(self.reaccionar)

        caja.addWidget(self.title)
        caja.addWidget(self.entrada)
        caja.addWidget(self.boton)
        caja.addWidget(self.lista)


        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
    def reaccionar(self):
        n = self.entrada.text()
        self.lista.addItem(n)
        self.entrada.setText("")
        self.boton.setText("Agregar")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    app.exec()