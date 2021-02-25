# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerDkVbxS.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(717, 600)
        self.centralwidget = QWidget(MainWindow)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4 = QVBoxLayout()
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_4 = QHBoxLayout()
        self.label = QLabel(self.centralwidget)
        self.label_2 = QLabel(self.centralwidget)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.tableView = QTableView(self.centralwidget)
        self.tableView_2 = QTableView(self.centralwidget)
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.listView = QListView(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.statusbar = QStatusBar(MainWindow)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.tableView_2)
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.listView)
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.menubar.setGeometry(QRect(0, 0, 717, 22))
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setCentralWidget(self.centralwidget)




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(679, 681)
        self.centralwidget = QWidget(MainWindow)
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_3 = QGridLayout()
        self.gridLayout = QGridLayout()
        self.verticalLayout = QVBoxLayout()
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.label = QLabel(self.centralwidget)
        self.label_2 = QLabel(self.centralwidget)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget_2 = QListWidget(self.centralwidget)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 2, 2, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 3)
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.listWidget, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.listWidget_2, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 2)
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.listWidget_3 = QListWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.listWidget_3)
        self.verticalLayout.addWidget(self.pushButton_5)
        self.gridLayout_4.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.gridLayout_4.addWidget(self.textBrowser, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 679, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
