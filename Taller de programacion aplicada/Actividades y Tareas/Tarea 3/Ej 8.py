import sys
from PyQt6.QtCore import QSize, Qt, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, \
    QWidget, QVBoxLayout, QLabel, QLineEdit
# VENTANA:
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formato E-Mail")
        self.setFixedSize(QSize(0,150))
        caja = QVBoxLayout()

        self.title = QLabel("Ingrese un correo electrónico para verificar si tiene el formato adecuado")
        self.texto = QLabel("")
        self.entrada = QLineEdit("")
        self.boton = QPushButton("Validar correo electrónico")
        self.boton.clicked.connect(self.reaccionar)

        caja.addWidget(self.title)
        caja.addWidget(self.entrada)
        caja.addWidget(self.texto)
        caja.addWidget(self.boton)

        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
    def reaccionar(self):
        regulador = QRegularExpression('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
        validar = QRegularExpressionValidator(regulador, self.entrada)
        self.entrada.setValidator(validar)
        email = self.entrada.text()
        if email:
            if self.entrada.hasAcceptableInput():
                self.texto.setText(f'"{self.entrada.text()}" es un formato de correo electrónico valido')
            else:
                self.texto.setText(f'"{self.entrada.text()}" es un formato de correo electrónico invalido')
        else:
            self.texto.setText('Ingrese un correo electrónico')

        self.entrada.setText("")
        self.boton.setText("Validar correo electrónico")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    app.exec()