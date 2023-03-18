# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AISettingsWindow(object):
    def setupUi(self, AISettingsWindow):
        if not AISettingsWindow.objectName():
            AISettingsWindow.setObjectName(u"AISettingsWindow")
        AISettingsWindow.resize(649, 553)
        AISettingsWindow.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.centralwidget = QWidget(AISettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxAPIKey = QGroupBox(self.centralwidget)
        self.groupBoxAPIKey.setObjectName(u"groupBoxAPIKey")
        self.groupBoxAPIKey.setMaximumSize(QSize(16777215, 96))
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxAPIKey)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelAPIKeyStatus = QLabel(self.groupBoxAPIKey)
        self.labelAPIKeyStatus.setObjectName(u"labelAPIKeyStatus")
        self.labelAPIKeyStatus.setStyleSheet(u"font: 13pt \"Segoe UI\";")
        self.labelAPIKeyStatus.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelAPIKeyStatus)

        self.pushButtonSetAPIKey = QPushButton(self.groupBoxAPIKey)
        self.pushButtonSetAPIKey.setObjectName(u"pushButtonSetAPIKey")

        self.verticalLayout_2.addWidget(self.pushButtonSetAPIKey)


        self.verticalLayout.addWidget(self.groupBoxAPIKey)

        self.groupBoxModels = QGroupBox(self.centralwidget)
        self.groupBoxModels.setObjectName(u"groupBoxModels")
        self.verticalLayout_3 = QVBoxLayout(self.groupBoxModels)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelModelImage = QLabel(self.groupBoxModels)
        self.labelModelImage.setObjectName(u"labelModelImage")
        self.labelModelImage.setMinimumSize(QSize(200, 150))
        self.labelModelImage.setMaximumSize(QSize(400, 300))
        self.labelModelImage.setLayoutDirection(Qt.LeftToRight)
        self.labelModelImage.setPixmap(QPixmap(u"images/code-cushman-001.png"))
        self.labelModelImage.setScaledContents(False)
        self.labelModelImage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelModelImage)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelModelName = QLabel(self.groupBoxModels)
        self.labelModelName.setObjectName(u"labelModelName")
        self.labelModelName.setMaximumSize(QSize(16777215, 32))
        self.labelModelName.setStyleSheet(u"font: 13pt \"Segoe UI\";")
        self.labelModelName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelModelName)

        self.labelModelDescription = QLabel(self.groupBoxModels)
        self.labelModelDescription.setObjectName(u"labelModelDescription")
        self.labelModelDescription.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.labelModelDescription.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.labelModelDescription)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.groupBoxModels)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(96, 21))

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lineEditBehavior = QLineEdit(self.groupBoxModels)
        self.lineEditBehavior.setObjectName(u"lineEditBehavior")

        self.horizontalLayout_2.addWidget(self.lineEditBehavior)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBoxModels)

        self.groupBoxCreativity = QGroupBox(self.centralwidget)
        self.groupBoxCreativity.setObjectName(u"groupBoxCreativity")
        self.groupBoxCreativity.setMaximumSize(QSize(16777215, 64))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBoxCreativity)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBoxCreativity)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSliderCreativity = QSlider(self.groupBoxCreativity)
        self.horizontalSliderCreativity.setObjectName(u"horizontalSliderCreativity")
        self.horizontalSliderCreativity.setMinimum(1)
        self.horizontalSliderCreativity.setMaximum(100)
        self.horizontalSliderCreativity.setValue(50)
        self.horizontalSliderCreativity.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSliderCreativity)

        self.label_2 = QLabel(self.groupBoxCreativity)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.groupBoxCreativity)

        self.groupBoxTalkativeness = QGroupBox(self.centralwidget)
        self.groupBoxTalkativeness.setObjectName(u"groupBoxTalkativeness")
        self.groupBoxTalkativeness.setMaximumSize(QSize(16777215, 64))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBoxTalkativeness)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBoxTalkativeness)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSliderTalkativeness = QSlider(self.groupBoxTalkativeness)
        self.horizontalSliderTalkativeness.setObjectName(u"horizontalSliderTalkativeness")
        self.horizontalSliderTalkativeness.setMinimum(25)
        self.horizontalSliderTalkativeness.setMaximum(4096)
        self.horizontalSliderTalkativeness.setValue(50)
        self.horizontalSliderTalkativeness.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.horizontalSliderTalkativeness)

        self.label_4 = QLabel(self.groupBoxTalkativeness)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.groupBoxTalkativeness)

        AISettingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AISettingsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 649, 21))
        AISettingsWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AISettingsWindow)
        self.statusbar.setObjectName(u"statusbar")
        AISettingsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AISettingsWindow)

        QMetaObject.connectSlotsByName(AISettingsWindow)
    # setupUi

    def retranslateUi(self, AISettingsWindow):
        AISettingsWindow.setWindowTitle(QCoreApplication.translate("AISettingsWindow", u"AI Settings Window", None))
        self.groupBoxAPIKey.setTitle(QCoreApplication.translate("AISettingsWindow", u"API Key", None))
        self.labelAPIKeyStatus.setText(QCoreApplication.translate("AISettingsWindow", u"Status: No API Key", None))
        self.pushButtonSetAPIKey.setText(QCoreApplication.translate("AISettingsWindow", u"Set API Key", None))
        self.groupBoxModels.setTitle(QCoreApplication.translate("AISettingsWindow", u"Model", None))
        self.labelModelImage.setText("")
        self.labelModelName.setText(QCoreApplication.translate("AISettingsWindow", u"TextLabel", None))
        self.labelModelDescription.setText(QCoreApplication.translate("AISettingsWindow", u"Capable of very simple tasks, usually the fastest model in the GPT-3 series, and lowest cost.", None))
        self.label_5.setText(QCoreApplication.translate("AISettingsWindow", u"Model behavior:", None))
        self.groupBoxCreativity.setTitle(QCoreApplication.translate("AISettingsWindow", u"Creativity", None))
        self.label.setText(QCoreApplication.translate("AISettingsWindow", u"Direct", None))
        self.label_2.setText(QCoreApplication.translate("AISettingsWindow", u"Creative", None))
        self.groupBoxTalkativeness.setTitle(QCoreApplication.translate("AISettingsWindow", u"Talkativeness", None))
        self.label_3.setText(QCoreApplication.translate("AISettingsWindow", u"Reticent", None))
        self.label_4.setText(QCoreApplication.translate("AISettingsWindow", u"Talkative", None))
    # retranslateUi

