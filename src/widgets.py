#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import string

from PyQt6.QtWidgets import (QComboBox, QLabel, QListWidgetItem,
                            QMenu, QListWidget, QListWidgetItem,
                            QPushButton, QTableWidget, QHeaderView, QTableWidgetItem)

from PyQt6.QtGui import QFont, QAction

from src.phrase import Phrase


class TableItem(QTableWidgetItem):

    def __init__(self,type=0):
        super().__init__(type=type)
        self.row = None
        self.column = None
        self.text = None

    def assign_location(self,row,column):
        self.row = row
        self.column = column

class Table(QTableWidget):

    def __init__(self,rows,columns,parent=None):
        super().__init__(rows,columns,parent=parent)
        self.parent = parent
        self.setObjectName("table")
        self.setHorizontalHeaderLabels(["OLD","NEW"])
        self.showGrid()
        self.setEditTriggers(QTableWidget.EditTriggers(0))
        headers = self.horizontalHeader()
        headers.setSectionResizeMode(0,QHeaderView.ResizeMode(1))
        headers.setSectionResizeMode(1,QHeaderView.ResizeMode(1))
        self.itemSelectionChanged.connect(self.select_row)

    def select_row(self):
        row = self.currentRow()
        self.selectRow(row)



class UpperComboBox(QComboBox):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setObjectName("Upper_Combo_Box")
        self.addItems([i for i in string.ascii_uppercase])
        self.setEditable(False)
        self.setFont(BoldFont())


class BoldFont(QFont):

    def __init__(self):
        super().__init__()
        self.setBold(True)


class WordLabel(QLabel):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setObjectName("word_label")
        self.setText("Words")
        self.setFont(BoldFont())
        self.setIndent(8)


class MatchesLabel(QLabel):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setObjectName("matches_label")
        self.setText("Matches")
        self.setFont(BoldFont())
        self.setIndent(8)


class TranslationLabel(QLabel):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setObjectName("translation_label")
        self.setText("Character Translation Table")
        self.setFont(BoldFont())
        self.setIndent(8)

class FileMenu(QMenu):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setTitle("File")
        exit_action = QAction(parent=self)
        exit_action.setText("Exit")
        clear_action = QAction(parent=self)
        clear_action.setText("Clear")
        self.addAction(exit_action)
        self.addAction(clear_action)
        exit_action.triggered.connect(self.destroy)
        clear_action.triggered.connect(self.clear)

    def destroy(self):
        sys.exit(self.parent.parent().app.exec)

    def clear(self):
        main_window = self.parent.parent()
        main_window.table.clear()
        main_window.word_list.clear()
        main_window.matches_list.clear()
        main_window.text_browser.clear()

class WordList(QListWidget):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setObjectName("Word_List")
        self.parent = parent
        self.currentItemChanged.connect(self.fill_matches)

    def fill_matches(self):
        matches_list = self.parent.parent().matches_list
        if word := self.currentItem():
            matches = list(word.obj.matches)
            matches_list.add_items(matches)

    def add_items(self,items):
        for item in items:
            word = WordListItem(item,parent=self)
            self.addItem(word)

class WordListItem(QListWidgetItem):

    def __init__(self,obj,parent=None):
        super().__init__(parent=parent)
        self.obj = obj
        self.setText(str(obj))

    def get_matches(self):
        if self.obj.matches:
            return list(self.object.matches)

class ChosenList(QListWidget):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setObjectName("Chosen_List")
        self.parent =parent

    def add_item(self,word):
        self.addItem(word)

class MatchesList(QListWidget):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setObjectName("Matches_List")
        self.parent =parent

    def add_items(self,items):
        self.clear()
        for item in items:
            self.addItem(item)

class SubmitPhraseButton(QPushButton):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setObjectName("submit_phrase")
        self.setText("Submit Phrase")
        self.pressed.connect(self.submit)

    def submit(self):
        p = self.parent.parent()
        text = p.line_edit.text()
        phrase = Phrase(text)
        wordlist = p.word_list
        wordlist.add_items(phrase.words)

class RemoveCharButton(QPushButton):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setObjectName("remove_char")
        self.setText("Remove Characters (old:new)")
        self.pressed.connect(self.remove)

    def remove(self):
        row = self.parent.parent().table.currentRow()
        self.paren.parent().table.takeItem(row)

class RemoveWordButton(QPushButton):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setObjectName("remove_word")
        self.setText("Remove Word")

class SolveButton(QPushButton):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setObjectName("solve")
        self.setText("Solve")

class SubmitCharButton(QPushButton):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setObjectName("submit_char")
        self.setText("Submit Characters (old:new)")
        self.pressed.connect(self.submit)

    def submit(self):
        old_txt = self.parent.parent().old_combo.currentText()
        new_txt = self.parent.parent().new_combo.currentText()
        index = self.parent.parent().table.rowCount()
        self.parent.parent().table.insertRow(index)
        item1 = TableItem(type=0)
        item1.assign_location(index,0)
        item2 = TableItem(type=0)
        item2.assign_location(index,1)
        item1.setText(old_txt)
        item2.setText(new_txt)
        self.parent.parent().table.setItem(index,0,item1)
        self.parent.parent().table.setItem(index,1,item2)

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
