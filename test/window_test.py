#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os,sys
from unittest import TestCase
from PyQt6.QtWidgets import QApplication
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.gui import Window


class BasicWindowTest(TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)

    def test_window_init(self):
        main = Window(self.app,parent=None)
        self.assertTrue(main)
        main.show()
        self.assertTrue(main.custom_widgets)
        self.assertIsNone(main.phrase)
        self.assertIsNone(main.driver)

