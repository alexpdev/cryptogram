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

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import numpy as np
import cv2 as cv
from PIL import Image
import pytesseract

SRCDIR = os.path.dirname(os.path.abspath(__file__))
DATADIR = os.path.join(os.path.dirname(SRCDIR), "data")
ALLWORDS = json.load(open(os.path.join(DATADIR, "allWords.json"),"rt"))


class CryptoImg(QThread):
    phrase_start = Signal()
    next_word = Signal(list)
    phrase_end = Signal()


    def __init__(self, path=None, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.path = path
        self.word = []
        self.img = cv.imread(path)

    def convert_image(self):
        gscale = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        _, threshold = cv.threshold(gscale, 150, 255, cv.THRESH_BINARY)
        return threshold

    def show_image(self, arr=None):
        if not arr:
            arr = self.img
        label = QLabel()
        image = Image.fromarray(arr)
        im = image.convert("RGBA").reduce(5)
        data = im.tobytes()
        qim = QImage(data, im.size[0], im.size[1], QImage.Format_RGBA8888)
        label.setPixmap(QPixmap.fromImage(qim))
        self.parent.scrolllayout.addWidget(label)
        label.show()
        QApplication.instance().processEvents()

    def get_contours(self, arr):
        contours, _ = cv.findContours(
            arr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE
        )
        upper, under, left, right = -5, 5, -3, 80
        sizes = {}
        for contour in contours:
            y, x = contour[0][0]
            sub = arr[x + upper : x + under, y + left : y + right]
            zed = np.where(sub==0)
            l = len(set(zed[0]))
            if l <= 5 and len(zed[1]) > 2:
                pxls = sorted(set(zed[1]))
                last = i = pxls[0]
                for j in pxls[1:]:
                    if j != i + 1:
                        break
                    i = j
                sizes.setdefault((l,i - last), [])
                sizes[(l,i-last)].append([x-l,x+l,y-2,y+i-last+2])
        _, rows = max(list(sizes.items()), key=lambda x: len(x[1]))
        grid = {}
        for row in rows:
            for g in grid:
                if abs(row[0] - g) <= 2:
                    grid[g].append(row)
                    break
            else:
                grid[row[0]] = [row]
        gap_list = sorted(list(grid.keys()))
        gap = max(
            [gap_list[k] - gap_list[k-1] for k in range(1,len(gap_list))]
        )
        rows = [sorted(v, key=lambda x: x[2]) for k,v in sorted(grid.items())]
        return gap, rows

    def run(self):
        self.phrase_start.emit()
        arr = self.convert_image()
        gap, rows = self.get_contours(arr)
        self.word_lengths(gap, rows)
        self.phrase_end.emit()

    def word_lengths(self, gap, rows):
        gap = gap // 2
        for row in rows:
            gaps = [row[i][2] - row[i-1][3] for i in range(1,len(row))]
            min_gap = min(gaps)
            for i in range(1, len(row)):
                _, x2, y1, y2 = row[i-1]
                _, _, y3, y4 = row[i]
                char1 = self.img[x2+10:x2+gap,y1:y2]
                char2 = self.img[x2+10:x2+gap,y3:y4]
                self.process_img(char1)
                if y3 - y2 > min_gap:
                    # upper = self.arr[x1 - gap: x1 - 1, y2 + 1: y3 - 1]
                    lower = self.img[x2 + 1: x2 + gap, y2 + 1: y3 - 1]
                    self.process_img(lower)
            self.process_img(char2)
            self.next_word.emit(self.word)
            self.word = []
        self.next_word.emit(self.word)

    def process_img(self, arr):
        img = Image.fromarray(arr)
        txt = pytesseract.image_to_string(img, lang="eng", config='-l eng --oem 1 --psm 6  -c preserve_interword_spaces=1 -c tessedit_char_whitelist="0123456789- "')
        txt = txt.strip()
        if not txt:
            self.next_word.emit(self.word)
            self.word = []
        elif txt.isdigit():
            self.word.append(txt)


class CryptoGram(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.window = parent.window
        self.mapping = {}
        self.rev = {}
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.phraseinput = QPushButton("Enter Phrase Text",parent=self)
        self.phraseimage = QPushButton("Select Phrase Image",parent=self)
        self.listwidget = QListWidget(parent=self)
        self.list2widget = QListWidget(parent=self)
        self.button3 = QPushButton("Clear", parent=self)
        self.button4 = QPushButton("Select", parent=self)
        self.resultlabel = Label("Result", self)
        self.resultedit1 = QTextBrowser(parent=self)
        self.resultedit1.setFontPointSize(16.0)
        self.resultedit1.setAlignment(Qt.AlignCenter)
        self.scrollarea = QScrollArea()
        self.scrollwidget = QWidget()
        self.scrolllayout = QVBoxLayout(self.scrollwidget)
        self.scrollarea.setWidget(self.scrollwidget)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setBackgroundRole(QPalette.Dark)
        self.hlayout1 = QHBoxLayout()
        self.hlayout2 = QHBoxLayout()
        self.hlayout3 = QHBoxLayout()
        self.vlayout1 = QVBoxLayout()
        self.vlayout2 = QVBoxLayout()
        self.vlayout3 = QVBoxLayout()
        self.vlayout4 = QVBoxLayout()
        self.hlayout1.addWidget(self.phraseimage)
        self.hlayout1.addWidget(self.phraseinput)
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
        self.splitter = QHBoxLayout()
        self.editframe = QFrame()
        self.editframe.setLayout(self.vlayout3)
        self.splitter.addWidget(self.editframe)
        self.splitter.addWidget(self.scrollarea)
        self.layout.addLayout(self.splitter)
        self.phraseimage.pressed.connect(self.select_phrase_file)
        self.phraseinput.pressed.connect(self.input_phrase)
        self.button3.pressed.connect(self.unselect)
        self.button4.pressed.connect(self.setChosen)
        self.listwidget.currentItemChanged.connect(self.switchcurrent)

    def input_phrase(self):
        self.dialog = InputDialog(self)
        self.dialog.inputAccepted.connect(self.solve)
        self.dialog.exec()

    def add_word_to_resultedit(self, word):
        inp = " ".join(word)
        if inp:
            self.solve(inp)

    def show_completed_message(self):
        self.window.statusbar.showMessage("Complete", 100000)

    def clear_widgets(self):
        self.resultedit1.clear()
        self.list2widget.clear()
        self.listwidget.clear()

    def select_phrase_file(self):
        path = QFileDialog.getOpenFileName(parent=self, caption="Image File")
        if path:
            path = path[0]
            self.cryptoimg = CryptoImg(path, self)
            self.cryptoimg.show_image()
            self.cryptoimg.phrase_start.connect(self.clear_widgets)
            self.cryptoimg.next_word.connect(self.add_word_to_resultedit)
            self.cryptoimg.phrase_end.connect(self.show_completed_message)
            self.cryptoimg.finished.connect(self.cryptoimg.deleteLater)
            self.cryptoimg.start()
        else:
            self.window.statusbar.showMessage("didnt work", 100000)

    def switchcurrent(self):
        self.list2widget.clear()
        item = self.listwidget.currentItem()
        word = item.word
        serword = serialize(word)
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
                        listitem = QListWidgetItem(type=0)
                        listitem.setText(string)
                        self.list2widget.addItem(listitem)

    def setChosen(self):
        item1 = self.listwidget.currentItem()
        item2 = self.list2widget.currentItem()
        if not item1 or not item2:
            return
        nums = item1.word
        string = item2.text()
        for x,y in zip(nums, string):
            if x == "'":
                self.mapping["'"] = "'"
                self.rev["'"] = "'"
            else:
                self.mapping[x] = y
                self.rev[y] = x
        self.reresult()

    def unselect(self):
        item = self.listwidget.currentItem()
        data = item.word
        chars = []
        for i in data:
            if i in self.mapping:
                chars.append(self.mapping[i])
                del self.mapping[i]
        for char in chars:
            if char in self.rev:
                del self.rev[char]
        self.reresult()

    def solve(self, inp):
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
        self.reresult()

    def reresult(self):
        self.resultedit1.clear()
        string = ""
        count = self.listwidget.count()
        for i in range(count):
            item = self.listwidget.item(i)
            word = item.word
            for char in word:
                if char in self.mapping:
                    string += self.mapping[char]
                else:
                    string += "_"
            string += "  "
            if count // 5 and i and not (i%count//5):
                string += "\n"
        self.resultedit1.setText(string)
        self.resultedit1.selectAll()
        self.resultedit1.setAlignment(Qt.AlignCenter)




class Window(QMainWindow):
    """The Main Window Widget for daily challenge puzzle solvers."""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QVBoxLayout()
        self.central = TabWidget(parent=self)
        self.resize(800,700)
        self.central.setLayout(self.layout)
        self.statusbar = self.statusBar()
        self.setStatusBar(self.statusbar)
        self.setCentralWidget(self.central)
        self.setWindowTitle("Daily Challenge Puzzle Solver")
        icon = QIcon("./assets/puzzle.png")
        self.setWindowIcon(icon)



class TabWidget(QTabWidget):
    """Tab widget keeps track of which solving tool to use."""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.window = parent
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
        word = partial[0]
        chars = [i for i in partial[1:] if i.isalpha() or i == "'"]
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

class InputDialog(QDialog):
    """Line edit widget for input phrase."""

    inputAccepted = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.editor = QPlainTextEdit(parent=self)
        self.layout = QVBoxLayout(self)
        self.hlayout = QHBoxLayout()
        self.layout.addWidget(self.editor)
        self.acceptbtn = QPushButton("Accept", parent=self)
        self.cancelbtn = QPushButton("Cancel", parent=self)
        self.hlayout.addWidget(self.acceptbtn)
        self.hlayout.addWidget(self.cancelbtn)
        self.layout.addLayout(self.hlayout)
        self.acceptbtn.clicked.connect(self.accept_input)
        self.cancelbtn.clicked.connect(self.close)

    def accept_input(self):
        text = self.editor.toPlainText()
        self.inputAccepted.emit(text)
        self.close()


class Label(QLabel):
    """Label identifying the results so far."""

    ssheet = """QLabel {color: #000;}"""

    def __init__(self, text, parent=None):
        super().__init__(text,parent)
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
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
