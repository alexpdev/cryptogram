import sys
from .window import Window, Application
from .phrase import PHRASE



def main():
    app = Application(sys.argv)
    window = Window()
    window.show()
    window.phraseinput.setText(PHRASE)
    window.setFocus()
    sys.exit(app.exec())
