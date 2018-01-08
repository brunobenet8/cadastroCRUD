#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Application(QWidget):
    def __init__(self):
        self.w = QMainWindow()
        self.menubar = self.w.menuBar()
        self.cadastro = self.menubar.addMenu('Cadastros')
        self.cadastro.addAction('Cadastro')
        self.cadastro.addAction('Pesquisa')
        self.sb = QStatusBar()
        self.l1 = QLabel('Sistema de Cadastro de Contatos')
        self.sb.addWidget(self.l1)
        self.w.setStatusBar(self.sb)
        self.w.resize(320, 240)
        self.w.setWindowTitle('..:: Contatos ::..')
        self.w.show()


app = QApplication(sys.argv)
a = Application()
sys.exit(app.exec_())
