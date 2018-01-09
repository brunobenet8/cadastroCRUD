#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import T_Cadastro
import T_Busca


class Application(QWidget):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.w = QMainWindow()

        self.buscar = QAction('Pesquisa', self)
        self.buscar.triggered.connect(self.busca)

        self.cadastrar = QAction('Cadastro', self)
        self.cadastrar.triggered.connect(self.cadastro)

        self.menubar = self.w.menuBar()
        self.cadastro = self.menubar.addMenu('Cadastros')

        self.cadastro.addAction(self.cadastrar)
        self.cadastro.addAction(self.buscar)

        self.sb = QStatusBar()
        self.l1 = QLabel('Sistema de Cadastro de Contatos')
        self.sb.addWidget(self.l1)

        self.w.setStatusBar(self.sb)
        self.w.resize(320, 240)
        self.w.setWindowTitle('..:: Contatos ::..')
        self.w.show()

    def busca(self):
        busca = T_Busca.Application()
        busca.exec_()

    def cadastro(self):
        cadastro = T_Cadastro.TCadastro()
        cadastro.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = Application()
    sys.exit(app.exec_())