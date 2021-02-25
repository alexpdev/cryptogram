#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.widgets import (WordLabel, MatchesLabel, UpperComboBox,
                        WordList, MatchesList, FileMenu,
                        SubmitPhraseButton, SubmitCharButton, ChosenList, RemoveWordButton, RemoveCharButton, Table)
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                            QWidget, QMenuBar,
                            QVBoxLayout, QHBoxLayout, QGridLayout,
                            QLineEdit, QTextBrowser, QStatusBar)


class Window(QMainWindow):
    def __init__(self,app,parent=None):
        super().__init__(parent=parent)
        self.app = app
        self.setObjectName("Window")
        self.resize(1000,500)
        self.setup_ui()

    def setup_ui(self):
        self.central = QWidget(self)
        self.central_layout = QVBoxLayout()
        self.vert_layout_1 = QVBoxLayout()
        self.vert_layout_2 = QVBoxLayout()
        self.vert_layout_3 = QVBoxLayout()
        self.vert_layout_4 = QVBoxLayout()
        self.horiz_layout_1 = QHBoxLayout()
        self.horiz_layout_2 = QHBoxLayout()
        self.horiz_layout_3 = QHBoxLayout()
        self.horiz_layout_4 = QHBoxLayout()
        self.grid_layout = QGridLayout()
        self.line_edit = QLineEdit(self.central)
        self.submit_phrase = SubmitPhraseButton(self.central)
        self.submit_char = SubmitCharButton(self.central)
        self.remove_char = RemoveCharButton(self.central)
        self.remove_word = RemoveWordButton(self.central)
        self.old_label = WordLabel(self.central)
        self.new_label = MatchesLabel(self.central)
        self.word_list = WordList(self.central)
        self.matches_list = MatchesList(self.central)
        self.chosen_list = ChosenList(self.central)
        self.table = Table(0,2,self.central)
        self.text_browser = QTextBrowser(self.central)
        self.old_combo = UpperComboBox(self.central)
        self.new_combo = UpperComboBox(self.central)
        self.menubar = QMenuBar(self)
        self.statusbar = QStatusBar(self)
        self.file_menu = FileMenu(self.menubar)

        self.central.setObjectName("central")
        self.line_edit.setObjectName("line_edit")
        self.text_browser.setObjectName("text_browser")
        self.menubar.setObjectName("menubar")
        self.statusbar.setObjectName("statusbar")

        self.setCentralWidget(self.central)
        self.setStatusBar(self.statusbar)
        self.setMenuBar(self.menubar)
        self.menubar.addMenu(self.file_menu)
        self.menubar.setVisible(True)

        self.central.setLayout(self.central_layout)
        self.central_layout.addLayout(self.horiz_layout_1)
        self.horiz_layout_1.addWidget(self.submit_phrase)
        self.horiz_layout_1.addWidget(self.line_edit)
        self.horiz_layout_2.addWidget(self.old_combo)
        self.horiz_layout_2.addWidget(self.new_combo)
        self.horiz_layout_3.addWidget(self.submit_char)
        self.horiz_layout_3.addWidget(self.remove_char)
        self.vert_layout_1.addWidget(self.table)
        self.vert_layout_1.addLayout(self.horiz_layout_2)
        self.vert_layout_1.addLayout(self.horiz_layout_3)
        self.vert_layout_2.addWidget(self.chosen_list)
        self.vert_layout_2.addWidget(self.remove_word)
        self.vert_layout_1.addLayout(self.vert_layout_2)
        self.grid_layout.addWidget(self.old_label,0,0)
        self.grid_layout.addWidget(self.word_list,1,0)
        self.grid_layout.addWidget(self.new_label,2,0)
        self.grid_layout.addWidget(self.matches_list,3,0)
        self.horiz_layout_4.addLayout(self.vert_layout_1)
        self.horiz_layout_4.addLayout(self.grid_layout)
        self.horiz_layout_4.addWidget(self.text_browser)
        self.central_layout.addLayout(self.horiz_layout_1)
        self.central_layout.addLayout(self.horiz_layout_4)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Window(app,parent=None)
    main.show()
    # main.after()
    sys.exit(app.exec())
