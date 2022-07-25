# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 515)
        MainWindow.setMinimumSize(QSize(720, 515))
        self.actionQuit_VeTools = QAction(MainWindow)
        self.actionQuit_VeTools.setObjectName(u"actionQuit_VeTools")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        self.gridLayout = QGridLayout(self.start_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.disease_selection = QComboBox(self.start_page)
        self.disease_selection.addItem("")
        self.disease_selection.addItem("")
        self.disease_selection.addItem("")
        self.disease_selection.setObjectName(u"disease_selection")

        self.verticalLayout_3.addWidget(self.disease_selection)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.start_button = QPushButton(self.start_page)
        self.start_button.setObjectName(u"start_button")

        self.verticalLayout_2.addWidget(self.start_button, 0, Qt.AlignHCenter)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.start_page)
        self.question_page = QWidget()
        self.question_page.setObjectName(u"question_page")
        self.gridLayout_2 = QGridLayout(self.question_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 95, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(100, 28, 100, -1)
        self.question = QLabel(self.question_page)
        self.question.setObjectName(u"question")
        self.question.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.question.setWordWrap(True)
        self.question.setMargin(0)

        self.verticalLayout_4.addWidget(self.question, 0, Qt.AlignTop)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, -1, 30, -1)
        self.end_button = QPushButton(self.question_page)
        self.end_button.setObjectName(u"end_button")

        self.horizontalLayout_2.addWidget(self.end_button)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.prev_button = QPushButton(self.question_page)
        self.prev_button.setObjectName(u"prev_button")

        self.horizontalLayout_2.addWidget(self.prev_button)

        self.next_button = QPushButton(self.question_page)
        self.next_button.setObjectName(u"next_button")

        self.horizontalLayout_2.addWidget(self.next_button)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 131, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.option_0 = QRadioButton(self.question_page)
        self.option_0.setObjectName(u"option_0")

        self.horizontalLayout.addWidget(self.option_0)

        self.horizontalSpacer_7 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.option_1 = QRadioButton(self.question_page)
        self.option_1.setObjectName(u"option_1")

        self.horizontalLayout.addWidget(self.option_1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.question_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.education_textbox = QTextBrowser(self.page)
        self.education_textbox.setObjectName(u"education_textbox")
        self.education_textbox.setOpenLinks(False)

        self.verticalLayout_6.addWidget(self.education_textbox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(30, -1, 30, -1)
        self.end_button_2 = QPushButton(self.page)
        self.end_button_2.setObjectName(u"end_button_2")

        self.horizontalLayout_3.addWidget(self.end_button_2)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.prev_button_2 = QPushButton(self.page)
        self.prev_button_2.setObjectName(u"prev_button_2")

        self.horizontalLayout_3.addWidget(self.prev_button_2)

        self.next_button_2 = QPushButton(self.page)
        self.next_button_2.setObjectName(u"next_button_2")

        self.horizontalLayout_3.addWidget(self.next_button_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionQuit_VeTools)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit_VeTools.setText(QCoreApplication.translate("MainWindow", u"Quit VeTools", None))
        self.disease_selection.setItemText(0, QCoreApplication.translate("MainWindow", u"Lyme Disease", None))
        self.disease_selection.setItemText(1, QCoreApplication.translate("MainWindow", u"Fecal Positive Roundworm", None))
        self.disease_selection.setItemText(2, QCoreApplication.translate("MainWindow", u"Fecal Positive Hookworm", None))

        self.disease_selection.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a positive result...", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start Questionaire", None))
        self.question.setText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Et netus et malesuada fames ac turpis. Lorem mollis aliquam ut porttitor. Magna sit amet purus gravida quis blandit turpis.", None))
        self.end_button.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.prev_button.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.option_0.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.option_1.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.end_button_2.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.prev_button_2.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.next_button_2.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

