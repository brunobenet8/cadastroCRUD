# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QWidget
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
        Dialog.resize(569, 383)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 581, 321))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayoutWidget = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 571, 321))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(239, 320, 331, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.buscar)
        self.pushButton_2.clicked.connect(self.limpar)
        self.pushButton_3.clicked.connect(self.cadastrar)


    def buscar(self):
        if(len(self.lineEdit.text()) > 0):
            if(CRUD.listar(self.lineEdit.text()) > 1):
                self.lineEdit_3.setText(str(CRUD.listar(self.lineEdit.text())[2]))
                self.lineEdit_2.setText(str(CRUD.listar(self.lineEdit.text())[1]))
                self.lineEdit_4.setText(str(CRUD.listar(self.lineEdit.text())[3]))
            else:
                self.mensagem("ID nao encontrado!")
                self.limpar()
        else:
            self.mensagem("Campo vazio!")
            self.limpar()

    def limpar(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')


    def cadastrar(self):
        self.id = self.lineEdit.text()
        self.nome = self.lineEdit_2.text()
        self.endereco = self.lineEdit_3.text()
        self.obs = self.lineEdit_4.text()
        if(len(self.lineEdit.text()) > 0):
            self.mensagem(str(CRUD.alterar(str(self.id),str(self.nome),str(self.endereco),str(self.obs))))
        else:
            self.mensagem(str(CRUD.inserir(str(self.nome), str(self.endereco), str(self.obs))))
        self.limpar()


    def excluir(self):
        self.mensagem(str(CRUD.deletar(self.lineEdit.text())))


    def mensagem(self, msg):
        w = QWidget()
        QMessageBox.information(w, 'Mensagem', msg)
        w.show()


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "..:: Cadastro ::..", None))
        self.label_2.setText(_translate("Dialog", "ID:", None))
        self.pushButton.setText(_translate("Dialog", "Buscar", None))
        self.label.setText(_translate("Dialog", "Nome:", None))
        self.label_3.setText(_translate("Dialog", "Telefone:", None))
        self.label_4.setText(_translate("Dialog", "Obs.:", None))
        self.pushButton_3.setText(_translate("Dialog", "Salvar", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar", None))

