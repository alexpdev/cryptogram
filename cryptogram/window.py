#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""GUI toolset for solving logic challenges and puzzles.

Includes:
    Cryptogram Solver
    Anogram Solver
    Word Permutations
"""


import os
import json

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

SRCDIR = os.path.dirname(os.path.abspath(__file__))
DATADIR = os.path.join(os.path.dirname(SRCDIR), "data")
ALLWORDS = json.load(open(os.path.join(DATADIR, "allWords.json"),"rt"))

class CryptoGram(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.window = parent.window
        self.mapping = {}
        self.rev = {}
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.phraselabel = Label("Phrase", parent=self)
        self.phraseinput = InputEdit(parent=self)
        self.button = QPushButton("Submit", parent=self)
        self.listwidget = QListWidget(parent=self)
        self.list2widget = QListWidget(parent=self)
        self.button3 = QPushButton("Clear", parent=self)
        self.button4 = QPushButton("Select", parent=self)
        self.resultlabel = Label("Result", self)
        self.resultedit1 = LineEdit(parent=self)
        self.hlayout1 = QHBoxLayout()
        self.hlayout2 = QHBoxLayout()
        self.hlayout3 = QHBoxLayout()
        self.vlayout1 = QVBoxLayout()
        self.vlayout2 = QVBoxLayout()
        self.vlayout3 = QVBoxLayout()
        self.vlayout4 = QVBoxLayout()
        self.hlayout1.addWidget(self.phraselabel)
        self.hlayout1.addWidget(self.phraseinput)
        self.hlayout1.addWidget(self.button)
        self.vlayout3.addWidget(self.resultlabel)
        self.vlayout3.addWidget(self.resultedit1)
        self.vlayout2.addWidget(self.list2widget)
        self.vlayout2.addWidget(self.button4)
        self.vlayout1.addWidget(self.listwidget)
        self.vlayout1.addWidget(self.button3)
        self.hlayout2.addLayout(self.vlayout1)
        self.hlayout2.addLayout(self.vlayout2)
        self.layout.addLayout(self.hlayout1)
        self.layout.addLayout(self.hlayout2)
        self.layout.addLayout(self.hlayout3)
        self.layout.addLayout(self.vlayout3)
        self.button.pressed.connect(self.solve)
        self.button3.pressed.connect(self.unselect)
        self.button4.pressed.connect(self.setChosen)
        self.listwidget.currentItemChanged.connect(self.switchcurrent)

    def switchcurrent(self):
        self.list2widget.clear()
        item = self.listwidget.currentItem()
        word = item.word
        serword = serialize(word)
        print(word, type(word))
        for string in ALLWORDS:
            if len(string) == len(word):
                if serialize(string) == serword:
                    matches = True
                    for x,y in zip(word, string):
                        if x in self.mapping and self.mapping[x] != y:
                            matches = False
                            break
                        if y in self.rev and self.rev[y] != x:
                            matches = False
                            break
                    if matches:
                        listitem = QListWidgetItem(parent=self.list2widget)
                        listitem.setText(string)
                        self.list2widget.addItem(listitem)

    def setChosen(self):
        print("setting chosen")
        item1 = self.listwidget.currentItem()
        item2 = self.list2widget.currentItem()
        if not item1 or not item2:
            return
        nums = item1.word
        string = item2.text()
        print(nums, string)
        print(self.mapping, self.rev)
        for x,y in zip(nums, string):
            if x == "'":
                self.mapping["'"] = "'"
                self.rev["'"] = "'"
            else:
                self.mapping[x] = y
                self.rev[y] = x
        self.reresult()
        print(self.mapping, self.rev)

    def unselect(self):
        print("unselecting")
        item = self.listwidget.currentItem()
        data = item.word
        chars = []
        print(self.mapping, self.rev)
        for i in data:
            if i in self.mapping:
                chars.append(self.mapping[i])
                del self.mapping[i]
        for char in chars:
            if char in self.rev:
                del self.rev[char]
        self.reresult()
        print(self.mapping, self.rev)

    def solve(self):
        inp = self.phraseinput.text()
        if inp[0].isalpha():
            words = inp.split(" ")
        elif inp[0].isdigit():
            split1, split2 = "  ", " "
            if inp.count(",") > 5:
                split1, split2 = " ", ","
            groups = inp.split(split1)
            words = []
            for group in groups:
                nums = [int(i) if i.isnumeric() else i for i in group.split(split2)]
                words.append(nums)
        for word in words:
            n = ListItem(self.listwidget,0)
            n.setText(str(word))
            n.setWord(word)
            self.listwidget.addItem(n)
        self.reresult

    def reresult(self):
        self.resultedit1.clear()
        string = ""
        for i in range(self.listwidget.count()):
            item = self.listwidget.item(i)
            word = item.word
            for char in word:
                if char in self.mapping:
                    string += self.mapping[char]
                else:
                    string += "_"
            string += "  "
        self.resultedit1.setText(string)


class Window(QMainWindow):
    """The Main Window Widget for daily challenge puzzle solvers."""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QVBoxLayout()
        self.central = TabWidget(parent=self)
        self.central.setLayout(self.layout)
        self.setCentralWidget(self.central)
        self.setWindowTitle("Daily Challenge Puzzle Solver")
        icon = QIcon("./assets/puzzle.png")
        self.setWindowIcon(icon)



class TabWidget(QTabWidget):
    """Tab widget keeps track of which solving tool to use."""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.window = parent.window
        self.tab1 = CryptoGram(parent=self)
        self.tab2 = Anonagram(parent=self)
        self.tab3 = Permutations(parent=self)
        self.addTab(self.tab1, "CryptoGram")
        self.addTab(self.tab2, "AnonaGram")
        self.addTab(self.tab3, "Permutations")


class Permutations(QWidget):
    """Permute word for when the anagram solver doesn't find a match."""

    def __init__(self, parent=None):
        """Construct permutation generator tab for daily challenges."""
        super().__init__(parent=parent)
        self.window = parent.window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.hlayout1 = QHBoxLayout()
        self.perm_label = QLabel("Letters",parent=self)
        self.perm_line_edit = QLineEdit(parent=self)
        self.perm_btn1 = QPushButton("Submit",parent=self)
        self.perm_btn1.pressed.connect(self.solve)
        self.hlayout1.addWidget(self.perm_label)
        self.hlayout1.addWidget(self.perm_line_edit)
        self.hlayout1.addWidget(self.perm_btn1)
        self.layout.addLayout(self.hlayout1)
        self.grid = QGridLayout()
        self.layout.addLayout(self.grid)

    def add_label(self, label):
        self.grid.addWidget(label, self.row, self.col, 1, 1)
        if self.col + 1 == self.limit:
            self.col = 0
            self.row += 1
        else:
            self.col += 1
        self.repaint()

    def solve(self):
        partial = self.perm_line_edit.text().upper()
        print(partial)
        word = partial[0]
        print(word)
        chars = [i for i in partial[1:] if i.isalpha() or i == "'"]
        print(chars)
        self.row = 0
        self.limit = 12
        self.col = 0
        self.permute(chars, word)

    def permute(self, chars, word):
        if chars:
            for i in range(len(chars)):
                char = chars[i]
                del chars[i]
                self.permute(chars, word + char)
                chars.insert(i,char)
        else:
            label = QLabel(word)
            self.add_label(label)


class Anonagram(QWidget):
    """Anagram Puzzle Daily Challenge."""

    def __init__(self, parent=None):
        """Construct the Anagram tab widget."""
        super().__init__(parent=parent)
        self.window = parent.window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.grid1 = QGridLayout()
        self.grid2 = QGridLayout()
        self.line1 = QLineEdit(parent=self)
        self.line2 = QLineEdit(parent=self)
        self.line3 = QLineEdit(parent=self)
        self.line4 = QLineEdit(parent=self)
        self.line5 = QLineEdit(parent=self)
        self.line6 = QLineEdit(parent=self)
        self.box1 = QComboBox(parent=self)
        self.box2 = QComboBox(parent=self)
        self.box3 = QComboBox(parent=self)
        self.box4 = QComboBox(parent=self)
        self.box5 = QComboBox(parent=self)
        self.box6 = QComboBox(parent=self)
        self.btn = QPushButton("Solve", parent=None)
        self.grid1.addWidget(self.line1, 0, 0, 1, 1)
        self.grid1.addWidget(self.line2, 0, 1, 1, 1)
        self.grid1.addWidget(self.box1, 1, 0, 1, 1)
        self.grid1.addWidget(self.box2, 1, 1, 1, 1)
        self.grid1.addWidget(self.line3, 2, 0, 1, 1)
        self.grid1.addWidget(self.line4, 2, 1, 1, 1)
        self.grid1.addWidget(self.box3, 3, 0, 1, 1)
        self.grid1.addWidget(self.box4, 3, 1, 1, 1)
        self.grid1.addWidget(self.line5, 4, 0, 1, 1)
        self.grid1.addWidget(self.line6, 4, 1, 1, 1)
        self.grid1.addWidget(self.box5, 5, 0, 1, 1)
        self.grid1.addWidget(self.box6, 5, 1, 1, 1)
        self.layout.addLayout(self.grid1)
        self.layout.addWidget(self.btn)
        self.btn.clicked.connect(self.solve)

    def solve(self):
        """Provide options for each of the input anagrams."""
        lines = [self.line1, self.line2, self.line3,
                 self.line4, self.line5, self.line6]
        boxes = [self.box1, self.box2, self.box3,
                 self.box4, self.box5, self.box6]
        for i, line in enumerate(lines):
            text = [i.upper() for i in line.text() if i.isalpha() or i == "'"]
            first = text[0]
            for word in ALLWORDS:
                if len(word) >= len(text) + 1 and word[0] == first:
                    for char in word:
                        if char in text:
                            text.remove(char)
                    if not text:
                        boxes[i].addItem(word, 0)


class ListItem(QListWidgetItem):
    """Child Items for QListWidget."""
    def __init__(self, parent=None, tpe=0):
        super().__init__(parent, tpe)
        self.word = None

    def setWord(self, other):
        self.word = other


class Application(QApplication):
    """The Application Event Loop."""
    def __init__(self, args):
        super().__init__(args)
        pass

class InputEdit(QLineEdit):
    """Line edit widget for input phrase."""

    ssheet = """QLineEdit {color: black;}"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        font = self.font()
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet(self.ssheet)


class Label(QLabel):
    """Label identifying the results so far."""

    ssheet = """QLabel {color: #000;}"""

    def __init__(self, text, parent=None):
        super().__init__(text,parent)
        self.setAlignment(Qt.Alignment.AlignCenter)
        self.setStyleSheet(self.ssheet)
        font = self.font()
        font.setBold(True)
        font.setPointSize(10)
        self.setFont(font)


class LineEdit(QLineEdit):
    """Line edit widget for displaying results."""

    ssheet = """QLineEdit {
        background-color: #eee;
        color: #000;
        border: 1px solid #eeeeee;
        border-bottom-color: #000;
    }"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setDisabled(True)
        self.setStyleSheet(self.ssheet)


def serialize(word):
    data = []
    mapping = {}
    current = 0
    for char in word:
        if char == "'":
            data.append("'")
        elif char in mapping:
            data.append(mapping[char])
        else:
            data.append(current)
            current += 1
            mapping[char] = current
    return data
