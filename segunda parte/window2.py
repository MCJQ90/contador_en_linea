#Clase semana 14, práctica

from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.statusBar().showMessage("HOLA MUNDO")
window.menuBar().addMenu("Archivo")
window.menuBar().addMenu("Inicio")

window.show()

sys.exit(app.exec())