import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, \
    QWidget, QVBoxLayout, QLabel, QLineEdit

# VENTANA:
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Suma de números")
        self.setFixedSize(QSize(400,200))
        caja = QVBoxLayout()

        self.title = QLabel("Ingrese dos números para poder sumarlos")
        self.texto = QLabel("")
        self.entrada = QLineEdit("")
        self.entrada2 = QLineEdit("")
        self.boton = QPushButton("Botón")
        self.boton.clicked.connect(self.reaccionar)

        caja.addWidget(self.title)
        caja.addWidget(self.entrada)
        caja.addWidget(self.entrada2)
        caja.addWidget(self.texto)
        caja.addWidget(self.boton)

        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
    def reaccionar(self):
        n = int(self.entrada.text())
        m = int(self.entrada2.text())
        self.texto.setText(f"La suma es {n+m}")
        self.entrada.setText("")
        self.entrada2.setText("")
        self.boton.setText("Botón")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    app.exec()