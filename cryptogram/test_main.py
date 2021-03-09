#! /usr/bin/python3
#-*- coding: utf-8 -*-

import os
import sys
from PyQt6.QtWidgets import QApplication
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from cryptogram.driver import Driver
from cryptogram.gui import Window

def main2():
        app = QApplication(sys.argv)
        window = Window(app,parent=None)
        driver = Driver(window)
        window.setDriver(driver)
        window.show()
        phrase = "YT JXX RDYGHLDU CLDL VLHLDWYGLV GNH HN RDYGH JGAHBYGZ HYXX HBLA CLDL UQDL YH CNQXV NTTLGV GNENVA HBLDL CNQXV EL SLDA XYHHXL RDYGHLV. - ELGKJWYG TDJGFXYG"
        chars = ("A","Y")
        window.line_edit.setText(phrase)
        window.table.add_chars(chars[0],chars[1])
        window.submit_phrase.click()
        sys.exit(app.exec())
