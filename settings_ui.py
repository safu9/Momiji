# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui',
# licensing of 'settings.ui' applies.
#
# Created: Fri Feb  1 01:03:18 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(207, 178)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.labelFont = QtWidgets.QLabel(self.frame)
        self.labelFont.setObjectName("labelFont")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelFont)
        self.fontComboBox = QtWidgets.QFontComboBox(self.frame)
        self.fontComboBox.setObjectName("fontComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fontComboBox)
        self.labelSize = QtWidgets.QLabel(self.frame)
        self.labelSize.setObjectName("labelSize")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelSize)
        self.spinBoxSize = QtWidgets.QSpinBox(self.frame)
        self.spinBoxSize.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBoxSize.setMinimum(1)
        self.spinBoxSize.setMaximum(50)
        self.spinBoxSize.setProperty("value", 9)
        self.spinBoxSize.setObjectName("spinBoxSize")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxSize)
        self.labelPreview = QtWidgets.QLabel(self.frame)
        self.labelPreview.setObjectName("labelPreview")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelPreview)
        self.labelPreviewFont = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPreviewFont.sizePolicy().hasHeightForWidth())
        self.labelPreviewFont.setSizePolicy(sizePolicy)
        self.labelPreviewFont.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelPreviewFont.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelPreviewFont.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPreviewFont.setMargin(4)
        self.labelPreviewFont.setObjectName("labelPreviewFont")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelPreviewFont)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.labelFont.setText(QtWidgets.QApplication.translate("Dialog", "Font", None, -1))
        self.labelSize.setText(QtWidgets.QApplication.translate("Dialog", "Size", None, -1))
        self.labelPreview.setText(QtWidgets.QApplication.translate("Dialog", "Preview", None, -1))
        self.labelPreviewFont.setText(QtWidgets.QApplication.translate("Dialog", "AaBbCc123", None, -1))

