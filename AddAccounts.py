# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddAccounts.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem)

class Ui_AddAccounts(object):
    def setupUi(self, AddAccounts):
        if not AddAccounts.objectName():
            AddAccounts.setObjectName(u"AddAccounts")
        AddAccounts.resize(740, 779)
        AddAccounts.setMinimumSize(QSize(740, 720))
        AddAccounts.setStyleSheet(u"font: 57 10pt \"Yu Gothic Medium\";")
        self.gridLayout = QGridLayout(AddAccounts)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(AddAccounts)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.spotify = QTableWidget(AddAccounts)
        if (self.spotify.columnCount() < 5):
            self.spotify.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.spotify.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.spotify.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.spotify.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.spotify.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.spotify.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.spotify.setObjectName(u"spotify")
        self.spotify.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.spotify.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.spotify, 3, 0, 1, 2)

        self.import_spotify = QPushButton(AddAccounts)
        self.import_spotify.setObjectName(u"import_spotify")
        self.import_spotify.setMinimumSize(QSize(150, 35))

        self.gridLayout.addWidget(self.import_spotify, 4, 1, 1, 1, Qt.AlignRight)

        self.import_google = QPushButton(AddAccounts)
        self.import_google.setObjectName(u"import_google")
        self.import_google.setMinimumSize(QSize(150, 35))

        self.gridLayout.addWidget(self.import_google, 6, 1, 1, 1, Qt.AlignRight)

        self.google = QTableWidget(AddAccounts)
        if (self.google.columnCount() < 2):
            self.google.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.google.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.google.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.google.setObjectName(u"google")
        self.google.setMinimumSize(QSize(0, 0))
        self.google.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.google.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.google, 5, 0, 1, 2)

        self.label = QLabel(AddAccounts)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)

        self.label_2 = QLabel(AddAccounts)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.import_twitch = QPushButton(AddAccounts)
        self.import_twitch.setObjectName(u"import_twitch")
        self.import_twitch.setMinimumSize(QSize(150, 35))

        self.gridLayout.addWidget(self.import_twitch, 2, 1, 1, 1, Qt.AlignRight)

        self.twitch = QTableWidget(AddAccounts)
        if (self.twitch.columnCount() < 6):
            self.twitch.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.twitch.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.twitch.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.twitch.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.twitch.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.twitch.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.twitch.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        self.twitch.setObjectName(u"twitch")
        self.twitch.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.twitch.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.twitch, 1, 0, 1, 2)


        self.retranslateUi(AddAccounts)

        QMetaObject.connectSlotsByName(AddAccounts)
    # setupUi

    def retranslateUi(self, AddAccounts):
        AddAccounts.setWindowTitle(QCoreApplication.translate("AddAccounts", u"Add Accounts", None))
        self.label_3.setText(QCoreApplication.translate("AddAccounts", u"Spotify Accounts", None))
        ___qtablewidgetitem = self.spotify.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddAccounts", u"Email Address", None));
        ___qtablewidgetitem1 = self.spotify.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AddAccounts", u"Password", None));
        ___qtablewidgetitem2 = self.spotify.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AddAccounts", u"Email Password", None));
        ___qtablewidgetitem3 = self.spotify.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AddAccounts", u"Email Host", None));
        ___qtablewidgetitem4 = self.spotify.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AddAccounts", u"Email Port", None));
        self.import_spotify.setText(QCoreApplication.translate("AddAccounts", u"Import Text File", None))
        self.import_google.setText(QCoreApplication.translate("AddAccounts", u"Import Text File", None))
        ___qtablewidgetitem5 = self.google.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AddAccounts", u"Email Address", None));
        ___qtablewidgetitem6 = self.google.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AddAccounts", u"Email Password", None));
        self.label.setText(QCoreApplication.translate("AddAccounts", u"Google Accounts", None))
        self.label_2.setText(QCoreApplication.translate("AddAccounts", u"Twitch Accounts:", None))
        self.import_twitch.setText(QCoreApplication.translate("AddAccounts", u"Import Text File", None))
        ___qtablewidgetitem7 = self.twitch.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AddAccounts", u"Username", None));
        ___qtablewidgetitem8 = self.twitch.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AddAccounts", u"Password", None));
        ___qtablewidgetitem9 = self.twitch.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("AddAccounts", u"Email Address", None));
        ___qtablewidgetitem10 = self.twitch.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("AddAccounts", u"Email Password", None));
        ___qtablewidgetitem11 = self.twitch.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("AddAccounts", u"Email Host", None));
        ___qtablewidgetitem12 = self.twitch.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("AddAccounts", u"Email Port", None));
    # retranslateUi

