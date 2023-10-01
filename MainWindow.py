# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1094, 870)
        MainWindow.setStyleSheet(u"font: 57 10pt \"Yu Gothic Medium\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.device_page = QWidget()
        self.device_page.setObjectName(u"device_page")
        self.verticalLayout_2 = QVBoxLayout(self.device_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.device_page)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.line = QFrame(self.device_page)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.horizontalLayout.addWidget(self.line)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.check_twitch_device = QCheckBox(self.device_page)
        self.check_twitch_device.setObjectName(u"check_twitch_device")

        self.verticalLayout_2.addWidget(self.check_twitch_device)

        self.twitch_devices = QTableWidget(self.device_page)
        if (self.twitch_devices.columnCount() < 5):
            self.twitch_devices.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.twitch_devices.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.twitch_devices.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.twitch_devices.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.twitch_devices.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.twitch_devices.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.twitch_devices.setObjectName(u"twitch_devices")
        self.twitch_devices.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.twitch_devices.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_2.addWidget(self.twitch_devices)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.remove_twitch_device = QPushButton(self.device_page)
        self.remove_twitch_device.setObjectName(u"remove_twitch_device")
        self.remove_twitch_device.setMinimumSize(QSize(180, 35))

        self.horizontalLayout_3.addWidget(self.remove_twitch_device)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.add_twitch_devices = QPushButton(self.device_page)
        self.add_twitch_devices.setObjectName(u"add_twitch_devices")
        self.add_twitch_devices.setMinimumSize(QSize(100, 35))

        self.horizontalLayout_3.addWidget(self.add_twitch_devices)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.device_page)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_2 = QFrame(self.device_page)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QFrame.HLine)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.check_spotify_device = QCheckBox(self.device_page)
        self.check_spotify_device.setObjectName(u"check_spotify_device")

        self.verticalLayout_2.addWidget(self.check_spotify_device)

        self.spotify_devices = QTableWidget(self.device_page)
        if (self.spotify_devices.columnCount() < 5):
            self.spotify_devices.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.spotify_devices.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.spotify_devices.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.spotify_devices.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.spotify_devices.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.spotify_devices.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.spotify_devices.setObjectName(u"spotify_devices")
        self.spotify_devices.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.spotify_devices.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_2.addWidget(self.spotify_devices)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.remove_spotify_devices = QPushButton(self.device_page)
        self.remove_spotify_devices.setObjectName(u"remove_spotify_devices")
        self.remove_spotify_devices.setMinimumSize(QSize(180, 35))

        self.horizontalLayout_4.addWidget(self.remove_spotify_devices)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.add_spotify_devices = QPushButton(self.device_page)
        self.add_spotify_devices.setObjectName(u"add_spotify_devices")
        self.add_spotify_devices.setMinimumSize(QSize(100, 35))

        self.horizontalLayout_4.addWidget(self.add_spotify_devices)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.device_page, "")
        self.account_management_page = QWidget()
        self.account_management_page.setObjectName(u"account_management_page")
        self.gridLayout_3 = QGridLayout(self.account_management_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.ac_twitch_devices = QListWidget(self.account_management_page)
        self.ac_twitch_devices.setObjectName(u"ac_twitch_devices")
        self.ac_twitch_devices.setMinimumSize(QSize(340, 0))
        self.ac_twitch_devices.setMaximumSize(QSize(340, 16777215))

        self.gridLayout.addWidget(self.ac_twitch_devices, 1, 0, 1, 2)

        self.add_accounts_to_devices = QPushButton(self.account_management_page)
        self.add_accounts_to_devices.setObjectName(u"add_accounts_to_devices")
        self.add_accounts_to_devices.setMinimumSize(QSize(120, 35))

        self.gridLayout.addWidget(self.add_accounts_to_devices, 4, 0, 1, 2)

        self.ac_spotify_devices = QListWidget(self.account_management_page)
        self.ac_spotify_devices.setObjectName(u"ac_spotify_devices")
        self.ac_spotify_devices.setMinimumSize(QSize(340, 0))
        self.ac_spotify_devices.setMaximumSize(QSize(340, 16777215))

        self.gridLayout.addWidget(self.ac_spotify_devices, 3, 0, 1, 1)

        self.select_twitch_devices = QCheckBox(self.account_management_page)
        self.select_twitch_devices.setObjectName(u"select_twitch_devices")

        self.gridLayout.addWidget(self.select_twitch_devices, 0, 0, 1, 1)

        self.select_spotify_devices = QCheckBox(self.account_management_page)
        self.select_spotify_devices.setObjectName(u"select_spotify_devices")

        self.gridLayout.addWidget(self.select_spotify_devices, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spotify_accounts = QTableWidget(self.account_management_page)
        if (self.spotify_accounts.columnCount() < 1):
            self.spotify_accounts.setColumnCount(1)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.spotify_accounts.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        self.spotify_accounts.setObjectName(u"spotify_accounts")
        self.spotify_accounts.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.spotify_accounts.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_2.addWidget(self.spotify_accounts, 4, 0, 1, 1)

        self.remove_twitch_accounts = QPushButton(self.account_management_page)
        self.remove_twitch_accounts.setObjectName(u"remove_twitch_accounts")
        self.remove_twitch_accounts.setMinimumSize(QSize(180, 35))

        self.gridLayout_2.addWidget(self.remove_twitch_accounts, 2, 0, 1, 1, Qt.AlignRight)

        self.remove_google_accounts = QPushButton(self.account_management_page)
        self.remove_google_accounts.setObjectName(u"remove_google_accounts")
        self.remove_google_accounts.setMinimumSize(QSize(180, 35))

        self.gridLayout_2.addWidget(self.remove_google_accounts, 8, 0, 1, 1, Qt.AlignRight)

        self.google_accounts = QTableWidget(self.account_management_page)
        if (self.google_accounts.columnCount() < 1):
            self.google_accounts.setColumnCount(1)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.google_accounts.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        self.google_accounts.setObjectName(u"google_accounts")
        self.google_accounts.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.google_accounts.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_2.addWidget(self.google_accounts, 7, 0, 1, 1)

        self.twitch_accounts = QTableWidget(self.account_management_page)
        if (self.twitch_accounts.columnCount() < 1):
            self.twitch_accounts.setColumnCount(1)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.twitch_accounts.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        self.twitch_accounts.setObjectName(u"twitch_accounts")
        self.twitch_accounts.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.twitch_accounts.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_2.addWidget(self.twitch_accounts, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.spotify_check = QCheckBox(self.account_management_page)
        self.spotify_check.setObjectName(u"spotify_check")

        self.horizontalLayout_7.addWidget(self.spotify_check)

        self.line_5 = QFrame(self.account_management_page)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(1)
        self.line_5.setFrameShape(QFrame.HLine)

        self.horizontalLayout_7.addWidget(self.line_5)

        self.horizontalLayout_7.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.twitch_check = QCheckBox(self.account_management_page)
        self.twitch_check.setObjectName(u"twitch_check")

        self.horizontalLayout_6.addWidget(self.twitch_check)

        self.line_4 = QFrame(self.account_management_page)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(1)
        self.line_4.setFrameShape(QFrame.HLine)

        self.horizontalLayout_6.addWidget(self.line_4)

        self.horizontalLayout_6.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.remove_spotify_accounts = QPushButton(self.account_management_page)
        self.remove_spotify_accounts.setObjectName(u"remove_spotify_accounts")
        self.remove_spotify_accounts.setMinimumSize(QSize(180, 35))

        self.gridLayout_2.addWidget(self.remove_spotify_accounts, 5, 0, 1, 1, Qt.AlignRight)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.google_check = QCheckBox(self.account_management_page)
        self.google_check.setObjectName(u"google_check")

        self.horizontalLayout_9.addWidget(self.google_check)

        self.line_6 = QFrame(self.account_management_page)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(1)
        self.line_6.setFrameShape(QFrame.HLine)

        self.horizontalLayout_9.addWidget(self.line_6)

        self.horizontalLayout_9.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_9, 6, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(1, 1)
        self.tabWidget.addTab(self.account_management_page, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.spotify_links = QPlainTextEdit(self.tab)
        self.spotify_links.setObjectName(u"spotify_links")
        self.spotify_links.setMinimumSize(QSize(350, 0))
        self.spotify_links.setMaximumSize(QSize(16777215, 16777215))
        self.spotify_links.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.verticalLayout_4.addWidget(self.spotify_links)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.proxies = QPlainTextEdit(self.tab)
        self.proxies.setObjectName(u"proxies")
        self.proxies.setMinimumSize(QSize(350, 0))
        self.proxies.setMaximumSize(QSize(16777215, 16777215))
        self.proxies.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.verticalLayout_6.addWidget(self.proxies)


        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 1, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_10.addWidget(self.label_11)

        self.twitter_links = QPlainTextEdit(self.tab)
        self.twitter_links.setObjectName(u"twitter_links")
        self.twitter_links.setMinimumSize(QSize(350, 0))
        self.twitter_links.setMaximumSize(QSize(16777215, 16777215))
        self.twitter_links.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.verticalLayout_10.addWidget(self.twitter_links)


        self.gridLayout_4.addLayout(self.verticalLayout_10, 0, 2, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_13.addWidget(self.label_14)

        self.twitch_profiles = QPlainTextEdit(self.tab)
        self.twitch_profiles.setObjectName(u"twitch_profiles")
        self.twitch_profiles.setMinimumSize(QSize(350, 0))
        self.twitch_profiles.setMaximumSize(QSize(16777215, 16777215))
        self.twitch_profiles.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.verticalLayout_13.addWidget(self.twitch_profiles)


        self.gridLayout_4.addLayout(self.verticalLayout_13, 1, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.line_7 = QFrame(self.tab)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setFrameShape(QFrame.HLine)

        self.horizontalLayout_11.addWidget(self.line_7)

        self.horizontalLayout_11.setStretch(1, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_12.addWidget(self.label_7)

        self.spot_min = QSpinBox(self.groupBox)
        self.spot_min.setObjectName(u"spot_min")
        self.spot_min.setMinimumSize(QSize(0, 25))
        self.spot_min.setMinimum(20)
        self.spot_min.setMaximum(1000000000)

        self.horizontalLayout_12.addWidget(self.spot_min)

        self.line_8 = QFrame(self.groupBox)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMinimumSize(QSize(10, 0))
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setFrameShape(QFrame.HLine)

        self.horizontalLayout_12.addWidget(self.line_8)

        self.spot_max = QSpinBox(self.groupBox)
        self.spot_max.setObjectName(u"spot_max")
        self.spot_max.setMinimumSize(QSize(0, 25))
        self.spot_max.setMaximum(1000000000)
        self.spot_max.setValue(30)

        self.horizontalLayout_12.addWidget(self.spot_max)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_12.addWidget(self.label_8)

        self.horizontalLayout_12.setStretch(1, 2)
        self.horizontalLayout_12.setStretch(3, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_14.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_13.addWidget(self.label_9)

        self.twit_min = QSpinBox(self.groupBox_2)
        self.twit_min.setObjectName(u"twit_min")
        self.twit_min.setMinimumSize(QSize(0, 25))
        self.twit_min.setMinimum(20)
        self.twit_min.setMaximum(1000000000)

        self.horizontalLayout_13.addWidget(self.twit_min)

        self.line_9 = QFrame(self.groupBox_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setMinimumSize(QSize(10, 0))
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setFrameShape(QFrame.HLine)

        self.horizontalLayout_13.addWidget(self.line_9)

        self.twit_max = QSpinBox(self.groupBox_2)
        self.twit_max.setObjectName(u"twit_max")
        self.twit_max.setMinimumSize(QSize(0, 25))
        self.twit_max.setMaximum(1000000000)
        self.twit_max.setValue(30)

        self.horizontalLayout_13.addWidget(self.twit_max)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_13.addWidget(self.label_10)

        self.horizontalLayout_13.setStretch(1, 2)
        self.horizontalLayout_13.setStretch(3, 2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_14.addWidget(self.groupBox_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)

        self.tabWidget.addTab(self.tab, "")
        self.preview_tab = QWidget()
        self.preview_tab.setObjectName(u"preview_tab")
        self.verticalLayout_3 = QVBoxLayout(self.preview_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.running_devices = QLabel(self.preview_tab)
        self.running_devices.setObjectName(u"running_devices")

        self.horizontalLayout_8.addWidget(self.running_devices)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.start = QPushButton(self.preview_tab)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(180, 35))

        self.horizontalLayout_8.addWidget(self.start)

        self.stop = QPushButton(self.preview_tab)
        self.stop.setObjectName(u"stop")
        self.stop.setMinimumSize(QSize(180, 35))

        self.horizontalLayout_8.addWidget(self.stop)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.logs = QPlainTextEdit(self.preview_tab)
        self.logs.setObjectName(u"logs")
        self.logs.setMaximumSize(QSize(16777215, 16777215))
        self.logs.setStyleSheet(u"QPlainTextEdit{\n"
"	background: black;\n"
"	border: 0;\n"
"	font-size: 15px;\n"
"}")
        self.logs.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.logs.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.logs)

        self.tabWidget.addTab(self.preview_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mobile Bot", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Twitch Category:", None))
        self.check_twitch_device.setText(QCoreApplication.translate("MainWindow", u"Check/Uncheck All", None))
        ___qtablewidgetitem = self.twitch_devices.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem1 = self.twitch_devices.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem2 = self.twitch_devices.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem3 = self.twitch_devices.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Success", None));
        ___qtablewidgetitem4 = self.twitch_devices.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Fails", None));
        self.remove_twitch_device.setText(QCoreApplication.translate("MainWindow", u"Remove Selected", None))
        self.add_twitch_devices.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Spotify Category:", None))
        self.check_spotify_device.setText(QCoreApplication.translate("MainWindow", u"Check/Uncheck All", None))
        ___qtablewidgetitem5 = self.spotify_devices.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem6 = self.spotify_devices.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem7 = self.spotify_devices.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem8 = self.spotify_devices.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Success", None));
        ___qtablewidgetitem9 = self.spotify_devices.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Fails", None));
        self.remove_spotify_devices.setText(QCoreApplication.translate("MainWindow", u"Remove Selected", None))
        self.add_spotify_devices.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.device_page), QCoreApplication.translate("MainWindow", u"Devices", None))
        self.add_accounts_to_devices.setText(QCoreApplication.translate("MainWindow", u"Add Accounts To Selected Devices", None))
        self.select_twitch_devices.setText(QCoreApplication.translate("MainWindow", u"Twitch Devices:", None))
        self.select_spotify_devices.setText(QCoreApplication.translate("MainWindow", u"Spotify Devices:", None))
        ___qtablewidgetitem10 = self.spotify_accounts.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.remove_twitch_accounts.setText(QCoreApplication.translate("MainWindow", u"Remove Selected", None))
        self.remove_google_accounts.setText(QCoreApplication.translate("MainWindow", u"Remove Selected", None))
        ___qtablewidgetitem11 = self.google_accounts.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem12 = self.twitch_accounts.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.spotify_check.setText(QCoreApplication.translate("MainWindow", u"Spotify Account:", None))
        self.twitch_check.setText(QCoreApplication.translate("MainWindow", u"Twitch Accounts:", None))
        self.remove_spotify_accounts.setText(QCoreApplication.translate("MainWindow", u"Remove Selected", None))
        self.google_check.setText(QCoreApplication.translate("MainWindow", u"Google Account:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.account_management_page), QCoreApplication.translate("MainWindow", u"Accounts Management", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Spotify Links:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Proxy List:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Twitter links:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Twitch Profiles:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Settings:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Spotify:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Stream Time:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Seconds", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Twitch:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Stream Time:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Seconds", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.running_devices.setText(QCoreApplication.translate("MainWindow", u"Running Devices: 0/0", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.preview_tab), QCoreApplication.translate("MainWindow", u"Preview", None))
    # retranslateUi

