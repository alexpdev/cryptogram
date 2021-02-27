#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.widgets import (WordLabel, MatchesLabel, UpperComboBox,
                        WordList, MatchesList, FileMenu,
                        SubmitPhraseButton, SubmitCharButton,
                        ChosenList, RemoveWordButton, RemoveCharButton,
                        Table, SolveButton, AutoCheck)
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                            QWidget, QMenuBar,
                            QVBoxLayout, QHBoxLayout, QGridLayout,
                            QLineEdit, QTextBrowser, QStatusBar)


class Window(QMainWindow):
    def __init__(self,app,parent=None):
        super().__init__(parent=parent)
        self.app = app
        self._phrase = None
        self.setObjectName("Window")
        self.resize(900,800)
        self.setup_ui()

    def setup_ui(self):
        self.central = QWidget(self)
        self.central_layout = QVBoxLayout()
        self.vert_layout_1 = QVBoxLayout()
        self.vert_layout_2 = QVBoxLayout()
        self.vert_layout_3 = QVBoxLayout()
        self.horiz_layout_1 = QHBoxLayout()
        self.horiz_layout_2 = QHBoxLayout()
        self.grid_layout_2 = QGridLayout()
        self.line_edit = QLineEdit(self.central)
        self.table = Table(0,2,self.central)
        self.submit_phrase = SubmitPhraseButton(self.central)
        self.submit_char = SubmitCharButton(self.central)
        self.remove_char = RemoveCharButton(self.central)
        self.chosen_list = ChosenList(self.central)
        self.remove_word = RemoveWordButton(self.central)
        self.solve_button = SolveButton(self.central)
        self.auto_check = AutoCheck(self.central)
        self.word_list = WordList(self.central)
        self.matches_list = MatchesList(self.central)
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
        self.horiz_layout_1.addWidget(self.submit_phrase)
        self.horiz_layout_1.addWidget(self.line_edit)
        self.vert_layout_1.addWidget(self.chosen_list)
        self.vert_layout_1.addWidget(self.remove_word)
        self.vert_layout_2.addWidget(self.solve_button)
        self.vert_layout_2.addWidget(self.word_list)
        self.vert_layout_3.addWidget(self.auto_check)
        self.vert_layout_3.addWidget(self.matches_list)
        self.grid_layout_2.addWidget(self.table,1,0,1,2)
        self.grid_layout_2.addWidget(self.old_combo,2,0,1,1)
        self.grid_layout_2.addWidget(self.new_combo,2,1,1,1)
        self.grid_layout_2.addWidget(self.submit_char,4,0,1,1)
        self.grid_layout_2.addWidget(self.remove_char,4,1,1,1)
        self.horiz_layout_2.addLayout(self.vert_layout_2)
        self.horiz_layout_2.addLayout(self.vert_layout_3)
        self.horiz_layout_2.addLayout(self.grid_layout_2)
        self.horiz_layout_2.addLayout(self.vert_layout_1)
        self.central_layout.addLayout(self.horiz_layout_1)
        self.central_layout.addLayout(self.horiz_layout_2)
        self.central_layout.addWidget(self.text_browser)

        self.custom_widgets = [self.table, self.submit_phrase, self.submit_char,
                            self.remove_char, self.chosen_list, self.remove_word,
                            self.solve_button, self.auto_check, self.word_list,
                            self.matches_list, self.old_combo, self.new_combo,
                            self.file_menu]

    def setWidgetWindow(self,window):
        for widget in self.custom_widgets:
            widget.setWindow(window)

    @property
    def phrase(self):
        return self._phrase

    def setPhrase(self,phrase):
        self._phrase = phrase



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Window(app,parent=None)
    main.show()
    main.setWidgetWindow(main)
    # main.after()
    sys.exit(app.exec())
