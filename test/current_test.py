#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os,sys
from unittest import TestCase
from PyQt6.QtWidgets import QApplication
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.gui import Window
from src.driver import Driver
from src.phrase import Phrase,sanatize


class WindowTest(TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = Window(self.app,parent=None)
        self.driver = Driver(self.app)
        self.window.setDriver(self.driver)
        self.window.show()

    def test_current_problem(self):
        phrase = "LGA KDFSO NSKNWC CAAIC QFMXGLAF KGAY WPR'JA BRCL INOA CPIALGMYX LGNL KNCY'L LGAFA QAHPFA. - YAMS XNMINY"
        chars = ("P","O")
        self.window.line_edit.setText(phrase)
        self.assertEqual(phrase,self.window.line_edit.text())
        self.window.table.add_chars(chars[0],chars[1])
        self.assertTrue(self.window.table.get_contents())
        self.assertIn(chars[0],self.window.table.get_contents())
        self.assertEqual(chars[1],self.window.table.get_contents()[chars[0]])
        self.window.submit_phrase.click()
        self.assertTrue(self.window.phrase)
        self.assertEqual(sanatize(phrase),self.window.phrase.txt)
        p = Phrase(phrase,table={chars[0]:chars[1]})
        rows = self.window.word_list.count()
        map(lambda x: self.assertIn(p.words,x),[self.window.word_list.item(i) for i in range(rows)])
        # self.window.solve_button.click()
        # sys.exit(self.app.exec())


