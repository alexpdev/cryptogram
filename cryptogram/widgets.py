#! /usr/bin/python3
# -*- coding: utf-8 -*-

import string

from PyQt6.QtWidgets import (QComboBox, QLabel, QListWidgetItem,
                            QMenu, QListWidget, QListWidgetItem,
                            QPushButton, QTableWidget, QHeaderView,
                            QTableWidgetItem, QCheckBox, QSizePolicy)

from PyQt6.QtGui import QFont, QAction

from cryptogram.phrase import Phrase

# Sample QSS Style Sheet
"""
    {
        background-color: #000000;
        background-repeat: repeat-y;
        background origin: content;
        border: 1px solid #000000;
        border-radius: 3px;
        color: #000000;
        gridline-color: gray;  #QtableView Only
        font-style: bold;
        margin: 5px;
        padding: 5px;
        min-height: 100px;
        max-width: 100px;
        text-align: center;
        opacity: 223;
        selection-color: darkblue;
        selection-background-color: white;
    }
"""

class TableItem(QTableWidgetItem):
    """
    TableItem [widgets that fill in the tablewidgets]

    Args:
        QTableWidgetItem ([int]type=0): [int enum represening item type. default=0]
    """

    def __init__(self,type=0):
        super().__init__(type=type)
        self.row = None
        self.column = None
        self._window = None

    def window(self):
        """ getter method for MainWindow """
        return self._window

    def setWindow(self,window):
        """ setter method for MainWindow """
        self._window = window

    def assign_location(self,row,column):
        """ setter for internal reference to row and column indeces """
        self.row = row
        self.column = column

class Table(QTableWidget):
    """
    ## Table:
        Table Widget to represent Phrase.table attribute graphically

    ## Args:
        QTableWidget (int row, int col, obj parent=None):
    """

    styleSheet = """
        QTableWidget {
            background-color: white;
            alternate-background-color: #850;
            gridline-color: #ddd;
            selection-color: #600;
            border: 3px solid #743;
            selection-background-color: #8cd;
        }"""

    def __init__(self,rows,columns,parent=None):
        super().__init__(rows,columns,parent=parent)
        self._window = None
        self.setObjectName("table")
        self.setHorizontalHeaderLabels(["OLD","NEW"])
        self.showGrid()
        self.setStyleSheet(self.styleSheet)
        self.setEditTriggers(QTableWidget.EditTriggers(0))
        headers = self.horizontalHeader()
        headers.setSectionResizeMode(0,QHeaderView.ResizeMode(1))
        headers.setSectionResizeMode(1,QHeaderView.ResizeMode(1))
        self.setSizePolicy(QSizePolicy.Policy(4),QSizePolicy.Policy(5))
        self.itemSelectionChanged.connect(self.select_row)

    def window(self):
        """ getter method for MainWindow """
        return self._window

    def setWindow(self,window):
        """ getter method for MainWindow """
        self._window = window

    def get_contents(self):
        """ collect all value pairs in the table to use as phrase.table """
        chars = {}
        for num in range(self.rowCount()):
            old = self.item(num,0).text()
            new = self.item(num,1).text()
            chars[old] = new
        return chars

    def select_row(self):
        """ re-select row to update screen after rematching phrase words """
        row = self.currentRow()
        self.selectRow(row)

    def remove_row(self,row):
        """ remove the items in the row at index row """
        self.removeRow(row)

    def remove_keys(self,chars):
        """ Iterates through rows removing those that are in arguement `cars` """
        for num in list(range(0,self.rowCount()))[::-1]:
            if self.item(num,0).text() in chars:
                self.remove_row(num)

    def add_changes(self,changes):
        """ Add charachtes in dictionary `changes` to table. """
        for k,v in changes.items():
            self.add_chars(k,v)

    def add_chars(self,old,new):
        """ receives a current word in phrase(old) and a match(new) and adds their characters """
        row_num = self.rowCount()
        self.insertRow(row_num)
        for i,text in enumerate((old,new)):
            item = TableItem(type=0)
            item.setText(text)
            self.setItem(row_num,i,item)

class UpperComboBox(QComboBox):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setObjectName("Upper_Combo_Box")
        self.addItems([i for i in string.ascii_uppercase])
        self.setEditable(False)
        self.setFont(BoldFont())
        self._window = None

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

class BoldFont(QFont):

    def __init__(self):
        super().__init__()
        self.setBold(True)


class HelpMenu(QMenu):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._window = None
        self.setTitle("Help")
        about_action = QAction(parent=self)
        about_action.setText("About")
        self.addAction(about_action)
        about_action.triggered.connect(self.about_show)

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

    def about_show(self):
        self.window().app.aboutQt()


class FileMenu(QMenu):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self._window = None
        self.setTitle("File")
        exit_action = QAction(parent=self)
        exit_action.setText("Exit")
        clear_action = QAction(parent=self)
        clear_action.setText("Clear")
        self.addAction(exit_action)
        self.addAction(clear_action)
        exit_action.triggered.connect(self.destroy)
        clear_action.triggered.connect(self.clear)

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

    def destroy(self):
        self.window().app.closeAllWindows()

    def clear(self):
        self.window().table.clear()
        self.window().chosen_list.clear()
        self.window().word_list.clear()
        self.window().matches_list.clear()
        self.window().text_browser.clear()

class WordList(QListWidget):
    styleSheet = """
        QListWidget {
            background-color: white;
            alternate-background-color: #a83;
            selection-color: #680406;
            border: 3px solid #743;
            selection-background-color: #8cd;
            font-style: bold;
        }
        QListView::item {
            border: 2px solid black;
        }"""

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._window = None
        self.setStyleSheet(self.styleSheet)
        self.setObjectName("Word_List")
        self.currentItemChanged.connect(self.fill_matches)

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

    def fill_matches(self):
        matches_list = self.window().matches_list
        if not matches_list:
            matches_list.clear()
        word = self.currentItem()
        matches = list(word.obj.matches)
        matches_list.add_items(matches)

    def add_items(self,items):
        for item in items:
            word = WordListItem(item,parent=self)
            self.addItem(word)

class WordListItem(QListWidgetItem):

    def __init__(self,obj,parent=None):
        super().__init__(parent=parent)
        self.setText(str(obj))
        self._word = None
        self._window = None
        self.obj = obj

    def setWord(self,word):
        self._word = word

    def getWord(self):
        return self._word

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

    def get_matches(self):
        if self.obj.matches:
            return list(self.object.matches)

class ChosenList(QListWidget):
    styleSheet = """
    QListWidget {
        background-color: white;
        alternate-background-color: #a83;
        selection-color: #600;
        border: 1px solid #743;
        selection-background-color: #8cd;
        font-style: bold;
    }
    QListView::item {
        border: 1px solid black;
    }"""

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setObjectName("Chosen_List")
        self.setStyleSheet(self.styleSheet)
        self._window = None
        self.internal = []

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

    def add_item(self,match):
        if match not in self.internal:
            word = WordListItem(match,parent=self)
            self.internal.append(match)
            self.addItem(word)

    def remove_word(self):
        for item in self.selectedItems():
            self.window().driver.undo_changes(item.text())

    def remove_match(self,match):
        self.internal.remove(match)
        for row in range(self.count()):
            item = self.item(row)
            if not item or item.text() == match:
                self.takeItem(row)
            # print(match, self.item(row),row,self.internal)


class MatchesList(QListWidget):
    styleSheet = """QListWidget {
            background-color: white;
            selection-color: #600;
            border: 3px solid #743;
            alternate-background-color: #a83;
            selection-background-color: #8cd;
            font-style: bold;
        }
        QListView::item {
            border: 2px solid black;
        }"""

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setObjectName("Matches_List")
        self.setStyleSheet(self.styleSheet)
        self.doubleClicked.connect(self.match_selected)
        self._window = None

    def match_selected(self):
        match = self.currentItem()
        word = self.window().word_list.currentItem()
        self.window().driver.match_selected(word.text(),match.text())
        self.window().word_list.fill_matches()
        self.window().driver.decrypt()

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

    def add_items(self,items):
        self.clear()
        for item in items:
            self.addItem(item)


class SubmitPhraseButton(QPushButton):
    styleSheet = """
        QPushButton {
            color: #ffe8c6;
            background-color: #283544;
        }
    """

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._window = None
        self.setObjectName("submit_phrase")
        self.setText("Submit Phrase")
        self.setStyleSheet(self.styleSheet)
        self.pressed.connect(self.submit)

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

    def submit(self):
        text = self.window().line_edit.text()
        table = self.window().table.get_contents()
        phrase = Phrase(text,table=table)
        self.window().setPhrase(phrase)
        wordlist = self.window().word_list
        wordlist.add_items(phrase.words)

class RemoveCharButton(QPushButton):
    styleSheet = """
        QPushButton {
            color: #ffe8c6;
            background-color: #283544;
        }
    """

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._window = None
        self.setObjectName("remove_char")
        self.setText("Remove Row")
        self.setStyleSheet(self.styleSheet)
        self.pressed.connect(self.remove)

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

    def remove(self):
        row = self.window().table.currentRow()
        self.window().table.remove_row(row)
        self.window().driver.decrypt()

class RemoveWordButton(QPushButton):
    styleSheet = """
        QPushButton {
            color: #ffe8c6;
            background-color: #283544;
        }
    """

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._window = None
        self.setObjectName("remove_word")
        self.setText("Remove Word")
        self.setStyleSheet(self.styleSheet)
        self.pressed.connect(self.remove_selected)

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

    def remove_selected(self):
        self.window().chosen_list.remove_word()
        self.window().driver.decrypt()

class SolveButton(QPushButton):
    styleSheet = """
        QPushButton {
            color: #ffe8c6;
            background-color: #283544;
        }
    """

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._window = None
        self.setObjectName("solve")
        self.setText("Auto Solve")
        self.setStyleSheet(self.styleSheet)
        self.pressed.connect(self.solve)

    def solve(self):
        table = self.window().table.get_contents()
        self.window().driver.auto_solve(table)

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

class SubmitCharButton(QPushButton):
    styleSheet = """
        QPushButton {
            color: #ffe8c6;
            background-color: #283544;
    }"""

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._window = None
        self.setObjectName("submit_char")
        self.setText("Add Row")
        self.setStyleSheet(self.styleSheet)
        self.pressed.connect(self.submit)

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

    def submit(self):
        old_txt = self.window().old_combo.currentText()
        new_txt = self.window().new_combo.currentText()
        self.window().table.add_chars(old_txt,new_txt)
        self.window().driver.decrypt()

class AutoCheck(QCheckBox):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._window = None
        self.setObjectName("AutoCheck")
        self.setText("Auto")

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

class WordLabel(QLabel):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._window = None
        self.setObjectName("word_label")
        self.setText("Words")
        self.setFont(BoldFont())
        self.setIndent(8)

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

class MatchesLabel(QLabel):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._window = None
        self.setObjectName("matches_label")
        self.setText("Matches")
        self.setFont(BoldFont())
        self.setIndent(8)

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window

class TranslationLabel(QLabel):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._window = None
        self.setObjectName("translation_label")
        self.setText("Character Translation Table")
        self.setFont(BoldFont())
        self.setIndent(8)

    def window(self):
        return self._window

    def setWindow(self,window):
        self._window = window
