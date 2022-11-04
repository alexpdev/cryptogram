import os
import numpy as np
import sys
import pytesseract
from PIL import Image
import cv2 as cv
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

sys.path.insert(0,"C:/usr/bin/Tesseract-OCR")

class Puzzle:
    def __init__(self, arr=None, path=None):
        self.arr = arr
        self.path = path
        self._key = None
        self.rows = []
        self.current = 1
        self.lines = []

    @property
    def height(self):
        return self.image.height

    @property
    def width(self):
        return self.image.width

    def __str__(self):
        return str(self.rows) + str(self.lines)


class Window(QMainWindow):
    """Window object."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.layout = QVBoxLayout()
        self.central = QWidget(parent=self)
        self.central.setLayout(self.layout)
        self.setCentralWidget(self.central)
        self.setObjectName('MainWindow')
        self.button = QPushButton("See Image", self)
        self.calc_button = QPushButton("Calculate", self)
        self.convert_button = QPushButton("convert", self)
        self.resize(500,500)
        self.scrollarea = QScrollArea()
        self.scrollarea.setBackgroundRole(QPalette.Dark)
        self.scrollwidget = QWidget()
        self.slayout = QVBoxLayout()
        self.scrollwidget.setLayout(self.slayout)
        self.label = QLabel()
        self.slayout.addWidget(self.label)
        self.shlayout = QHBoxLayout()
        self.slayout.addLayout(self.shlayout)
        self.hlayout = QHBoxLayout()
        self.scrollarea.setWidget(self.scrollwidget)
        self.scrollarea.setWidgetResizable(True)
        self.layout.addLayout(self.hlayout)
        self.hlayout.addWidget(self.button)
        self.hlayout.addWidget(self.convert_button)
        self.hlayout.addWidget(self.calc_button)
        self.layout.addWidget(self.scrollarea)
        parent = os.path.dirname(__file__)
        self.imgs = [os.path.join(parent, "imgs", i) for i in os.listdir("imgs")]
        self.current = 0
        self.puzzle = None
        self.button.clicked.connect(self.showImage)
        self.convert_button.clicked.connect(self.convert)
        self.calc_button.clicked.connect(self.calculate)
        self.chars_layout = self.shlayout
        self.chars = []
        self.all_chars = []

    def convert_to_pixmap(self, arr):
        image = Image.fromarray(arr)
        im = image.convert("RGBA")
        data = im.tobytes("raw", "RGBA")
        qim = QImage(data, im.size[0], im.size[1], QImage.Format_RGBA8888)
        return QPixmap.fromImage(qim)

    def showImage(self):
        path = self.imgs[self.current]
        image = cv.imread(path)
        arr = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        puzzle = Puzzle(path=path, arr=arr)
        self.puzzle = puzzle
        self.calculate()
        img = self.convert_to_pixmap(puzzle.arr)
        self.label.setPixmap(img.scaledToWidth(800))
        self.label.show()
        self.scrollarea.show()
        self.current += 1


    def gen_labels(self, arr):
        label =  QLabel()
        image = Image.fromarray(arr)
        im = image.convert("RGBA")
        data = im.tobytes()
        qim = QImage(data, im.size[0], im.size[1], QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qim)
        label.setPixmap(pixmap)
        if len(self.chars) < 6:
            self.chars_layout.addWidget(label)
            self.chars.append(label)
        else:
            self.all_chars.append(self.chars)
            self.chars = []
            self.chars_layout = QHBoxLayout()
            self.chars_layout.addWidget(label)
            self.chars.append(label)
            self.slayout.addLayout(self.chars_layout)
        label.show()

    def calculate(self):
        arr = self.puzzle.arr
        mask = arr < 150
        arr[mask] = 0
        mask = arr > 150
        arr[mask] = 255
        rows = []
        last = start = 0
        for i in range(len(arr)):
            if np.sum(arr[i]) != 255*len(arr[i]):
                if last == 0:
                    last = start = i
                elif start + 1 != i:
                    rows.append((last, start))
                    last = start = i
                else:
                    start = i
        rows.append((last, start))
        self.puzzle.rows = rows
        sizes = [start - last for last,start in rows]
        shortest = min(sizes)
        largest = max(sizes)
        areas = {}
        for last, start in rows:
            if start - last == shortest:
                section = arr[last]
                indeces = np.where(section == 0)[0]
                t = []
                l = f = indeces[0]
                for index in indeces[1:]:
                    if index == f + 1:
                        f = index
                    else:
                        t.append((l,f))
                        l = f = index
                t.append((l,f))
                areas[(last, start)] = t
        word_counter = []
        gap = largest // 2
        for key, value in areas.items():
            char_counter = []
            x1, x2 = key
            gaps = [value[i][0] - value[i-1][1] for i in range(1, len(value))]
            min_gap = min(gaps)
            count, apostrophe = 1, False
            for i in range(1, len(value)):
                y1, y2 = value[i-1]
                y3, y4 = value[i]
                char1 = arr[x2+10:x2+gap,y1:y2]
                char2 = arr[x2+10:x2+gap,y3:y4]
                self.gen_labels(char1)
                # arr[x2+10:x2+gap,y1:y2] = 0
                # arr[x2+10:x2+gap,y3:y4] = 0
                if y3-y2 == min_gap:
                    count += 1
                elif y3 - y2 > min_gap:
                    upper = arr[x1-gap:x1-1, y2+1:y3-1]
                    lower = arr[x2+1:x2+gap, y2+1:y3-1]
                    if np.sum(upper) != 255 * upper.size:
                        if np.sum(lower) == 255 * lower.size:
                            apostrophe = True
                        # arr[x2+1:x2+gap, y2+1:y3-1] = 0
                        self.gen_labels(arr[x2+1:x2+gap, y2+1:y3-1])
                        count += 2
                    else:
                        char_counter.append((count,apostrophe))
                        count = 1
                        apostrophe = False
            self.gen_labels(char2)
            char_counter.append((count, apostrophe))
            word_counter.append(char_counter)
            self.puzzle.word_counter = word_counter

    def convert(self):
        index = self.puzzle.current
        print(self.puzzle)
        self.puzzle.current += 1
        x,y = self.puzzle.rows[index]
        start = x - 5
        end = y + 5
        arr = self.puzzle.arr[start:end]
        img = self.convert_to_pixmap(arr)
        self.label.setPixmap(img.scaledToWidth(500))
        image = Image.fromarray(arr)
        txt = pytesseract.image_to_string(image, lang="eng", config='-l eng --oem 1 --psm 6  -c preserve_interword_spaces=1 -c tessedit_char_whitelist="0123456789- "')
        self.puzzle.lines.append(txt)
        print(txt)

app = QApplication([])
window = Window()
window.show()
app.exec()
