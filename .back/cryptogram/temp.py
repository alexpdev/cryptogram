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

        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton.setObjectName(u"pushButton")
        self.lineEdit.setObjectName(u"lineEdit")
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label.setObjectName(u"label")
        self.tableView_2.setObjectName(u"tableView_2")
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2.setObjectName(u"label_2")
        self.listView.setObjectName(u"listView")
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView.setObjectName(u"tableView")
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.textBrowser.setObjectName(u"textBrowser")
        self.menubar.setObjectName(u"menubar")
        self.statusbar.setObjectName(u"statusbar")




        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi
