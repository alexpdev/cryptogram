#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os,sys
from unittest import TestCase
from PyQt6.QtWidgets import QApplication
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.gui import Window
from src.driver import Driver

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

class WindowTest(TestCase):

    def setUp(self):
        self._app = QApplication(sys.argv)
        self.window = Window(self._app,parent=None)

    def test_driver(self):
        driver = Driver(window=self.window)
        self.window.setDriver(driver)
        self.assertEqual(driver,self.window.driver)
        self.window.show()
        widgets = ( self.window.central,
                    self.window.central_layout,
                    self.window.vert_layout_1,
                    self.window.vert_layout_2,
                    self.window.vert_layout_3,
                    self.window.horiz_layout_1,
                    self.window.horiz_layout_2,
                    self.window.grid_layout_2,
                    self.window.line_edit,
                    self.window.table,
                    self.window.submit_phrase,
                    self.window.submit_char,
                    self.window.remove_char,
                    self.window.remove_word,
                    self.window.solve_button,
                    self.window.auto_check,
                    self.window.text_browser,
                    self.window.old_combo,
                    self.window.new_combo,
                    self.window.menubar,
                    self.window.statusbar,
                    self.window.file_menu)
        for widget in widgets:
            if widget:
                print(widget)
            else:
                print("False", widget)
            self.assertTrue(widget)
            if widget in self.window.custom_widgets:
                self.assertEqual(widget.window(),self.window)























