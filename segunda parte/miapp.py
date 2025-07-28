from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contador en Línea JL")
        # self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("images/logo.png"))

        self.setStyleSheet("background-color: #f0f0f0; color: #333; font-family: Arial, sans-serif;")

app = QApplication(sys.argv)
ventana = MiVentana()
ventana.show()
sys.exit(app.exec())