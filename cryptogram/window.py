import os
import sys
import json
import string

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

SRCDIR = os.path.dirname(os.path.abspath(__file__))
DATADIR = os.path.join(os.path.dirname(SRCDIR), "data")
ALLWORDS = json.load(open(os.path.join(DATADIR, "allWords.json"),"rt"))

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.mapping = {}
        self.rev = {}
        self.central = QWidget(parent=self)
        self.layout = QVBoxLayout()
        self.central.setLayout(self.layout)
        self.setCentralWidget(self.central)
        self.phraseinput = QLineEdit(parent=self)
        self.hlayout1 = QHBoxLayout()
        self.hlayout2 = QHBoxLayout()
        self.hlayout3 = QHBoxLayout()
        self.vlayout1 = QVBoxLayout()
        self.vlayout2 = QVBoxLayout()
        self.vlayout3 = QVBoxLayout()
        self.vlayout4 = QVBoxLayout()
        self.phraselabel = QLabel(parent=self)
        self.phraselabel.setText("Phrase")
        self.hlayout1.addWidget(self.phraselabel)
        self.hlayout1.addWidget(self.phraseinput)
        self.listwidget = QListWidget(parent=self)
        self.list2widget = QListWidget(parent=self)
        self.button = QPushButton(parent=self)
        self.button.setText("Submit")
        self.button2 = QPushButton(parent=self)
        self.button2.setText("Select")
        self.button3 = QPushButton(parent=self)
        self.button3.setText("Unselect")
        self.button4 = QPushButton(parent=self)
        self.button4.setText("Select")
        self.button.pressed.connect(self.solve)
        self.button2.pressed.connect(self.findmatch)
        self.button3.pressed.connect(self.unselect)
        self.button4.pressed.connect(self.setChosen)
        self.vlayout2.addWidget(self.list2widget)
        self.vlayout2.addWidget(self.button4)
        self.vlayout1.addWidget(self.listwidget)
        self.vlayout1.addWidget(self.button2)
        self.vlayout1.addWidget(self.button3)
        self.hlayout2.addLayout(self.vlayout1)
        self.hlayout2.addLayout(self.vlayout2)
        self.hlayout3.addWidget(self.button)
        self.layout.addLayout(self.hlayout1)
        self.layout.addLayout(self.hlayout2)
        self.layout.addLayout(self.hlayout3)
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
        print(self.mapping, self.rev)

    def findmatch(self):
        item = self.listwidget.currentItem()
        print(item)


    def solve(self):
        inp = self.phraseinput.text()
        strwords = inp.split(" ")
        phrase = []
        numword = []
        for word in strwords:
            nums = word.split(",")
            for num in nums:
                if num.isnumeric():
                    numword.append(int(num))
                else:
                    numword.append(num)
            phrase.append(numword)
            numword = []
        for numword in phrase:
            n = ListItem(self.listwidget,0)
            n.setText(str(numword))
            n.setWord(numword)
            self.listwidget.addItem(n)



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

class ListItem(QListWidgetItem):
    def __init__(self, parent=None, tpe=0):
        super().__init__(parent, tpe)
        self.word = None

    def setWord(self, other):
        self.word = other


class Application(QApplication):
    def __init__(self, args):
        super().__init__(args)
        pass
