#! /usr/bin/python3
# -*- coding: utf-8 -*-

from cryptogram.widgets import (UpperComboBox, WordList, MatchesList,
                        FileMenu, SubmitPhraseButton, SubmitCharButton,
                        ChosenList, RemoveWordButton, RemoveCharButton,
                        Table, SolveButton, MatchesLabel, HelpMenu)

from PyQt6.QtWidgets import (QMainWindow, QWidget, QMenuBar,
                            QVBoxLayout, QHBoxLayout, QGridLayout,
                            QLineEdit, QTextBrowser, QStatusBar)

from PyQt6.QtGui import QIcon

class Window(QMainWindow):
    styleSheet = "QMainWindow {background-color: #737373;}"

    def __init__(self,app,parent=None):
        super().__init__(parent=parent)
        self.app = app
        self._phrase = None
        self._driver = None
        self.setWindowTitle("Cryptogram")
        self.setWindowIcon(QIcon("img/crypto.png"))
        self.setObjectName("Window")
        self.resize(900,800)
        self.setup_ui()
        self.assign_window()

    @property
    def phrase(self):
        return self._phrase

    @property
    def driver(self):
        return self._driver

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
        self.word_list = WordList(self.central)
        self.matches_list = MatchesList(self.central)
        self.text_browser = QTextBrowser(self.central)
        self.old_combo = UpperComboBox(self.central)
        self.new_combo = UpperComboBox(self.central)
        self.matches_label = MatchesLabel(self.central)
        self.menubar = QMenuBar(self)
        self.statusbar = QStatusBar(self)
        self.file_menu = FileMenu(self.menubar)
        self.help_menu = HelpMenu(self.menubar)

        self.central.setObjectName("central")
        self.line_edit.setObjectName("line_edit")
        self.text_browser.setObjectName("text_browser")
        self.menubar.setObjectName("menubar")
        self.statusbar.setObjectName("statusbar")

        self.setCentralWidget(self.central)
        self.setStatusBar(self.statusbar)
        self.setMenuBar(self.menubar)
        self.menubar.addMenu(self.file_menu)
        self.menubar.addMenu(self.help_menu)
        self.menubar.setVisible(True)
        self.setStyleSheet(self.styleSheet)

        self.central.setLayout(self.central_layout)
        self.horiz_layout_1.addWidget(self.submit_phrase)
        self.horiz_layout_1.addWidget(self.line_edit)
        self.vert_layout_1.addWidget(self.chosen_list)
        self.vert_layout_1.addWidget(self.remove_word)
        self.vert_layout_2.addWidget(self.solve_button)
        self.vert_layout_2.addWidget(self.word_list)
        self.vert_layout_3.addWidget(self.matches_label)
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
                            self.solve_button, self.word_list, self.matches_list,
                            self.old_combo, self.new_combo, self.file_menu, self.help_menu]

    def re_update(self):
        widgets = [self.table,self.chosen_list,self.word_list,self.matches_list,self.text_browser, self.line_edit]
        for widget in widgets:
            widget.repaint()
        self.update()

    def assign_window(self):
        for widget in self.custom_widgets:
            widget.setWindow(self)

    def setPhrase(self,phrase):
        self._phrase = phrase
        self.driver.setPhrase(phrase)

    def setDriver(self,driver):
        self._driver = driver
