# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddDevice.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout)

class Ui_AddDevice(object):
    def setupUi(self, AddDevice):
        if not AddDevice.objectName():
            AddDevice.setObjectName(u"AddDevice")
        AddDevice.resize(570, 450)
        AddDevice.setMaximumSize(QSize(570, 450))
        AddDevice.setStyleSheet(u"font: 57 10pt \"Yu Gothic Medium\";")
        self.horizontalLayout = QHBoxLayout(AddDevice)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AddDevice)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.devices = QListWidget(AddDevice)
        self.devices.setObjectName(u"devices")
        self.devices.setMaximumSize(QSize(270, 16777215))

        self.verticalLayout.addWidget(self.devices)

        self.refresh = QPushButton(AddDevice)
        self.refresh.setObjectName(u"refresh")
        self.refresh.setMinimumSize(QSize(150, 35))

        self.verticalLayout.addWidget(self.refresh, 0, Qt.AlignRight)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.select_by_number = QCheckBox(AddDevice)
        self.select_by_number.setObjectName(u"select_by_number")

        self.verticalLayout_2.addWidget(self.select_by_number)

        self.number = QSpinBox(AddDevice)
        self.number.setObjectName(u"number")
        self.number.setEnabled(False)
        self.number.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.number)

        self.select_all = QPushButton(AddDevice)
        self.select_all.setObjectName(u"select_all")
        self.select_all.setMinimumSize(QSize(150, 35))

        self.verticalLayout_2.addWidget(self.select_all)

        self.deselect_all = QPushButton(AddDevice)
        self.deselect_all.setObjectName(u"deselect_all")
        self.deselect_all.setMinimumSize(QSize(150, 35))

        self.verticalLayout_2.addWidget(self.deselect_all)

        self.groupBox = QGroupBox(AddDevice)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.emus = QSpinBox(self.groupBox)
        self.emus.setObjectName(u"emus")
        self.emus.setEnabled(True)
        self.emus.setMinimumSize(QSize(0, 25))
        self.emus.setMinimum(0)
        self.emus.setMaximum(1000000000)
        self.emus.setValue(0)

        self.verticalLayout_3.addWidget(self.emus)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.save = QPushButton(AddDevice)
        self.save.setObjectName(u"save")
        self.save.setMinimumSize(QSize(150, 35))

        self.verticalLayout_2.addWidget(self.save, 0, Qt.AlignRight)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(AddDevice)

        QMetaObject.connectSlotsByName(AddDevice)
    # setupUi

    def retranslateUi(self, AddDevice):
        AddDevice.setWindowTitle(QCoreApplication.translate("AddDevice", u"Add Devices", None))
        self.label.setText(QCoreApplication.translate("AddDevice", u"List Of Connected Devices:", None))
        self.refresh.setText(QCoreApplication.translate("AddDevice", u"Refresh", None))
        self.select_by_number.setText(QCoreApplication.translate("AddDevice", u"Select By Number", None))
        self.select_all.setText(QCoreApplication.translate("AddDevice", u"Select All", None))
        self.deselect_all.setText(QCoreApplication.translate("AddDevice", u"Deselect All", None))
        self.groupBox.setTitle(QCoreApplication.translate("AddDevice", u"Add Emulators:", None))
        self.label_2.setText(QCoreApplication.translate("AddDevice", u"Amount:", None))
        self.save.setText(QCoreApplication.translate("AddDevice", u"Save", None))
    # retranslateUi

