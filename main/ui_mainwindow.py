# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2281, 1249)
        MainWindow.setWindowOpacity(0.950000000000000)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionInstructions = QAction(MainWindow)
        self.actionInstructions.setObjectName(u"actionInstructions")
        self.actionAuthors = QAction(MainWindow)
        self.actionAuthors.setObjectName(u"actionAuthors")
        self.actionUser = QAction(MainWindow)
        self.actionUser.setObjectName(u"actionUser")
        self.actionLibrarian = QAction(MainWindow)
        self.actionLibrarian.setObjectName(u"actionLibrarian")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(980, 940, 851, 241))
        self.WindowStart = QGridLayout(self.gridLayoutWidget_3)
        self.WindowStart.setObjectName(u"WindowStart")
        self.WindowStart.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.gridLayoutWidget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.WindowStart.addWidget(self.line_3, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.WindowStart.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WindowStart.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(330, 0))
        self.label_3.setMaximumSize(QSize(343, 50))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.WindowStart.addWidget(self.label_3, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WindowStart.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.WindowStart.addWidget(self.label, 4, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.WindowStart.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.line_4 = QFrame(self.gridLayoutWidget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.WindowStart.addWidget(self.line_4, 3, 1, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(30, 30, 1094, 451))
        self.WindowUserMain = QGridLayout(self.gridLayoutWidget_4)
        self.WindowUserMain.setObjectName(u"WindowUserMain")
        self.WindowUserMain.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Label = QLabel(self.gridLayoutWidget_4)
        self.Label.setObjectName(u"Label")
        self.Label.setMinimumSize(QSize(0, 5))
        self.Label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(14)
        self.Label.setFont(font)
        self.Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.Label, 0, 0, 1, 1)

        self.Description = QLabel(self.gridLayoutWidget_4)
        self.Description.setObjectName(u"Description")
        self.Description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.Description.setWordWrap(True)

        self.gridLayout_4.addWidget(self.Description, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 1, 1, 1)

        self.Photo = QLabel(self.gridLayoutWidget_4)
        self.Photo.setObjectName(u"Photo")
        self.Photo.setMinimumSize(QSize(100, 200))
        self.Photo.setMaximumSize(QSize(200, 266))

        self.gridLayout_3.addWidget(self.Photo, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.table_UserYour = QTableWidget(self.gridLayoutWidget_4)
        self.table_UserYour.setObjectName(u"table_UserYour")

        self.gridLayout_9.addWidget(self.table_UserYour, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_9.addWidget(self.label_4, 0, 1, 1, 1)

        self.table_UserTake = QTableWidget(self.gridLayoutWidget_4)
        self.table_UserTake.setObjectName(u"table_UserTake")
        self.table_UserTake.setMinimumSize(QSize(400, 0))
        self.table_UserTake.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_9.addWidget(self.table_UserTake, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_9, 1, 0, 1, 1)


        self.WindowUserMain.addLayout(self.gridLayout_2, 1, 2, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.but_Take = QPushButton(self.gridLayoutWidget_4)
        self.but_Take.setObjectName(u"but_Take")
        self.but_Take.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_5.addWidget(self.but_Take, 0, 0, 1, 1)

        self.but_Give = QPushButton(self.gridLayoutWidget_4)
        self.but_Give.setObjectName(u"but_Give")
        self.but_Give.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_5.addWidget(self.but_Give, 0, 1, 1, 1)


        self.WindowUserMain.addLayout(self.gridLayout_5, 2, 2, 1, 1)

        self.line_Query = QLineEdit(self.gridLayoutWidget_4)
        self.line_Query.setObjectName(u"line_Query")

        self.WindowUserMain.addWidget(self.line_Query, 2, 0, 1, 1)

        self.table_Library = QTableWidget(self.gridLayoutWidget_4)
        self.table_Library.setObjectName(u"table_Library")
        self.table_Library.setMinimumSize(QSize(600, 0))
        self.table_Library.setMaximumSize(QSize(16777215, 16777215))

        self.WindowUserMain.addWidget(self.table_Library, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_7 = QFrame(self.gridLayoutWidget_4)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_7)

        self.radBut_Name = QRadioButton(self.gridLayoutWidget_4)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radBut_Name)
        self.radBut_Name.setObjectName(u"radBut_Name")
        self.radBut_Name.setMinimumSize(QSize(30, 0))
        self.radBut_Name.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.radBut_Name)

        self.line_5 = QFrame(self.gridLayoutWidget_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.radBut_Author = QRadioButton(self.gridLayoutWidget_4)
        self.buttonGroup.addButton(self.radBut_Author)
        self.radBut_Author.setObjectName(u"radBut_Author")

        self.horizontalLayout.addWidget(self.radBut_Author)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_8 = QFrame(self.gridLayoutWidget_4)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_8)

        self.radBut_Genre = QRadioButton(self.gridLayoutWidget_4)
        self.buttonGroup.addButton(self.radBut_Genre)
        self.radBut_Genre.setObjectName(u"radBut_Genre")
        self.radBut_Genre.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.radBut_Genre)

        self.line_6 = QFrame(self.gridLayoutWidget_4)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_6)

        self.radBut_ShowAll = QRadioButton(self.gridLayoutWidget_4)
        self.buttonGroup.addButton(self.radBut_ShowAll)
        self.radBut_ShowAll.setObjectName(u"radBut_ShowAll")

        self.horizontalLayout_2.addWidget(self.radBut_ShowAll)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.WindowUserMain.addLayout(self.verticalLayout, 4, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.but_Printout = QPushButton(self.gridLayoutWidget_4)
        self.but_Printout.setObjectName(u"but_Printout")
        self.but_Printout.setMinimumSize(QSize(50, 0))
        self.but_Printout.setMaximumSize(QSize(100, 16777215))
        self.but_Printout.setAutoFillBackground(False)

        self.gridLayout_6.addWidget(self.but_Printout, 0, 0, 1, 1)


        self.WindowUserMain.addLayout(self.gridLayout_6, 4, 2, 1, 1)

        self.gridLayoutWidget_9 = QWidget(self.centralwidget)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(640, 570, 391, 321))
        self.WindowLibrarianAuthentication = QGridLayout(self.gridLayoutWidget_9)
        self.WindowLibrarianAuthentication.setObjectName(u"WindowLibrarianAuthentication")
        self.WindowLibrarianAuthentication.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WindowLibrarianAuthentication.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_8, 0, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.butLibrarian = QPushButton(self.gridLayoutWidget_9)
        self.butLibrarian.setObjectName(u"butLibrarian")

        self.gridLayout_13.addWidget(self.butLibrarian, 0, 1, 1, 1)


        self.WindowLibrarianAuthentication.addLayout(self.gridLayout_13, 5, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.WindowLibrarianAuthentication.addItem(self.verticalSpacer_6, 6, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WindowLibrarianAuthentication.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.line_10 = QFrame(self.gridLayoutWidget_9)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.WindowLibrarianAuthentication.addWidget(self.line_10, 2, 1, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.line_Login = QLineEdit(self.gridLayoutWidget_9)
        self.line_Login.setObjectName(u"line_Login")
        self.line_Login.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_12.addWidget(self.line_Login, 0, 0, 1, 1)

        self.line_Password = QLineEdit(self.gridLayoutWidget_9)
        self.line_Password.setObjectName(u"line_Password")
        self.line_Password.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_12.addWidget(self.line_Password, 0, 1, 1, 1)


        self.WindowLibrarianAuthentication.addLayout(self.gridLayout_12, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.WindowLibrarianAuthentication.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.WindowLibrarianAuthentication.addWidget(self.label_5, 1, 1, 1, 1)

        self.line_11 = QFrame(self.gridLayoutWidget_9)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.WindowLibrarianAuthentication.addWidget(self.line_11, 4, 1, 1, 1)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 500, 481, 301))
        self.WindowUserAuthentication = QGridLayout(self.layoutWidget)
        self.WindowUserAuthentication.setObjectName(u"WindowUserAuthentication")
        self.WindowUserAuthentication.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_Address = QLabel(self.layoutWidget)
        self.label_Address.setObjectName(u"label_Address")

        self.horizontalLayout_5.addWidget(self.label_Address)

        self.line_AddressCity = QLineEdit(self.layoutWidget)
        self.line_AddressCity.setObjectName(u"line_AddressCity")

        self.horizontalLayout_5.addWidget(self.line_AddressCity)

        self.line_AddressStreet = QLineEdit(self.layoutWidget)
        self.line_AddressStreet.setObjectName(u"line_AddressStreet")
        self.line_AddressStreet.setMaximumSize(QSize(138, 16777215))

        self.horizontalLayout_5.addWidget(self.line_AddressStreet)

        self.line_Address_ZipCode = QLineEdit(self.layoutWidget)
        self.line_Address_ZipCode.setObjectName(u"line_Address_ZipCode")
        self.line_Address_ZipCode.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_5.addWidget(self.line_Address_ZipCode)


        self.gridLayout_11.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.WindowUserAuthentication.addLayout(self.gridLayout_11, 6, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.WindowUserAuthentication.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.lab_OptionalData = QLabel(self.layoutWidget)
        self.lab_OptionalData.setObjectName(u"lab_OptionalData")

        self.WindowUserAuthentication.addWidget(self.lab_OptionalData, 4, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WindowUserAuthentication.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.WindowUserAuthentication.addWidget(self.line_2, 2, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.WindowUserAuthentication.addItem(self.verticalSpacer_5, 11, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.line_PhoneNumber = QLineEdit(self.layoutWidget)
        self.line_PhoneNumber.setObjectName(u"line_PhoneNumber")

        self.gridLayout_8.addWidget(self.line_PhoneNumber, 0, 0, 1, 1)

        self.line_Email = QLineEdit(self.layoutWidget)
        self.line_Email.setObjectName(u"line_Email")

        self.gridLayout_8.addWidget(self.line_Email, 0, 1, 1, 1)


        self.WindowUserAuthentication.addLayout(self.gridLayout_8, 7, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.line_MiddleName = QLineEdit(self.layoutWidget)
        self.line_MiddleName.setObjectName(u"line_MiddleName")

        self.gridLayout_7.addWidget(self.line_MiddleName, 0, 3, 1, 1)

        self.line_FirstName = QLineEdit(self.layoutWidget)
        self.line_FirstName.setObjectName(u"line_FirstName")
        self.line_FirstName.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_7.addWidget(self.line_FirstName, 0, 1, 1, 1)

        self.line_LastName = QLineEdit(self.layoutWidget)
        self.line_LastName.setObjectName(u"line_LastName")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_LastName.sizePolicy().hasHeightForWidth())
        self.line_LastName.setSizePolicy(sizePolicy)
        self.line_LastName.setMinimumSize(QSize(10, 0))
        self.line_LastName.setMaximumSize(QSize(130, 16777215))

        self.gridLayout_7.addWidget(self.line_LastName, 0, 2, 1, 1)


        self.WindowUserAuthentication.addLayout(self.gridLayout_7, 3, 1, 1, 1)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.WindowUserAuthentication.addWidget(self.line, 5, 1, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_DateOfBirth = QLabel(self.layoutWidget)
        self.label_DateOfBirth.setObjectName(u"label_DateOfBirth")

        self.horizontalLayout_3.addWidget(self.label_DateOfBirth)

        self.line_Day = QLineEdit(self.layoutWidget)
        self.line_Day.setObjectName(u"line_Day")
        self.line_Day.setMinimumSize(QSize(4, 0))
        self.line_Day.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.line_Day)

        self.line_Month = QLineEdit(self.layoutWidget)
        self.line_Month.setObjectName(u"line_Month")
        self.line_Month.setMinimumSize(QSize(4, 0))
        self.line_Month.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.line_Month)

        self.line_Year = QLineEdit(self.layoutWidget)
        self.line_Year.setObjectName(u"line_Year")
        self.line_Year.setMinimumSize(QSize(4, 0))
        self.line_Year.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.line_Year)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout_10.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)


        self.WindowUserAuthentication.addLayout(self.gridLayout_10, 9, 1, 1, 1)

        self.lab_PersonalData = QLabel(self.layoutWidget)
        self.lab_PersonalData.setObjectName(u"lab_PersonalData")

        self.WindowUserAuthentication.addWidget(self.lab_PersonalData, 1, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.WindowUserAuthentication.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.but_Continue = QPushButton(self.layoutWidget)
        self.but_Continue.setObjectName(u"but_Continue")

        self.gridLayout.addWidget(self.but_Continue, 0, 1, 1, 1)


        self.WindowUserAuthentication.addLayout(self.gridLayout, 10, 1, 1, 1)

        self.gridLayoutWidget_10 = QWidget(self.centralwidget)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(1050, 440, 918, 451))
        self.WindowLibrarianMain = QGridLayout(self.gridLayoutWidget_10)
        self.WindowLibrarianMain.setObjectName(u"WindowLibrarianMain")
        self.WindowLibrarianMain.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.line_FirstNameLib = QLineEdit(self.gridLayoutWidget_10)
        self.line_FirstNameLib.setObjectName(u"line_FirstNameLib")
        self.line_FirstNameLib.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.line_FirstNameLib)

        self.line_LastNameLib = QLineEdit(self.gridLayoutWidget_10)
        self.line_LastNameLib.setObjectName(u"line_LastNameLib")
        self.line_LastNameLib.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_6.addWidget(self.line_LastNameLib)

        self.line_MiddleNameLib = QLineEdit(self.gridLayoutWidget_10)
        self.line_MiddleNameLib.setObjectName(u"line_MiddleNameLib")
        self.line_MiddleNameLib.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_6.addWidget(self.line_MiddleNameLib)


        self.gridLayout_15.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.but_Enter = QPushButton(self.gridLayoutWidget_10)
        self.but_Enter.setObjectName(u"but_Enter")

        self.gridLayout_17.addWidget(self.but_Enter, 0, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_17, 2, 1, 1, 1)

        self.table_UserBooksLibrary = QTableWidget(self.gridLayoutWidget_10)
        self.table_UserBooksLibrary.setObjectName(u"table_UserBooksLibrary")
        self.table_UserBooksLibrary.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.table_UserBooksLibrary, 4, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_6, 0, 1, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.but_MakeChanges = QPushButton(self.gridLayoutWidget_10)
        self.but_MakeChanges.setObjectName(u"but_MakeChanges")

        self.gridLayout_18.addWidget(self.but_MakeChanges, 0, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_18, 5, 1, 1, 1)

        self.table_OperationsLibrary = QTableWidget(self.gridLayoutWidget_10)
        self.table_OperationsLibrary.setObjectName(u"table_OperationsLibrary")
        self.table_OperationsLibrary.setMinimumSize(QSize(300, 0))

        self.gridLayout_15.addWidget(self.table_OperationsLibrary, 4, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_10)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_15.addWidget(self.label_7, 2, 0, 1, 1)


        self.WindowLibrarianMain.addLayout(self.gridLayout_15, 0, 3, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.tableLibLibrary = QTableWidget(self.gridLayoutWidget_10)
        self.tableLibLibrary.setObjectName(u"tableLibLibrary")
        self.tableLibLibrary.setMinimumSize(QSize(300, 0))
        self.tableLibLibrary.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_14.addWidget(self.tableLibLibrary, 0, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_10, 0, 0, 1, 1)

        self.but_addBook = QPushButton(self.gridLayoutWidget_10)
        self.but_addBook.setObjectName(u"but_addBook")

        self.gridLayout_16.addWidget(self.but_addBook, 0, 1, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_16, 1, 0, 1, 1)


        self.WindowLibrarianMain.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.line_9 = QFrame(self.gridLayoutWidget_10)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.WindowLibrarianMain.addWidget(self.line_9, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2281, 22))
        self.menuMain = QMenu(self.menubar)
        self.menuMain.setObjectName(u"menuMain")
        self.menuService = QMenu(self.menubar)
        self.menuService.setObjectName(u"menuService")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuService.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuMain.addAction(self.actionUser)
        self.menuService.addAction(self.actionLibrarian)
        self.menuAbout.addAction(self.actionInstructions)
        self.menuAbout.addAction(self.actionAuthors)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Library Management System", None))
        self.actionInstructions.setText(QCoreApplication.translate("MainWindow", u"Instructions", None))
        self.actionAuthors.setText(QCoreApplication.translate("MainWindow", u"Authors", None))
        self.actionUser.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.actionLibrarian.setText(QCoreApplication.translate("MainWindow", u"Librarian", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"The library system is designed to ensure that the process of location in the library is not tedious and slow.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"(c) Egor Nedospasov, Alya Hasanova", None))
        self.Label.setText("")
        self.Description.setText("")
        self.Photo.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Operations", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Your books", None))
        self.but_Take.setText(QCoreApplication.translate("MainWindow", u"Take", None))
        self.but_Give.setText(QCoreApplication.translate("MainWindow", u"Give", None))
        self.radBut_Name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.radBut_Author.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.radBut_Genre.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        self.radBut_ShowAll.setText(QCoreApplication.translate("MainWindow", u"Show all", None))
        self.but_Printout.setText(QCoreApplication.translate("MainWindow", u"Printout", None))
        self.butLibrarian.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fill your Login and Password", None))
        self.label_Address.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.lab_OptionalData.setText(QCoreApplication.translate("MainWindow", u"Optional Information", None))
        self.label_DateOfBirth.setText(QCoreApplication.translate("MainWindow", u"Date of birth", None))
        self.lab_PersonalData.setText(QCoreApplication.translate("MainWindow", u"Fill your Personal Data", None))
        self.but_Continue.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.but_Enter.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Personal Data of User", None))
        self.but_MakeChanges.setText(QCoreApplication.translate("MainWindow", u"Make Changes", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Result Operations", None))
        self.but_addBook.setText(QCoreApplication.translate("MainWindow", u"Add Book", None))
        self.menuMain.setTitle(QCoreApplication.translate("MainWindow", u"  Main", None))
        self.menuService.setTitle(QCoreApplication.translate("MainWindow", u"Service", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

