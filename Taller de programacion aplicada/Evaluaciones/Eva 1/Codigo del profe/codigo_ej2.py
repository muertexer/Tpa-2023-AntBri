import sys
from PyQt6 import QtWidgets, uic

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget, QListWidget)


from VentanaPrincipal import Ui_VentanaPrincipal as vp
from ventanasecundaria import Ui_VentanaSecundaria as vs


class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso:float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} anios de la especie {self.especie} con {self.peso} Kg."


class Ventana(QtWidgets.QMainWindow, vp, vs):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
        self.clicks = 0

        self.pushButton.clicked.connect(self.guardar_mascota)

##Intento de cambio de ventana para que sea trasladado a la ventana primaria y secundaria
    def cambiarVP(self):
        #self.caja_inferior.setCurrentIndex(0)
        pass
    def cambiarVS(self):
        #self.caja_inferior.setCurrentIndex(1)
        pass
    def guardar_mascota(self):
        self.clicks += 1
        nombre = self.entrada_nombre.text()
        edad = self.entrada_edad.text()
        especie = self.entrada_especie.text()
        peso = self.entrada_peso.text()
        mascota = f"La Mascota N°{self.clicks}:  {nombre} de {edad} años de la especie {especie} con {peso} Kg."
        self.entrada_peso.setValue(0)
        self.entrada_edad.setValue(0)
        self.entrada_especie.setText("")
        self.entrada_nombre.setText("")
        self.lista.addItem(mascota)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana()
    vista.show()
    app.exec()