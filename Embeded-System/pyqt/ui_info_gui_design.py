# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info-gui-designMEqAEi.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(449, 323)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.getInfoPushButton = QPushButton(self.centralwidget)
        self.getInfoPushButton.setObjectName(u"getInfoPushButton")
        self.getInfoPushButton.setGeometry(QRect(30, 160, 100, 32))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 341, 116))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.hostnameLabel = QLabel(self.widget)
        self.hostnameLabel.setObjectName(u"hostnameLabel")

        self.gridLayout.addWidget(self.hostnameLabel, 0, 0, 1, 1)

        self.hostnameLineEdit = QLineEdit(self.widget)
        self.hostnameLineEdit.setObjectName(u"hostnameLineEdit")

        self.gridLayout.addWidget(self.hostnameLineEdit, 0, 1, 1, 1)

        self.ipLabel = QLabel(self.widget)
        self.ipLabel.setObjectName(u"ipLabel")

        self.gridLayout.addWidget(self.ipLabel, 1, 0, 1, 1)

        self.ipAddressLineEdit = QLineEdit(self.widget)
        self.ipAddressLineEdit.setObjectName(u"ipAddressLineEdit")

        self.gridLayout.addWidget(self.ipAddressLineEdit, 1, 1, 1, 1)

        self.processorLabel = QLabel(self.widget)
        self.processorLabel.setObjectName(u"processorLabel")

        self.gridLayout.addWidget(self.processorLabel, 2, 0, 1, 1)

        self.processorLineEdit = QLineEdit(self.widget)
        self.processorLineEdit.setObjectName(u"processorLineEdit")

        self.gridLayout.addWidget(self.processorLineEdit, 2, 1, 1, 1)

        self.osLabel = QLabel(self.widget)
        self.osLabel.setObjectName(u"osLabel")

        self.gridLayout.addWidget(self.osLabel, 3, 0, 1, 1)

        self.osLineEdit = QLineEdit(self.widget)
        self.osLineEdit.setObjectName(u"osLineEdit")

        self.gridLayout.addWidget(self.osLineEdit, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 449, 43))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TCP Tools for Raspberry Pi", None))
        self.getInfoPushButton.setText(QCoreApplication.translate("MainWindow", u"Get Info", None))
        self.hostnameLabel.setText(QCoreApplication.translate("MainWindow", u"Hostname", None))
        self.ipLabel.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.processorLabel.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.osLabel.setText(QCoreApplication.translate("MainWindow", u"OS", None))
    # retranslateUi

