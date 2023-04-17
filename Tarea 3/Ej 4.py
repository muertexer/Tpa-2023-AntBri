import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, \
    QWidget, QVBoxLayout, QLabel, QLineEdit

# VENTANA:
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Número Primo")
        self.setFixedSize(QSize(400,200))
        caja = QVBoxLayout()

        self.title = QLabel("Ingrese un número para determinar si es primo")
        self.texto = QLabel("")
        self.entrada = QLineEdit("")
        self.boton = QPushButton("Botón")
        self.boton.clicked.connect(self.reaccionar)

        caja.addWidget(self.title)
        caja.addWidget(self.entrada)
        caja.addWidget(self.texto)
        caja.addWidget(self.boton)

        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
    def reaccionar(self):
        n = int(self.entrada.text())

# Funcion para saber si es primo
        def es_primo(n):
            if n <= 1:
                return f"El número {n} no es primo"
            for i in range(2, int(n / 2) + 1):
                if n % i == 0:
                    return f"El número {n} no es primo"
            return f"El número {n} es primo"

        self.texto.setText(es_primo(n))
        self.entrada.setText("")
        self.boton.setText("Botón")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    app.exec()