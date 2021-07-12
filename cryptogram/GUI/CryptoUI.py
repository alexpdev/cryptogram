import sys
import os
import json
from PyQt6.QtWidgets import (QWidget,QGridLayout,QLabel,QComboBox,
                             QPushButton,QCheckBox,QLineEdit,
                             QMainWindow,QApplication,QTextBrowser,
                             )

class CryptUI(QMainWindow):
    def __init__(self):
        super().__init__()
        centralWidget = QWidget()
        self.resize(600,100)
        label1 = QLabel("Text Browser")
        self.combo = QComboBox()
        label2 = QLabel("Encrypted Text")
        # checkLabel = QLabel("CheckBox")
        # self.box = QCheckBox()
        # self.box.setChecked(True)
        self.linedit = QLineEdit()
        grid = QGridLayout()
        self.browser = QTextBrowser()
        btn = QPushButton("&Click Me")
        btn.clicked.connect(self.sendBrowser)
        centralWidget.setLayout(grid)
        grid.addWidget(label1,3,0)
        grid.addWidget(label2,0,0)
        grid.addWidget(btn,2,0)
        grid.addWidget(self.combo,5,0)
        # grid.addWidget(self.box,3,1)
        # grid.addWidget(checkLabel,3,0)
        grid.addWidget(self.linedit,1,0)
        grid.addWidget(self.browser,4,0)
        grid.setSpacing(4)
        self.setCentralWidget(centralWidget)
        self.setWindowTitle("Window Title")


    def sendBrowser(self,event):
        path = self.linedit.text()
        js = json.load(open(path))
        s = ""
        for k,v in js.items():
            s += f"( {k} : {v} )\n"
        self.browser.setText(s)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CryptUI()
    window.show()
    sys.exit(app.exec_())
