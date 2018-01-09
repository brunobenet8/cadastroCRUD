#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import CRUD

class Application(QWidget):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.fbox = QFormLayout()

        self.l1 = QLabel("Busca:")
        self.t1 = QLineEdit()
        self.b1 = QPushButton("Buscar")

        self.cb = QComboBox()
        self.cb.addItem("ID")
        self.cb.addItem("Nome")
        self.cb.addItem("Telefone")
        self.cb.addItem("Obs")

        self.vbox = QHBoxLayout()
        self.vbox.addWidget(self.t1)
        self.vbox.addWidget(self.cb)
        self.vbox.addWidget(self.b1)


        self.h1 = QFrame()
        self.h1.setFrameShape(QFrame.HLine)
        self.h1.setFrameShadow(QFrame.Sunken)

        self.tb = QTableWidget()
        self.tb.resizeRowsToContents()
        self.tb.setColumnCount(4)
        self.tb.setHorizontalHeaderLabels(QString("ID;Nome;Telefone;Obs").split(";"))
        for linha in range(len(CRUD.carregar())):
            self.tb.insertRow(linha)
            self.tb.setItem(linha,0, QTableWidgetItem(str(CRUD.carregar()[linha][0])))
            self.tb.setItem(linha,1, QTableWidgetItem(str(CRUD.carregar()[linha][1])))
            self.tb.setItem(linha,2, QTableWidgetItem(str(CRUD.carregar()[linha][2])))
            self.tb.setItem(linha,3, QTableWidgetItem(str(CRUD.carregar()[linha][3])))

        self.fbox.addRow(self.l1, self.vbox)
        self.fbox.addRow(self.h1)
        self.fbox.addRow(self.tb)

        self.w = QWidget()
        self.w.setLayout(self.fbox)
        self.w.setWindowTitle('..:: Tela de Busca ::..')
        self.w.setGeometry(100,100,600,250)
        self.w.show()

"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Application()
    sys.exit(app.exec_())"""
