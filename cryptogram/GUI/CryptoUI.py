import string
import sys
import os
import json
from PyQt5.QtWidgets import (QWidget,QGridLayout,QLabel,QComboBox,
                             QPushButton,QCheckBox,QLineEdit,
                             QMainWindow,QApplication,QTextBrowser,
                             QListWidget,QTableWidget,QVBoxLayout,
                             QHBoxLayout,QTextEdit,QListWidgetItem)
from PyQt5.QtGui import QFont



class CryptUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("Main Window")
        self.setWindowTitle("CryptoGram v0.1.1")
        self.resize(800,600)
        self.key_id = 0
        self.setupUi()

    def setupUi(self):
        self.central = QWidget(self)
        self.keys = QListWidget()
        self.vals = QListWidget()
        self.vals.setSelectionMode(0)
        self.phrase = QLineEdit()
        self.output = QTextBrowser()
        self.key_combo = QComboBox()
        self.val_combo = QComboBox()
        self.font = QFont("Folio Book BT")
        self.font.setBold(False)
        self.font.setPointSize(12)
        self.central.setFont(self.font)

        self.key_combo.addItems([i for i in string.ascii_uppercase])
        self.val_combo.addItems([i for i in string.ascii_uppercase])

        self.vals.setMaximumWidth(100)
        self.vals.setMaximumHeight(400)
        self.keys.setMaximumHeight(400)
        self.keys.setMaximumWidth(100)

        # Buttons and Labels
        oldLabel = QLabel("Old")
        newLabel = QLabel("New")
        submit_btn = QPushButton("&Submit Phrase")
        add_keys_btn = QPushButton("&Add Key")
        remove_keys_btn = QPushButton("&Remove Keys")

        # Layouts
        HLayout1 = QHBoxLayout()
        HLayout2 = QHBoxLayout()
        HLayout3 = QHBoxLayout()
        VLayout0 = QVBoxLayout()
        VLayout1 = QVBoxLayout()
        VLayout2 = QVBoxLayout()
        VLayout3 = QVBoxLayout()
        GLayout1 = QGridLayout()
        GLayout2 = QGridLayout()

        # Line Edit
        # Output Results
        GLayout1.addWidget(submit_btn,0,0)
        GLayout1.addWidget(self.phrase,0,1)
        GLayout1.addLayout(HLayout3,1,0,1,2)
        # GLayout1.addWidget(self.output,1,0,1,2)
        # VLayout2.addLayout(HLayout1)


        # Keys
        VLayout0.addWidget(oldLabel)
        VLayout0.addWidget(self.keys)
        VLayout0.addWidget(self.key_combo)

        # Vals
        VLayout1.addWidget(newLabel)
        VLayout1.addWidget(self.vals)
        VLayout1.addWidget(self.val_combo)

        # Keys + Vals
        GLayout2.addLayout(VLayout0,0,0)
        GLayout2.addLayout(VLayout1,0,1)

        # Keys + Vals + Buttons
        # VLayout3.addLayout(HLayout2)
        GLayout2.addWidget(add_keys_btn,1,0,1,2)
        GLayout2.addWidget(remove_keys_btn,2,0,1,2)

        # All Widgets
        HLayout3.addWidget(self.output)
        HLayout3.addLayout(GLayout2)

        # Assign Button Actions
        submit_btn.clicked.connect(self.submit_phrase)
        add_keys_btn.clicked.connect(self.add_keys)
        remove_keys_btn.clicked.connect(self.remove_keys)

        # Final Assignments
        self.central.setLayout(GLayout1)
        self.central.setObjectName("central")
        self.setCentralWidget(self.central)


    def remove_keys(self):
        item = self.keys.currentItem()
        item_idx = self.keys.indexFromItem(item)
        val_item = self.vals.itemFromIndex(item_idx)
        self.vals.takeItem(item_idx.row())
        self.keys.takeItem(item_idx.row())

    def add_keys(self):
        k = self.key_combo.currentText()
        v = self.val_combo.currentText()
        self.keys.addItem(k)
        self.vals.addItem(v)

    def find_matches(self):
        pass

    def submit_phrase(self,event):
        for row in range(self.keys.count()):
            key = self.keys.item(row)
            val = self.vals.item(row)
            d = {self.key_id:{key.text():val.text()}}
            self.key_id += 1
            if self.output.toPlainText():
                old = json.loads(self.output.toPlainText())
                self.output.clear()
                old.update(d)
                d = old
            txt = json.dumps(d)
            self.output.setText(txt)
        phrase = self.phrase.text()
        print(phrase)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CryptUI()
    window.show()
    sys.exit(app.exec_())
