# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculatorcBRsLr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.resize(296, 310)
        self.label = QLabel(Calculator)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(10, 10, 272, 32))
        self.label.setAcceptDrops(False)
        self.label.setFrameShape(QFrame.Panel)
        self.label.setFrameShadow(QFrame.Sunken)
        self.label.setLineWidth(1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pbCE = QPushButton(Calculator)
        self.pbCE.setObjectName(u"pbCE")
        self.pbCE.setGeometry(QRect(10, 50, 65, 50))
        self.pbClear = QPushButton(Calculator)
        self.pbClear.setObjectName(u"pbClear")
        self.pbClear.setGeometry(QRect(80, 50, 65, 50))
        self.pbDivide = QPushButton(Calculator)
        self.pbDivide.setObjectName(u"pbDivide")
        self.pbDivide.setGeometry(QRect(220, 50, 65, 50))
        self.pbDelete = QPushButton(Calculator)
        self.pbDelete.setObjectName(u"pbDelete")
        self.pbDelete.setGeometry(QRect(150, 50, 65, 50))
        self.pbNum9 = QPushButton(Calculator)
        self.pbNum9.setObjectName(u"pbNum9")
        self.pbNum9.setGeometry(QRect(150, 100, 65, 50))
        self.pbNum7 = QPushButton(Calculator)
        self.pbNum7.setObjectName(u"pbNum7")
        self.pbNum7.setGeometry(QRect(10, 100, 65, 50))
        self.pbNum8 = QPushButton(Calculator)
        self.pbNum8.setObjectName(u"pbNum8")
        self.pbNum8.setGeometry(QRect(80, 100, 65, 50))
        self.pbMultiply = QPushButton(Calculator)
        self.pbMultiply.setObjectName(u"pbMultiply")
        self.pbMultiply.setGeometry(QRect(220, 100, 65, 50))
        self.pbNum4 = QPushButton(Calculator)
        self.pbNum4.setObjectName(u"pbNum4")
        self.pbNum4.setGeometry(QRect(10, 150, 65, 50))
        self.pbNum5 = QPushButton(Calculator)
        self.pbNum5.setObjectName(u"pbNum5")
        self.pbNum5.setGeometry(QRect(80, 150, 65, 50))
        self.pbMinus = QPushButton(Calculator)
        self.pbMinus.setObjectName(u"pbMinus")
        self.pbMinus.setGeometry(QRect(220, 150, 65, 50))
        self.pbNum6 = QPushButton(Calculator)
        self.pbNum6.setObjectName(u"pbNum6")
        self.pbNum6.setGeometry(QRect(150, 150, 65, 50))
        self.pbNum1 = QPushButton(Calculator)
        self.pbNum1.setObjectName(u"pbNum1")
        self.pbNum1.setGeometry(QRect(10, 200, 65, 50))
        self.pbNum1.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pbNum2 = QPushButton(Calculator)
        self.pbNum2.setObjectName(u"pbNum2")
        self.pbNum2.setGeometry(QRect(80, 200, 65, 50))
        self.pbNum3 = QPushButton(Calculator)
        self.pbNum3.setObjectName(u"pbNum3")
        self.pbNum3.setGeometry(QRect(150, 200, 65, 50))
        self.pbPlus = QPushButton(Calculator)
        self.pbPlus.setObjectName(u"pbPlus")
        self.pbPlus.setGeometry(QRect(220, 200, 65, 50))
        self.pbNum0 = QPushButton(Calculator)
        self.pbNum0.setObjectName(u"pbNum0")
        self.pbNum0.setGeometry(QRect(80, 250, 65, 50))
        self.pbSign = QPushButton(Calculator)
        self.pbSign.setObjectName(u"pbSign")
        self.pbSign.setGeometry(QRect(10, 250, 65, 50))
        self.pbDecimalSeparator = QPushButton(Calculator)
        self.pbDecimalSeparator.setObjectName(u"pbDecimalSeparator")
        self.pbDecimalSeparator.setGeometry(QRect(150, 250, 65, 50))
        self.PbExecute = QPushButton(Calculator)
        self.PbExecute.setObjectName(u"PbExecute")
        self.PbExecute.setGeometry(QRect(220, 250, 65, 50))

        self.retranslateUi(Calculator)
        self.pbNum0.clicked.connect(Calculator.pbNumberClicked)
        self.pbNum1.clicked.connect(Calculator.pbNumberClicked)
        self.pbNum2.clicked.connect(Calculator.pbNumberClicked)
        self.pbNum3.clicked.connect(Calculator.pbNumberClicked)
        self.pbNum4.clicked.connect(Calculator.pbNumberClicked)
        self.pbNum8.clicked.connect(Calculator.pbNumberClicked)
        self.pbNum7.clicked.connect(Calculator.pbNumberClicked)
        self.pbNum6.clicked.connect(Calculator.pbNumberClicked)
        self.pbNum5.clicked.connect(Calculator.pbNumberClicked)
        self.pbNum9.clicked.connect(Calculator.pbNumberClicked)
        self.PbExecute.clicked.connect(Calculator.pbExecuteClicked)
        self.pbDivide.clicked.connect(Calculator.pbOperationClicked)
        self.pbPlus.clicked.connect(Calculator.pbOperationClicked)
        self.pbMultiply.clicked.connect(Calculator.pbOperationClicked)
        self.pbMinus.clicked.connect(Calculator.pbOperationClicked)
        self.pbDecimalSeparator.clicked.connect(Calculator.pbDecimalSeparatorClicked)
        self.pbDelete.clicked.connect(Calculator.pbDeleteClicked)
        self.pbClear.clicked.connect(Calculator.pbClearClicked)

        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"Calculator", None))
        self.label.setText("")
        self.pbCE.setText(QCoreApplication.translate("Calculator", u"N/A", None))
        self.pbClear.setText(QCoreApplication.translate("Calculator", u"Clear", None))
        self.pbDivide.setText(QCoreApplication.translate("Calculator", u"/", None))
        self.pbDelete.setText(QCoreApplication.translate("Calculator", u"Del", None))
        self.pbNum9.setText(QCoreApplication.translate("Calculator", u"9", None))
        self.pbNum7.setText(QCoreApplication.translate("Calculator", u"7", None))
        self.pbNum8.setText(QCoreApplication.translate("Calculator", u"8", None))
        self.pbMultiply.setText(QCoreApplication.translate("Calculator", u"*", None))
        self.pbNum4.setText(QCoreApplication.translate("Calculator", u"4", None))
        self.pbNum5.setText(QCoreApplication.translate("Calculator", u"5", None))
        self.pbMinus.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.pbNum6.setText(QCoreApplication.translate("Calculator", u"6", None))
        self.pbNum1.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.pbNum2.setText(QCoreApplication.translate("Calculator", u"2", None))
        self.pbNum3.setText(QCoreApplication.translate("Calculator", u"3", None))
        self.pbPlus.setText(QCoreApplication.translate("Calculator", u"+", None))
        self.pbNum0.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.pbSign.setText(QCoreApplication.translate("Calculator", u"N/A", None))
        self.pbDecimalSeparator.setText(QCoreApplication.translate("Calculator", u".", None))
        self.PbExecute.setText(QCoreApplication.translate("Calculator", u"=", None))
    # retranslateUi

