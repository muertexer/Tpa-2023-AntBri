import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, \
    QWidget, QLineEdit, QGridLayout, QLabel, QPlainTextEdit, QSpinBox, QSlider

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.addtxt = ""
        self.setWindowTitle("Ejercicios de GUIs")
        self.setFixedSize(QSize(750,450))
        caja = QGridLayout()

        # PRIMERA COLUMNA
        self.NyA = QLabel("Nombre y Apellido")
        caja.addWidget(self.NyA, 0, 0)
        self.Desc = QLabel("Descripción") #Va con Qplantextedit
        caja.addWidget(self.Desc, 1, 0)
        self.Edad = QLabel("Edad")
        caja.addWidget(self.Edad, 2, 0)
        self.Altura = QLabel("Altura")
        caja.addWidget(self.Altura, 3, 0)
        self.CIoP = QLabel("Cédula de Identidad o Pasaporte")
        caja.addWidget(self.CIoP, 4, 0)
        self.IDE = QLabel("Identificador del Documento")
        caja.addWidget(self.IDE, 5, 0)
        self.Gnre = QLabel("Género")
        caja.addWidget(self.Gnre, 6, 0)
        self.EsCiv = QLabel("Estado Civil")
        caja.addWidget(self.EsCiv, 7, 0)
        self.Edu = QLabel("Educación")
        caja.addWidget(self.Edu, 8, 0)
        self.Stats = QLabel("Habilidades")
        caja.addWidget(self.Stats, 9, 0)
        self.Eng = QLabel("Nivel de Idioma Inglés")
        caja.addWidget(self.Eng, 10, 0)
        self.Born = QLabel("Fecha de Nacimiento")
        caja.addWidget(self.Born, 11, 0)
        self.User = QLabel("Nombre Usuario (Sin espacios)")
        caja.addWidget(self.User, 12, 0)
        self.Pass = QLabel("Contraseña Usuario ")
        caja.addWidget(self.Pass, 13, 0)


        #SEGUNDA COLUMNA
        self.Display = QLabel('Label: "Mensaje del Botón"')
        self.txtNyA = QLineEdit()
        self.txtDesc = QPlainTextEdit()
        self.txtEdad = QSpinBox()
        self.txtAltura = QSlider() #Mostrar valor con Qlabel
        self.txtCIoP = QSpinBox() #Mostrar valor con Qlabel #TODO SEGUIR REVISANDO TEST PARA SIMPLIFICAR EL CIoP
        self.txtIDE = QSpinBox()
        self.txtGnre = QSpinBox()
        self.txtEsCiv = QSpinBox()
        self.txtEdu = QSpinBox()
        self.txtStats = QSpinBox()
        self.txtEng = QSpinBox()
        self.txtBorn = QSpinBox()
        self.txtUser = QSpinBox()
        self.txtPass = QSpinBox()











        self.btn1 = QPushButton("Aceptar")


        self.txtEdit = QLineEdit("______")

        #addWidget de
        caja.addWidget(self.Display, 1 , 2)
        caja.addWidget(self.btn1, 0, 3)
        caja.addWidget(self.NyA, 0, 1)





        ventana = QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    app.exec()