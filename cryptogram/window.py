import os
import json

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
