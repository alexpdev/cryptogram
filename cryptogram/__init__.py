import sys
from .window import Application, Window

def main():
    app = Application(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
