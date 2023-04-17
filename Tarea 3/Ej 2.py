import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, \
    QWidget, QVBoxLayout, QLabel, QLineEdit

# VENTANA:
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Palabra al revés")
        self.setFixedSize(QSize(400,200))
        caja = QVBoxLayout()

        self.title = QLabel("Ingrese una palabra para entregarla al revés")
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
        n = self.entrada.text()
        self.texto.setText(f"La palabra al revés es: {n[::-1]}")
        self.entrada.setText("")
        self.boton.setText("Botón")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    app.exec()