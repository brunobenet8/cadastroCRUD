# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget, QTableWidget, QTableWidgetItem
import CRUD

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(652, 422)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 651, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.comboBox = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 40, 651, 381))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableWidget = QtGui.QTableWidget(self.horizontalLayoutWidget_2)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.preenche

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "..:: Pesquisa ::..", None))
        self.label.setText(_translate("Dialog", "Pesquisa:", None))
        self.comboBox.setItemText(0, _translate("Dialog", "ID", None))
        self.comboBox.setItemText(1, _translate("Dialog", "Nome", None))
        self.comboBox.setItemText(2, _translate("Dialog", "Endereco", None))
        self.comboBox.setItemText(3, _translate("Dialog", "Obs", None))
        self.pushButton.setText(_translate("Dialog", "Buscar", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nome", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Endereco", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Obs", None))
        self.pushButton.clicked.connect(self.pesquisar)


    def preenche(self):
        self.tableWidget.setRowCount(0)
        for linha in range(len(CRUD.carregar())):
            self.tableWidget.insertRow(linha)
            self.tableWidget.setItem(linha,0, QTableWidgetItem(str(CRUD.carregar()[linha][0])))
            self.tableWidget.setItem(linha,1, QTableWidgetItem(str(CRUD.carregar()[linha][1])))
            self.tableWidget.setItem(linha,2, QTableWidgetItem(str(CRUD.carregar()[linha][2])))
            self.tableWidget.setItem(linha,3, QTableWidgetItem(str(CRUD.carregar()[linha][3])))


    def pesquisar(self):
        self.tableWidget.setRowCount(0)
        for linha in range(len(CRUD.buscar(self.comboBox.currentIndex(), str(self.lineEdit.text())))):
                self.tableWidget.insertRow(linha)
                self.tableWidget.setItem(linha,0, QTableWidgetItem(str(CRUD.buscar(self.comboBox.currentIndex(), str(self.lineEdit.text()))[linha][0])))
                self.tableWidget.setItem(linha,1, QTableWidgetItem(str(CRUD.buscar(self.comboBox.currentIndex(), str(self.lineEdit.text()))[linha][1])))
                self.tableWidget.setItem(linha,2, QTableWidgetItem(str(CRUD.buscar(self.comboBox.currentIndex(), str(self.lineEdit.text()))[linha][2])))
                self.tableWidget.setItem(linha,3, QTableWidgetItem(str(CRUD.buscar(self.comboBox.currentIndex(), str(self.lineEdit.text()))[linha][3])))
