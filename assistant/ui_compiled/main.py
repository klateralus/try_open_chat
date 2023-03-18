# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AIAssistantWindow(object):
    def setupUi(self, AIAssistantWindow):
        if not AIAssistantWindow.objectName():
            AIAssistantWindow.setObjectName(u"AIAssistantWindow")
        AIAssistantWindow.resize(649, 452)
        AIAssistantWindow.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.actionPreferences = QAction(AIAssistantWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionHow_to_make_API_key = QAction(AIAssistantWindow)
        self.actionHow_to_make_API_key.setObjectName(u"actionHow_to_make_API_key")
        self.actionMake_new_API_key = QAction(AIAssistantWindow)
        self.actionMake_new_API_key.setObjectName(u"actionMake_new_API_key")
        self.centralwidget = QWidget(AIAssistantWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelModelName = QLabel(self.centralwidget)
        self.labelModelName.setObjectName(u"labelModelName")
        self.labelModelName.setStyleSheet(u"font: 13pt \"Segoe UI\";")
        self.labelModelName.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelModelName)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.labelCreativity = QLabel(self.centralwidget)
        self.labelCreativity.setObjectName(u"labelCreativity")
        self.labelCreativity.setStyleSheet(u"font: 13pt \"Segoe UI\";")
        self.labelCreativity.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelCreativity)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.labelTalkativeness = QLabel(self.centralwidget)
        self.labelTalkativeness.setObjectName(u"labelTalkativeness")
        self.labelTalkativeness.setStyleSheet(u"font: 13pt \"Segoe UI\";")
        self.labelTalkativeness.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelTalkativeness)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollAreaMessages = QScrollArea(self.centralwidget)
        self.scrollAreaMessages.setObjectName(u"scrollAreaMessages")
        self.scrollAreaMessages.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollAreaMessages.setWidgetResizable(True)
        self.scrollAreaMessagesWidgetContents = QWidget()
        self.scrollAreaMessagesWidgetContents.setObjectName(u"scrollAreaMessagesWidgetContents")
        self.scrollAreaMessagesWidgetContents.setGeometry(QRect(0, 0, 612, 176))
        self.verticalLayoutMessages = QVBoxLayout(self.scrollAreaMessagesWidgetContents)
        self.verticalLayoutMessages.setObjectName(u"verticalLayoutMessages")
        self.verticalLayoutMessages.setContentsMargins(2, 2, 2, 2)
        self.scrollAreaMessages.setWidget(self.scrollAreaMessagesWidgetContents)

        self.verticalLayout.addWidget(self.scrollAreaMessages)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.requestEdit = QTextEdit(self.centralwidget)
        self.requestEdit.setObjectName(u"requestEdit")
        self.requestEdit.setMaximumSize(QSize(16777215, 96))
        self.requestEdit.setAcceptDrops(False)
        self.requestEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_2.addWidget(self.requestEdit)

        self.pushButtonSend = QPushButton(self.centralwidget)
        self.pushButtonSend.setObjectName(u"pushButtonSend")
        self.pushButtonSend.setMaximumSize(QSize(16777215, 24))
        self.pushButtonSend.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.pushButtonSend)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        AIAssistantWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AIAssistantWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 649, 21))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        AIAssistantWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AIAssistantWindow)
        self.statusbar.setObjectName(u"statusbar")
        AIAssistantWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSettings.addAction(self.actionPreferences)
        self.menuSettings.addAction(self.actionMake_new_API_key)
        self.menuHelp.addAction(self.actionHow_to_make_API_key)

        self.retranslateUi(AIAssistantWindow)

        QMetaObject.connectSlotsByName(AIAssistantWindow)
    # setupUi

    def retranslateUi(self, AIAssistantWindow):
        AIAssistantWindow.setWindowTitle(QCoreApplication.translate("AIAssistantWindow", u"AI Assistant", None))
        self.actionPreferences.setText(QCoreApplication.translate("AIAssistantWindow", u"Preferences", None))
        self.actionHow_to_make_API_key.setText(QCoreApplication.translate("AIAssistantWindow", u"How to make API key", None))
        self.actionMake_new_API_key.setText(QCoreApplication.translate("AIAssistantWindow", u"Make new API key", None))
        self.labelModelName.setText(QCoreApplication.translate("AIAssistantWindow", u"TextLabel", None))
        self.labelCreativity.setText(QCoreApplication.translate("AIAssistantWindow", u"TextLabel", None))
        self.labelTalkativeness.setText(QCoreApplication.translate("AIAssistantWindow", u"TextLabel", None))
        self.pushButtonSend.setText(QCoreApplication.translate("AIAssistantWindow", u"Send", None))
        self.menuSettings.setTitle(QCoreApplication.translate("AIAssistantWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("AIAssistantWindow", u"Help", None))
    # retranslateUi

