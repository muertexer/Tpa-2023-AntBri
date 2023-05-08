import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, \
    QWidget, QLineEdit, QGridLayout
# VENTANA:
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.txt = ""
        self.clicks = 0
        self.setWindowTitle("Calculadora")
        self.setFixedSize(QSize())
        caja = QGridLayout()
        caja_grande = QHBoxLayout()


        self.Display = QLineEdit("")
        self.BorrarTodo = QPushButton("Borrar Todo")
        self.Borrar = QPushButton("Borrar")
        self.botonPar = QPushButton("(")
        self.botonCPar = QPushButton(")")
        self.botonDIV = QPushButton("/")
        self.botonMULT = QPushButton("*")
        self.botonREST = QPushButton("-")
        self.botonSUM = QPushButton("+")
        self.botonIGUAL = QPushButton("=")
        self.boton0 = QPushButton("0")
        self.boton1 = QPushButton("1")
        self.boton2 = QPushButton("2")
        self.boton3 = QPushButton("3")
        self.boton4 = QPushButton("4")
        self.boton5 = QPushButton("5")
        self.boton6 = QPushButton("6")
        self.boton7 = QPushButton("7")
        self.boton8 = QPushButton("8")
        self.boton9 = QPushButton("9")


        self.Borrar.clicked.connect(self.fBorrar)
        self.BorrarTodo.clicked.connect(self.fBorrarTodo)
        self.botonPar.clicked.connect(self.fbotonPar)
        self.botonCPar.clicked.connect(self.fbotonCPar)
        self.botonDIV.clicked.connect(self.fbotonDIV)
        self.botonMULT.clicked.connect(self.fbotonMULT)
        self.botonREST.clicked.connect(self.fbotonREST)
        self.botonSUM.clicked.connect(self.fbotonSUM)
        self.botonIGUAL.clicked.connect(self.fbotonIGUAL)
        self.boton0.clicked.connect(self.fboton0)
        self.boton1.clicked.connect(self.fboton1)
        self.boton2.clicked.connect(self.fboton2)
        self.boton3.clicked.connect(self.fboton3)
        self.boton4.clicked.connect(self.fboton4)
        self.boton5.clicked.connect(self.fboton5)
        self.boton6.clicked.connect(self.fboton6)
        self.boton7.clicked.connect(self.fboton7)
        self.boton8.clicked.connect(self.fboton8)
        self.boton9.clicked.connect(self.fboton9)


        caja.addWidget(self.Display,    0,  2,  1,   2)
        caja.addWidget(self.Borrar,     0,  0)
        caja.addWidget(self.BorrarTodo, 0, 1)
        caja.addWidget(self.botonPar,   1,  1)
        caja.addWidget(self.botonCPar,  1,  2)
        caja.addWidget(self.botonDIV,   1,  3)
        caja.addWidget(self.botonMULT,  2,  3)
        caja.addWidget(self.botonREST,  3,  3)
        caja.addWidget(self.botonSUM,   4,  3)
        caja.addWidget(self.botonIGUAL, 5,  3)
        caja.addWidget(self.boton1, 4,   0)
        caja.addWidget(self.boton2, 4,   1)
        caja.addWidget(self.boton3, 4,   2)
        caja.addWidget(self.boton4, 3,   0)
        caja.addWidget(self.boton5, 3,   1)
        caja.addWidget(self.boton6, 3,   2)
        caja.addWidget(self.boton7, 2,   0)
        caja.addWidget(self.boton8, 2,   1)
        caja.addWidget(self.boton9, 2,   2)
        caja.addWidget(self.boton0, 5,   1)



        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
        ventana2 = QWidget()
        ventana2.setLayout(caja_grande)
        #self.setCentralWidget(ventana2)

    # TODO arreglar el igual y borrar

    def fbotonIGUAL(self):
        try:
            resultado = eval(self.txt)
            self.Display.setText(str(resultado))
        except:
            self.Display.setText("Error")

    def fBorrarTodo(self):
        a = len(self.txt)
        self.txt = self.txt[:-a]
        self.Display.setText(self.txt)
    def fBorrar(self):
        self.txt = self.txt[:-1]
        self.Display.setText(self.txt)
    def fbotonPar(self):
        self.txt += "("
        self.Display.setText(self.txt)
    def fbotonCPar(self):
        self.txt += ")"
        self.Display.setText(self.txt)
    def fbotonDIV(self):
        self.txt += "/"
        self.Display.setText(self.txt)
    def fbotonMULT(self):
        self.txt += "*"
        self.Display.setText(self.txt)
    def fbotonREST(self):
        self.txt += "-"
        self.Display.setText(self.txt)
    def fbotonSUM(self):
        self.txt += "+"
        self.Display.setText(self.txt)
    def fboton0(self):
        self.txt += "0"
        self.Display.setText(self.txt)
    def fboton1(self):
        self.txt += "1"
        self.Display.setText(self.txt)
    def fboton2(self):
        self.txt += "2"
        self.Display.setText(self.txt)
    def fboton3(self):
        self.txt += "3"
        self.Display.setText(self.txt)
    def fboton4(self):
        self.txt += "4"
        self.Display.setText(self.txt)
    def fboton5(self):
        self.txt += "5"
        self.Display.setText(self.txt)
    def fboton6(self):
        self.txt += "6"
        self.Display.setText(self.txt)
    def fboton7(self):
        self.txt += "7"
        self.Display.setText(self.txt)
    def fboton8(self):
        self.txt += "8"
        self.Display.setText(self.txt)
    def fboton9(self):
        self.txt += "9"
        self.Display.setText(self.txt)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    app.exec()