# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(681, 399)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"#sideW{\n"
"    border-right:1px solid #3A3A3A;\n"
"	border-top:1px solid #3A3A3A;\n"
"	border-bottom:1px solid #3A3A3A;\n"
"	border-radius:5px;\n"
"\n"
"}\n"
"\n"
"#bee,#gtFrame,#chatBox{\n"
"	 border:1px solid #3A3A3A;\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sideW = QWidget(self.centralwidget)
        self.sideW.setObjectName(u"sideW")
        self.sideW.setMinimumSize(QSize(200, 0))
        self.sideW.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.sideW)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bee = QLabel(self.sideW)
        self.bee.setObjectName(u"bee")
        self.bee.setMinimumSize(QSize(0, 50))
        self.bee.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.bee.setFont(font)
        self.bee.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.bee)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.newChat = QPushButton(self.sideW)
        self.newChat.setObjectName(u"newChat")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.newChat.sizePolicy().hasHeightForWidth())
        self.newChat.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.newChat)

        self.chatHis = QPushButton(self.sideW)
        self.chatHis.setObjectName(u"chatHis")
        sizePolicy1.setHeightForWidth(self.chatHis.sizePolicy().hasHeightForWidth())
        self.chatHis.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.chatHis)

        self.dashboard = QPushButton(self.sideW)
        self.dashboard.setObjectName(u"dashboard")
        sizePolicy1.setHeightForWidth(self.dashboard.sizePolicy().hasHeightForWidth())
        self.dashboard.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.dashboard)

        self.settings = QPushButton(self.sideW)
        self.settings.setObjectName(u"settings")
        sizePolicy1.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.settings)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)

        self.horizontalLayout.addWidget(self.sideW)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gtFrame = QFrame(self.page)
        self.gtFrame.setObjectName(u"gtFrame")
        sizePolicy.setHeightForWidth(self.gtFrame.sizePolicy().hasHeightForWidth())
        self.gtFrame.setSizePolicy(sizePolicy)
        self.gtFrame.setMinimumSize(QSize(0, 40))
        self.gtFrame.setMaximumSize(QSize(16777215, 60))
        self.gtFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.gtFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.gtFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gt1 = QLabel(self.gtFrame)
        self.gt1.setObjectName(u"gt1")
        sizePolicy2.setHeightForWidth(self.gt1.sizePolicy().hasHeightForWidth())
        self.gt1.setSizePolicy(sizePolicy2)
        self.gt1.setMinimumSize(QSize(0, 30))
        self.gt1.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.gt1.setFont(font1)
        self.gt1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.gt1)

        self.gt2 = QLabel(self.gtFrame)
        self.gt2.setObjectName(u"gt2")
        sizePolicy2.setHeightForWidth(self.gt2.sizePolicy().hasHeightForWidth())
        self.gt2.setSizePolicy(sizePolicy2)
        self.gt2.setMinimumSize(QSize(0, 20))
        self.gt2.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setPointSize(10)
        self.gt2.setFont(font2)
        self.gt2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.gt2)


        self.verticalLayout.addWidget(self.gtFrame)

        self.chatBox = QScrollArea(self.page)
        self.chatBox.setObjectName(u"chatBox")
        self.chatBox.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 437, 239))
        self.chatBox.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.chatBox)

        self.frameLine = QFrame(self.page)
        self.frameLine.setObjectName(u"frameLine")
        sizePolicy2.setHeightForWidth(self.frameLine.sizePolicy().hasHeightForWidth())
        self.frameLine.setSizePolicy(sizePolicy2)
        self.frameLine.setMinimumSize(QSize(0, 50))
        self.frameLine.setMaximumSize(QSize(16777215, 70))
        self.frameLine.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLine.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameLine)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.frameLine)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.Sendbtn = QPushButton(self.frameLine)
        self.Sendbtn.setObjectName(u"Sendbtn")

        self.horizontalLayout_2.addWidget(self.Sendbtn)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout.addWidget(self.frameLine)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #3A3A3A;\n"
"    background-color: transparent;\n"
"    color: grey;\n"
"    text-align: left;\n"
"    padding: 10px 15px;\n"
"    border-radius: 8px;\n"
"    font-size: 20px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2D2D2D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #404040;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_14 = QLabel(self.page_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy4)
        self.label_14.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.label_14.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_14)

        self.chatBtn1 = QPushButton(self.page_2)
        self.chatBtn1.setObjectName(u"chatBtn1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.chatBtn1.sizePolicy().hasHeightForWidth())
        self.chatBtn1.setSizePolicy(sizePolicy5)
        font4 = QFont()
        font4.setWeight(QFont.Medium)
        self.chatBtn1.setFont(font4)
        self.chatBtn1.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.chatBtn1)

        self.chatBtn2 = QPushButton(self.page_2)
        self.chatBtn2.setObjectName(u"chatBtn2")

        self.verticalLayout_4.addWidget(self.chatBtn2)

        self.chatBtn3 = QPushButton(self.page_2)
        self.chatBtn3.setObjectName(u"chatBtn3")

        self.verticalLayout_4.addWidget(self.chatBtn3)

        self.chatBtn4 = QPushButton(self.page_2)
        self.chatBtn4.setObjectName(u"chatBtn4")

        self.verticalLayout_4.addWidget(self.chatBtn4)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 18);\n"
"    border: 2px solid rgba(255, 255, 255, 180);\n"
"    border-radius: 18px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background-color: rgba(255, 255, 255, 25);\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"}")
        self.gridLayout = QGridLayout(self.page_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.page_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setPointSize(26)
        font5.setBold(True)
        self.label_2.setFont(font5)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        font6 = QFont()
        font6.setBold(True)
        self.label.setFont(font6)

        self.verticalLayout_5.addWidget(self.label)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        font7 = QFont()
        font7.setItalic(True)
        self.label_4.setFont(font7)

        self.verticalLayout_5.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setFont(font6)

        self.verticalLayout_5.addWidget(self.label_5)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 6)

        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.page_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        font8 = QFont()
        font8.setPointSize(18)
        font8.setBold(False)
        self.label_10.setFont(font8)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setFont(font6)

        self.verticalLayout_7.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setFont(font7)

        self.verticalLayout_7.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setFont(font6)

        self.verticalLayout_7.addWidget(self.label_13)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 6)

        self.gridLayout.addWidget(self.frame_5, 2, 0, 1, 1)

        self.frame_3 = QFrame(self.page_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        font9 = QFont()
        font9.setPointSize(22)
        font9.setBold(False)
        self.label_6.setFont(font9)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setFont(font6)

        self.verticalLayout_6.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setFont(font7)

        self.verticalLayout_6.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setFont(font6)

        self.verticalLayout_6.addWidget(self.label_9)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 6)

        self.gridLayout.addWidget(self.frame_3, 1, 1, 2, 1)

        self.label_15 = QLabel(self.page_3)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)
        font10 = QFont()
        font10.setPointSize(16)
        font10.setBold(True)
        self.label_15.setFont(font10)

        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_2 = QGridLayout(self.page_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.page_4)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1)

        self.label_20 = QLabel(self.page_4)
        self.label_20.setObjectName(u"label_20")
        sizePolicy4.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy4)
        self.label_20.setFont(font10)

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_19 = QLabel(self.page_4)
        self.label_19.setObjectName(u"label_19")
        font11 = QFont()
        font11.setPointSize(12)
        self.label_19.setFont(font11)

        self.gridLayout_2.addWidget(self.label_19, 4, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.page_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 4, 1, 1, 1)

        self.label_18 = QLabel(self.page_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font11)

        self.gridLayout_2.addWidget(self.label_18, 3, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.page_4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 2, 1, 1, 1)

        self.label_16 = QLabel(self.page_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font11)

        self.gridLayout_2.addWidget(self.label_16, 1, 0, 1, 1)

        self.label_17 = QLabel(self.page_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font11)

        self.gridLayout_2.addWidget(self.label_17, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.page_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_3 = QGridLayout(self.page_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_22 = QLabel(self.page_5)
        self.label_22.setObjectName(u"label_22")
        sizePolicy4.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy4)
        self.label_22.setFont(font11)
        self.label_22.setStyleSheet(u"QLabel{\n"
"	border:1px solid black;\n"
"	border-radius: 1px;\n"
"	\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.label_22, 4, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.page_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_3.addWidget(self.lineEdit_6, 10, 0, 1, 2)

        self.label_26 = QLabel(self.page_5)
        self.label_26.setObjectName(u"label_26")
        sizePolicy4.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy4)
        self.label_26.setFont(font11)
        self.label_26.setStyleSheet(u"QLabel{\n"
"	border:1px solid black;\n"
"	border-radius: 1px;\n"
"	\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.label_26, 6, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.page_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_3.addWidget(self.lineEdit_4, 5, 0, 1, 2)

        self.label_25 = QLabel(self.page_5)
        self.label_25.setObjectName(u"label_25")
        sizePolicy4.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy4)
        self.label_25.setFont(font11)
        self.label_25.setStyleSheet(u"QLabel{\n"
"	border:1px solid black;\n"
"	border-radius: 1px;\n"
"	\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.label_25, 13, 2, 1, 1)

        self.lineEdit_7 = QLineEdit(self.page_5)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_3.addWidget(self.lineEdit_7, 12, 0, 1, 2)

        self.lineEdit_5 = QLineEdit(self.page_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_3.addWidget(self.lineEdit_5, 6, 0, 1, 2)

        self.label_23 = QLabel(self.page_5)
        self.label_23.setObjectName(u"label_23")
        sizePolicy4.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy4)
        self.label_23.setFont(font11)
        self.label_23.setStyleSheet(u"QLabel{\n"
"	border:1px solid black;\n"
"	border-radius: 1px;\n"
"	\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.label_23, 5, 2, 1, 1)

        self.lineEdit_9 = QLineEdit(self.page_5)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_3.addWidget(self.lineEdit_9, 13, 0, 1, 2)

        self.label_28 = QLabel(self.page_5)
        self.label_28.setObjectName(u"label_28")
        sizePolicy4.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy4)
        self.label_28.setFont(font11)
        self.label_28.setStyleSheet(u"QLabel{\n"
"	border:1px solid black;\n"
"	border-radius: 1px;\n"
"	\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.label_28, 10, 2, 1, 1)

        self.label_27 = QLabel(self.page_5)
        self.label_27.setObjectName(u"label_27")
        sizePolicy4.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy4)
        self.label_27.setFont(font11)
        self.label_27.setStyleSheet(u"QLabel{\n"
"	border:1px solid black;\n"
"	border-radius: 1px;\n"
"	\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.label_27, 12, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.page_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 4, 0, 1, 2)

        self.label_3 = QLabel(self.page_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font10)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_24 = QLabel(self.page_5)
        self.label_24.setObjectName(u"label_24")
        sizePolicy4.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy4)
        self.label_24.setFont(font11)
        self.label_24.setStyleSheet(u"QLabel{\n"
"	border:1px solid black;\n"
"	border-radius: 1px;\n"
"	\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.label_24, 9, 2, 1, 1)

        self.lineEdit_8 = QLineEdit(self.page_5)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_3.addWidget(self.lineEdit_8, 9, 0, 1, 2)

        self.label_21 = QLabel(self.page_5)
        self.label_21.setObjectName(u"label_21")
        sizePolicy4.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy4)
        self.label_21.setFont(font11)
        self.label_21.setStyleSheet(u"QLabel{\n"
"	border:1px solid black;\n"
"	border-radius: 1px;\n"
"	\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.label_21, 3, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.page_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy3.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_5)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bee.setText(QCoreApplication.translate("MainWindow", u"B.E.E", None))
        self.newChat.setText(QCoreApplication.translate("MainWindow", u"New Chats", None))
        self.chatHis.setText(QCoreApplication.translate("MainWindow", u"Chat History", None))
        self.dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Settibgs", None))
        self.gt1.setText(QCoreApplication.translate("MainWindow", u"Good to see you again", None))
        self.gt2.setText(QCoreApplication.translate("MainWindow", u"     What would you like to do first?", None))
        self.Sendbtn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Your last few chats.......", None))
        self.chatBtn1.setText(QCoreApplication.translate("MainWindow", u"history text one", None))
        self.chatBtn2.setText(QCoreApplication.translate("MainWindow", u"history text two", None))
        self.chatBtn3.setText(QCoreApplication.translate("MainWindow", u"history text three", None))
        self.chatBtn4.setText(QCoreApplication.translate("MainWindow", u"history text four", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u2302", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RENT DUE:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Due Today", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u20b92950", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\U0001f6d2", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"GROCERY", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"5 Items in cart", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u20b91200", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u2668", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TIFFINE DUE:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Due Today", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u20b92400", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Today's Overview", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Logout:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Logout Your Account", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Version:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Fill Details", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Appearance:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Details:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"                    vers.1.1005.7v", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"fjkhfhf", None))

        self.label_22.setText(QCoreApplication.translate("MainWindow", u"7355562687@axl", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tiffine Service Name", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"7355562687@axl", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Landloard Name", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"7355562687", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tiffine Service UPI ID", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Landloard UPI Id", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Arjun Bhaiya", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tiffine Service Number", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Nepali mess", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"7355562687@axl", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User UPI ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"7355562687", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Landloard NUmber", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"ashutosh", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
    # retranslateUi

