from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(171, 247)
        self.title = QtWidgets.QLineEdit(Form)
        self.title.setGeometry(QtCore.QRect(10, 40, 151, 20))
        self.title.setObjectName("title")
        self.roasting = QtWidgets.QLineEdit(Form)
        self.roasting.setGeometry(QtCore.QRect(10, 70, 151, 20))
        self.roasting.setObjectName("roasting")
        self.ground = QtWidgets.QLineEdit(Form)
        self.ground.setGeometry(QtCore.QRect(10, 100, 151, 20))
        self.ground.setObjectName("ground")
        self.taste = QtWidgets.QLineEdit(Form)
        self.taste.setGeometry(QtCore.QRect(10, 130, 151, 20))
        self.taste.setObjectName("taste")
        self.price = QtWidgets.QSpinBox(Form)
        self.price.setGeometry(QtCore.QRect(10, 160, 151, 22))
        self.price.setObjectName("price")
        self.packege = QtWidgets.QSpinBox(Form)
        self.packege.setGeometry(QtCore.QRect(10, 190, 151, 22))
        self.packege.setObjectName("packege")
        self.select_box = QtWidgets.QComboBox(Form)
        self.select_box.setGeometry(QtCore.QRect(10, 10, 151, 22))
        self.select_box.setObjectName("select_box")
        self.chenge = QtWidgets.QPushButton(Form)
        self.chenge.setGeometry(QtCore.QRect(10, 220, 75, 23))
        self.chenge.setObjectName("chenge")
        self.create_b = QtWidgets.QPushButton(Form)
        self.create_b.setGeometry(QtCore.QRect(90, 220, 75, 23))
        self.create_b.setObjectName("create_b")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.chenge.setText(_translate("Form", "Изменить"))
        self.create_b.setText(_translate("Form", "Создать"))
