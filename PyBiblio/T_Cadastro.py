#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import CRUD


class TCadastro(QWidget):
    def __init__(self, parent=None):

        super(TCadastro, self).__init__(parent)
        self.l1 = QLabel("ID:")
        self.t1 = QLineEdit()
        self.b1 = QPushButton("...")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.t1)
        self.hbox.addWidget(self.b1)

        self.h1 = QFrame()
        self.h1.setFrameShape(QFrame.HLine)
        self.h1.setFrameShadow(QFrame.Sunken)

        self.h2 = QFrame()
        self.h2.setFrameShape(QFrame.HLine)
        self.h2.setFrameShadow(QFrame.Sunken)

        self.l2 = QLabel("Nome:")
        self.t2 = QLineEdit()

        self.l3 = QLabel("Telefone:")
        self.t3 = QLineEdit()

        self.l4 = QLabel("Obs:")
        self.t4 = QLineEdit()

        self.b2 = QPushButton("Salvar")
        self.b3 = QPushButton("Cancelar")

        self.fbox = QFormLayout()
        self.fbox.addRow(self.l1, self.hbox)
        self.fbox.addRow(self.h1)
        self.fbox.addRow(self.l2, self.t2)
        self.fbox.addRow(self.l3, self.t3)
        self.fbox.addRow(self.l4, self.t4)
        self.fbox.addRow(self.h2)
        self.fbox.addRow(self.b2, self.b3)

        self.w = QWidget()
        self.w.setLayout(self.fbox)
        self.w.setWindowTitle("..:: Tela de Cadastro ::..")
        self.w.setGeometry(100, 100, 400, 200)
        self.w.show()


"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Application()
    sys.exit(app.exec_())"""
