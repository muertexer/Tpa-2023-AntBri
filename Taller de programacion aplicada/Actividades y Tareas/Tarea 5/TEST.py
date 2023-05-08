from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ID Document Type")
        self.setGeometry(100, 100, 300, 200)

        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setGeometry(20, 20, 30, 20)
        self.slider.setMinimum(0)
        self.slider.setMaximum(1)
        self.slider.setSingleStep(1)
        self.slider.setTickPosition(QSlider.TickPosition.NoTicks)
        self.slider.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #bbb;
                background: white;
                height: 10px;
                border-radius: 4px;
            }

            QSlider::handle:horizontal {
                background: #bbb;
                border: 1px solid #777;
                width: 20px;
                margin: -5px 0;
                border-radius: 4px;
            }

            QSlider::handle:horizontal:checked {
                background: #0f0;
            }
        """)
        self.slider.sliderReleased.connect(self.toggle_slider)

        self.label = QLabel("Please select ID document type", self)
        self.label.setGeometry(20, 80, 200, 20)

    def toggle_slider(self):
        if self.slider.value() == 0:
            self.slider.setValue(1)
            self.label.setText("Pasaporte selected")
        elif self.slider.value() == 1:
            self.slider.setValue(0)
            self.label.setText("Cédula de Identidad selected")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()