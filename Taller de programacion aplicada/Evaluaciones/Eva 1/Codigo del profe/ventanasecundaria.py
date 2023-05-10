

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget, QListWidget, )
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VentanaSecundaria(object):
    def setupUi(self, VentanaSecundaria):
        if not VentanaSecundaria.objectName():
            VentanaSecundaria.setObjectName(u"VentanaSecundaria")
        VentanaSecundaria.resize(700, 400)
        self.verticalLayoutWidget = QWidget(VentanaSecundaria)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 661, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.btncambioVP = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btncambioVP.setObjectName("btncambioVP")
        self.verticalLayout.addWidget(self.btncambioVP)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(24)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lista = QListWidget(self.verticalLayoutWidget)
        self.lista.setObjectName(u"aaaaa")

        self.verticalLayout.addWidget(self.lista)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(VentanaSecundaria)

        QMetaObject.connectSlotsByName(VentanaSecundaria)
    # setupUi

    def retranslateUi(self, VentanaSecundaria):
        VentanaSecundaria.setWindowTitle(QCoreApplication.translate("VentanaSecundaria", u"VentanaSecundaria", None))
        self.label.setText(QCoreApplication.translate("VentanaSecundaria", u"Informaci\u00f3n Mascota", None))
        self.label_2.setText(QCoreApplication.translate("VentanaSecundaria", u"Datos de la mascota:", None))
        self.pushButton.setText(QCoreApplication.translate("VentanaSecundaria", u"OK", None))
        self.btncambioVP.setText(QCoreApplication.translate("VentanaSecundaria", u"Ventana Principal", None))


    # retranslateUi

