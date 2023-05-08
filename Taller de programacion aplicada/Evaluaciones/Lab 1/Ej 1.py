# INTEGRANTES
# Antoine Briones - Sebastian Adriazola - Cristhoper Gonzalez - Benjamin Burgos

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, \
    QWidget, QVBoxLayout, QLabel, QDialog, QDialogButtonBox, QLineEdit


class VentanaIngresoIZQ(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingreso de Datos Libras")
        self.titleDialog = QLabel("Ingreso de Datos Libras")
        self.titleLibras = QLabel("Libras: ")
        self.inputLibras = QLineEdit()

        QBtn = QDialogButtonBox.StandardButton.Save
        self.guardar = QDialogButtonBox(QBtn)
        self.guardar.clicked.connect(self.accept)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.titleDialog)
        self.layout.addWidget(self.titleLibras)
        self.layout.addWidget(self.inputLibras)
        self.layout.addWidget(self.guardar)
        self.setLayout(self.layout)


class VentanaIngresoDER(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingreso de Datos Onzas")
        self.titleDialog = QLabel("Ingreso de Datos Onzas")
        self.titleOnzas = QLabel("Onzas: ")
        self.inputOnzas = QLineEdit()

        QBtn = QDialogButtonBox.StandardButton.Save
        self.guardar = QDialogButtonBox(QBtn)
        self.guardar.clicked.connect(self.accept)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.titleDialog)
        self.layout.addWidget(self.titleOnzas)
        self.layout.addWidget(self.inputOnzas)
        self.layout.addWidget(self.guardar)
        self.setLayout(self.layout)





# VENTANA:
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Comparativa de Datos LAB 1 [TPA2023-1]")
        self.setFixedSize(QSize())
        cajaGrande = QVBoxLayout()
        cajaChica = QHBoxLayout()
        cajaChiquitaIZQ = QVBoxLayout()
        cajaChiquitaDER = QVBoxLayout()
        self.ValorIZQ = None
        self.ValorDER= None


        #Caja
        self.title = QLabel("Comparativa de Datos")
        self.subTitle = QLabel('- Ingrese la masa 1  (en libras) con el botón "Agregar Datos" del lado izquierdo \
                                \n- Ingrese la masa 2 (en Onzas) con el botón "Agregar Datos" del lado derecho \
                                    \nEl botón "Comparar" utiliza los datos ingresados anteriormente, '
                               'bajo una fórmula para convertirlos a Kgs, '
                               'para indicar si una masa es mayor, menor o igual a la masa')
        self.botonComp = QPushButton("Comparar")
        self.botonComp.clicked.connect(self.comparacion)


        #Caja Chica

        ###Caja Chiquita1 IZQ
        self.atributo1IZQ = QLabel("Libras")
        self.atributo2IZQ = QLabel("Libras Ingresadas: ")
        self.atributo3IZQ = QLabel("BLANK")
        self.resultIZQ = QLabel("Dato Calculado (Dato en KG)")
        self.botonAddIZQ = QPushButton("Agregar Datos")
        self.botonAddIZQ.clicked.connect(self.agregarDatosIZQ)


        ###Simbolo comparativo
        self.simboloComparacion = QLabel("")


        ###Caja Chiquita2 DER
        self.atributo1DER = QLabel("Onzas")
        self.atributo2DER = QLabel("Onzas Ingresadas:")
        self.atributo3DER = QLabel("BLANK")
        self.resultDER = QLabel("Dato Calculado (Dato en KG)")
        self.botonAddDER = QPushButton("Agregar Datos")
        self.botonAddDER.clicked.connect(self.agregarDatosDER)

        #ARMADO DE GUI

        cajaGrande.addWidget(self.title)
        cajaGrande.addWidget(self.subTitle)
        #cajaChica
        ###Caja Chiquita1 IZQ

        cajaChiquitaIZQ.addWidget(self.atributo1IZQ)
        cajaChiquitaIZQ.addWidget(self.atributo2IZQ)
        cajaChiquitaIZQ.addWidget(self.atributo3IZQ)
        cajaChiquitaIZQ.addWidget(self.resultIZQ)
        cajaChiquitaIZQ.addWidget(self.botonAddIZQ)

        cajaChica.addLayout(cajaChiquitaIZQ)

        ##SIMBOLO
        cajaChica.addWidget(self.simboloComparacion)
        ###Caja Chiquita2 DER

        cajaChiquitaDER.addWidget(self.atributo1DER)
        cajaChiquitaDER.addWidget(self.atributo2DER)
        cajaChiquitaDER.addWidget(self.atributo3DER)
        cajaChiquitaDER.addWidget(self.resultDER)
        cajaChiquitaDER.addWidget(self.botonAddDER)

        cajaChica.addLayout(cajaChiquitaDER)
        cajaGrande.addLayout(cajaChica)


        cajaGrande.addWidget(self.botonComp)



        Ventana = QWidget()
        Ventana.setLayout(cajaGrande)
        self.setCentralWidget(Ventana)
        Ventana2 = QWidget()
        Ventana2.setLayout(cajaChica)
        Ventana3 = QWidget()
        Ventana3.setLayout(cajaChiquitaIZQ)
        Ventana4 = QWidget()
        Ventana4.setLayout(cajaChiquitaDER)



    def agregarDatosIZQ(self):
        dialogIZQ = VentanaIngresoIZQ()
        dialogIZQ.exec()
        self.atributo3IZQ.setText(dialogIZQ.inputLibras.text())
        valorEquivalente = float(dialogIZQ.inputLibras.text()) / 2.205
        self.resultIZQ.setText(f"Es equivalente a {round(valorEquivalente,2)} Kg")
        self.ValorIZQ = valorEquivalente


    def agregarDatosDER(self):
        dialogDER = VentanaIngresoDER()
        dialogDER.exec()
        self.atributo3DER.setText(dialogDER.inputOnzas.text())
        valorEquivalente = float(dialogDER.inputOnzas.text()) / 35.274
        self.resultDER.setText(f"Es equivalente a {round(valorEquivalente,2)} Kg")
        self.ValorDER = valorEquivalente




    def comparacion(self):
        if self.ValorIZQ > self.ValorDER:
            self.simboloComparacion.setText(">")
        elif self.ValorIZQ < self.ValorDER:
            self.simboloComparacion.setText("<")
        else:
            self.simboloComparacion.setText("=")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    app.exec()