#!/usr/bin/env python3
import os
import json
import sys
from PyQt6.QtWidgets import QApplication
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from src.driver import Driver
from src.gui import Window

PHRASES = json.load(open("data\\phrases.json","rt"))

def main():
    app = QApplication(sys.argv)
    main = Window(app,parent=None)
    driver = Driver()
    main.setDriver(driver)
    main.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


