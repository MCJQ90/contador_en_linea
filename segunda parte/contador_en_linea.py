from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 761, 531))
        self.widget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(10, 70, 171, 20))
        self.label.setObjectName("label")
        self.inputNumeroIdentificacion = QtWidgets.QLineEdit(
            parent=self.widget)
        self.inputNumeroIdentificacion.setGeometry(
            QtCore.QRect(190, 100, 113, 21))
        self.inputNumeroIdentificacion.setObjectName(
            "inputNumeroIdentificacion")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 171, 20))
        self.label_2.setObjectName("label_2")
        self.inputNombre = QtWidgets.QLineEdit(parent=self.widget)
        self.inputNombre.setGeometry(QtCore.QRect(190, 130, 331, 21))
        self.inputNombre.setObjectName("inputNombre")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_4.setObjectName("label_4")
        self.inputApellido = QtWidgets.QLineEdit(parent=self.widget)
        self.inputApellido.setGeometry(QtCore.QRect(190, 160, 331, 21))
        self.inputApellido.setObjectName("inputApellido")
        self.inputDireccion = QtWidgets.QLineEdit(parent=self.widget)
        self.inputDireccion.setGeometry(QtCore.QRect(190, 190, 331, 21))
        self.inputDireccion.setObjectName("inputDireccion")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 91, 16))
        self.label_5.setObjectName("label_5")
        self.inputEmail = QtWidgets.QLineEdit(parent=self.widget)
        self.inputEmail.setGeometry(QtCore.QRect(190, 220, 331, 21))
        self.inputEmail.setObjectName("inputEmail")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 220, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setGeometry(QtCore.QRect(10, 250, 91, 16))
        self.label_7.setObjectName("label_7")
        self.intTelefono = QtWidgets.QLineEdit(parent=self.widget)
        self.intTelefono.setGeometry(QtCore.QRect(190, 250, 113, 21))
        self.intTelefono.setObjectName("intTelefono")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(190, 300, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 300, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setGeometry(QtCore.QRect(310, 10, 141, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.widget)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 151, 16))
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(parent=self.widget)
        self.comboBox.setGeometry(QtCore.QRect(190, 70, 150, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(3, "")
        self.textOutPut = QtWidgets.QTextEdit(parent=self.widget)
        self.textOutPut.setGeometry(QtCore.QRect(50, 340, 651, 181))
        self.textOutPut.setObjectName("textOutPut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", " TIPO DE IDENTIFICACIÓN:"))
        self.label_2.setText(_translate(
            "MainWindow", " NUMERO DE IDENTIFICACIÓN:"))
        self.label_3.setText(_translate("MainWindow", " NOMBRES:"))
        self.label_4.setText(_translate("MainWindow", " APELLIDOS:"))
        self.label_5.setText(_translate("MainWindow", " DIRECCIÓN:"))
        self.label_6.setText(_translate("MainWindow", " EMAIL:"))
        self.label_7.setText(_translate("MainWindow", " TELÉFONO:"))
        self.pushButton.setText(_translate("MainWindow", "REGISTRAR"))
        self.pushButton_2.setText(_translate("MainWindow", "CANCELAR"))
        self.label_8.setText(_translate("MainWindow", "CONTADOR EN LINEA JL"))
        self.label_9.setText(_translate("MainWindow", "REGISTRO DE CLIENTES"))
        self.comboBox.setItemText(0, _translate("MainWindow", "04: RUC"))
        self.comboBox.setItemText(1, _translate("MainWindow", "05: CEDULA"))
        self.comboBox.setItemText(2, _translate("MainWindow", "06: PASAPORTE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    def registrar_cliente():
        tipo_id = ui.comboBox.currentText()
        numero_id = ui.inputNumeroIdentificacion.text()
        nombres = ui.inputNombre.text()
        apellidos = ui.inputApellido.text()
        direccion = ui.inputDireccion.text()
        email = ui.inputEmail.text()
        telefono = ui.intTelefono.text()

        resumen = (
            f"📋 Datos del Cliente Registrado:\n"
            f"Tipo ID: {tipo_id}\n"
            f"Número ID: {numero_id}\n"
            f"Nombres: {nombres}\n"
            f"Apellidos: {apellidos}\n"
            f"Dirección: {direccion}\n"
            f"Email: {email}\n"
            f"Teléfono: {telefono}\n"
    )

        ui.textOutPut.setPlainText(resumen)


    def cancelar_formulario():
        ui.comboBox.setCurrentIndex(0)
        ui.inputNumeroIdentificacion.clear()
        ui.inputNombre.clear()
        ui.inputApellido.clear()
        ui.inputDireccion.clear()
        ui.inputEmail.clear()
        ui.intTelefono.clear()
        ui.textOutPut.clear()

    # Conectar botones
    ui.pushButton.clicked.connect(registrar_cliente)
    ui.pushButton_2.clicked.connect(cancelar_formulario)

    MainWindow.show()
    sys.exit(app.exec())
