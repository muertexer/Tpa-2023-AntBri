
import sys

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setMouseTracking(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 721, 361))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.texto = QLabel(self.verticalLayoutWidget)
        self.texto.setObjectName(u"texto")
        font = QFont()
        font.setFamilies([u"Script"])
        font.setPointSize(50)
        self.texto.setFont(font)

        self.verticalLayout.addWidget(self.texto)

        self.entrada = QLineEdit(self.verticalLayoutWidget)
        self.entrada.setObjectName(u"entrada")

        self.verticalLayout.addWidget(self.entrada)

        self.boton = QPushButton(self.verticalLayoutWidget)
        self.boton.setObjectName(u"boton")

        self.verticalLayout.addWidget(self.boton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 860, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

#vola editada
    def saludar(self):
        self.texto.setText(f"Bienvenido {self.entrada.text()}")
        self.entrada.setText("")
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.texto.setText(QCoreApplication.translate("MainWindow", u"Texto de bienvenida", None))
        self.boton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vista = Ui_MainWindow()
    vista.show()
    app.exec()