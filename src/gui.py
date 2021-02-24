# -*- coding: utf-8 -*-
#! /usr/local/bin/python3

import sys
import string
from src.widgets import WordLabel,MatchesLabel,TranslationLabel,UpperComboBox
from PyQt6.QtCore import *
from PyQt6.QtWidgets import (QApplication, QListView, QMainWindow, QTableView, QWidget, QMenuBar, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QTextBrowser, QStatusBar)


class Window(QMainWindow):
    def __init__(self,app,parent=None):
        super().__init__(parent=parent)
        self.app = app
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("Window")
        self.resize(1000,500)

        self.central = QWidget(self)
        self.central_layout = QVBoxLayout()
        self.vert_layout_1 = QVBoxLayout()
        self.vert_layout_2 = QVBoxLayout()
        self.vert_layout_3 = QVBoxLayout()
        self.vert_layout_4 = QVBoxLayout()
        self.horiz_layout_1 = QHBoxLayout()
        self.horiz_layout_2 = QHBoxLayout()
        self.horiz_layout_3 = QHBoxLayout()
        self.line_edit = QLineEdit(self.central)
        self.submit_phrase = QPushButton(self.central)
        self.submit_char = QPushButton(self.central)
        self.old_label = WordLabel(self.central)
        self.new_label = MatchesLabel(self.central)
        self.translation_label = TranslationLabel(self.central)
        self.old_list_view = QListView(self.central)
        self.new_list_view = QListView(self.central)
        self.table = QTableView(self.central)
        self.text_browser = QTextBrowser(self.central)
        self.old_combo_box = UpperComboBox(self.central)
        self.new_combo_box = UpperComboBox(self.central)
        self.menubar = QMenuBar(self)
        self.statusbar = QStatusBar(self)

        self.central.setObjectName("central")
        self.line_edit.setObjectName("line_edit")
        self.submit_phrase.setObjectName("Submit Phrase")
        self.submit_char.setObjectName("Submit Character")
        self.old_list_view.setObjectName("old_list_view")
        self.new_list_view.setObjectName("new_list_view")
        self.table.setObjectName("table")
        self.text_browser.setObjectName("text_browser")
        self.old_combo_box.setObjectName("old_combo_box")
        self.new_combo_box.setObjectName("new_combo_box")
        self.menubar.setObjectName("menubar")
        self.statusbar.setObjectName("statusbar")

        self.submit_phrase.setText("Submit Encrypted Phrase")
        self.submit_char.setText("Submit Characters (old:new)")
        self.setCentralWidget(self.central)
        self.setMenuBar(self.menubar)
        self.file_menu = FileMenu(self.menubar)
        self.menubar.addMenu(self.file_menu)
        self.menubar.setVisible(True)
        self.setStatusBar(self.statusbar)

        self.central.setLayout(self.central_layout)
        self.central_layout.addLayout(self.horiz_layout_1)
        self.central_layout.addLayout(self.horiz_layout_2)
        self.central_layout.addWidget(self.text_browser)
        self.horiz_layout_1.addWidget(self.submit_phrase)
        self.horiz_layout_1.addWidget(self.line_edit)
        self.horiz_layout_2.addLayout(self.vert_layout_1)
        self.horiz_layout_2.addLayout(self.vert_layout_2)
        self.horiz_layout_2.addLayout(self.vert_layout_3)
        self.vert_layout_1.addWidget(self.old_label)
        self.vert_layout_1.addWidget(self.old_list_view)
        self.vert_layout_2.addWidget(self.new_label)
        self.vert_layout_2.addWidget(self.new_list_view)
        self.vert_layout_3.addWidget(self.translation_label)
        self.vert_layout_3.addWidget(self.table)
        self.vert_layout_3.addLayout(self.horiz_layout_3)
        self.vert_layout_3.addWidget(self.submit_char)
        self.horiz_layout_3.addWidget(self.old_combo_box)
        self.horiz_layout_3.addWidget(self.new_combo_box)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Window(app,parent=None)
    main.show()
    sys.exit(app.exec())
