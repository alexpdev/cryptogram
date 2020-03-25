# /usr/bin/python3
# ~*~ charset: utf8 ~*~
# Cryptogram: version 0.1.1
#############################################################################
##
## Copyright (C) 2020 ASPDEV.
##
## Cryptogram v0.1.1
## All rights reserved.
##
## You may use this file under the terms of the PLv3 license:
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
##
#############################################################################

import sys
import os
import string


from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QLabel, QComboBox, QMenu, QMenuBar, QListWidget,
                             QListWidgetItem, QGridLayout, QPushButton,
                             QPlainTextEdit, QTableWidget, QTableWidgetItem,
                             QSplitter, QVBoxLayout, QHBoxLayout)

from PyQt5.QtGui import QStandardItemModel, QFont

from PyQt5.QtCore import Qt, QModelIndex, QCoreApplication

sys.path.append(os.getcwd())

from cryptogram.utils import start_decryption, stop_decryption

class Window(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("Window")
        self.resize(1000,500)
        self.setup_widgets()
        self.setup_layout()
        self.setCentralWidget(self.central)
        self.central.setLayout(self.grid)
        self.btn3.clicked.connect(self.add_to_key)
        self.btn1.clicked.connect(self.start_crypto)
        self.btn2.clicked.connect(self.stop_crypto)
        self.btn4.clicked.connect(self.remove_from_key)


    def setup_widgets(self):
        self.grid = QGridLayout()
        self.central = QWidget(parent=self)
        self.central.setObjectName("Central")
        self.phrase = QPlainTextEdit(parent=self)
        self.phrase.setObjectName("Phrase Editor")
        self.key_table = QTableWidget(parent=self)
        self.key_table.setObjectName("KeyTable")
        self.key_table.setColumnCount(2)
        self.key_table.adjustSize()
        self.key_table.setHorizontalHeaderLabels(["Old","New"])
        self.combo1 = QComboBox(parent=self)
        self.combo1.setObjectName("OldCombo")
        self.combo2 = QComboBox(parent=self)
        self.combo2.setObjectName("NewCombo")
        self.combo1.setEditable(False)
        self.combo2.setEditable(False)
        self.combo1.addItems([i for i in string.ascii_uppercase])
        self.combo2.addItems([i for i in string.ascii_uppercase])
        self.wList = QListWidget(self)
        self.wList.setObjectName("Guesses")
        self.btn1 = QPushButton("Start",parent=self)
        self.btn2 = QPushButton("Stop",parent=self)
        self.btn3 = QPushButton("Add Key",parent=self)
        self.btn4 = QPushButton("Remove Key",parent=self)
        self.word_table = QTableWidget(parent=self)
        self.word_table.setObjectName("WordTable")
        self.word_table.setRowCount(1)
        return

    def setup_layout(self):
        self.grid.addWidget(self.btn1,0,0,1,1)
        self.grid.addWidget(self.btn2,1,0,1,1)
        self.grid.addWidget(self.phrase,0,1,2,-1)
        self.vlayout = QVBoxLayout()
        self.hlayout = QHBoxLayout()
        self.vlayout.addWidget(self.key_table)
        self.hlayout.addWidget(self.combo1)
        self.hlayout.addWidget(self.combo2)
        self.vlayout.addLayout(self.hlayout)
        self.vlayout.addWidget(self.btn3)
        self.vlayout.addWidget(self.btn4)
        self.vertWidg = QWidget()
        self.vertWidg.setLayout(self.vlayout)
        self.splitter = QSplitter(parent=self.central)
        self.splitter.setStretchFactor(3,2)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter2 = QSplitter(parent=self.central)
        self.splitter2.addWidget(self.vertWidg)
        self.splitter.addWidget(self.wList)
        self.splitter.addWidget(self.word_table)
        self.splitter2.addWidget(self.splitter)
        self.splitter2.setStretchFactor(1,3)
        self.grid.addWidget(self.splitter2,2,0,-1,-1)

    def remove_from_key(self):
        idxs = self.key_table.currentRow()
        print(idxs)
        self.key_table.removeRow(idxs)

    def add_to_key(self):
        c1 = self.combo1.currentText()
        c2 = self.combo2.currentText()
        self.addKeys((c1,c2))

    def addKeys(self,keys):
        row_count = self.key_table.rowCount()
        self.key_table.setRowCount(row_count + 1)
        item1 = QTableWidgetItem(keys[0])
        item2 = QTableWidgetItem(keys[1])
        self.key_table.setItem(row_count,0,item1)
        self.key_table.setItem(row_count,1,item2)

    def start_crypto(self):
        phrase = self.phrase.toPlainText()
        rows = self.key_table.rowCount()
        key = {}
        for idx in range(rows):
            old = self.key_table.item(idx,0)
            new = self.key_table.item(idx,1)
            key[old.text()] = new.text()
        start_decryption(phrase,key,self)
        return

    def stop_crypto(self):
        stop_decryption()

    def add_keys(self,val):
        self.addKeys(val)
        self.key_table.repaint(self.key_table.geometry())
        return

    def remove_keys(self,val):
        for row in range(self.key_table.rowCount()):
            if self.key_table.item(row,0).text() == val:
                self.key_table.removeRow(row)
                break
        self.key_table.repaint(self.key_table.geometry())
        return

    def add_guess(self,val):
        c = self.wList.count()
        if c > 50:
            item = self.wList.takeItem(c-1)
            del item
        new_item = QListWidgetItem(val)
        self.wList.insertItem(0,new_item)
        self.wList.repaint(self.wList.geometry())
        QCoreApplication.processEvents()
        return

    def add_word(self,val):
        idx = self.word_table.rowCount()
        item = QTableWidgetItem(val)
        self.word_table.setItem(0,idx,item)
        return

    def remove_word(self,val):
        idx = self.word_table.rowCount()
        item = self.word_table.takeItem(0,idx-1)
        del item
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())
