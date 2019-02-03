# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/window.ui',
# licensing of 'ui/window.ui' applies.
#
# Created: Sun Feb  3 04:17:22 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QtCore.QSize(400, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textEdit = TextEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_4.addWidget(self.textEdit)
        self.verticalLayout.addWidget(self.frame)
        self.frameFindBox = QtWidgets.QFrame(self.centralwidget)
        self.frameFindBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFindBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameFindBox.setObjectName("frameFindBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameFindBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frameFindSettings = QtWidgets.QFrame(self.frameFindBox)
        self.frameFindSettings.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameFindSettings.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameFindSettings.setObjectName("frameFindSettings")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameFindSettings)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonCloseFind = QtWidgets.QToolButton(self.frameFindSettings)
        self.buttonCloseFind.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonCloseFind.setStyleSheet("QToolButton { border: none; }")
        self.buttonCloseFind.setIconSize(QtCore.QSize(8, 8))
        self.buttonCloseFind.setShortcut("Esc")
        self.buttonCloseFind.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.buttonCloseFind.setArrowType(QtCore.Qt.DownArrow)
        self.buttonCloseFind.setObjectName("buttonCloseFind")
        self.horizontalLayout_2.addWidget(self.buttonCloseFind)
        self.labelFindResult = QtWidgets.QLabel(self.frameFindSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelFindResult.sizePolicy().hasHeightForWidth())
        self.labelFindResult.setSizePolicy(sizePolicy)
        self.labelFindResult.setText("")
        self.labelFindResult.setObjectName("labelFindResult")
        self.horizontalLayout_2.addWidget(self.labelFindResult)
        self.buttonCase = QtWidgets.QPushButton(self.frameFindSettings)
        self.buttonCase.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonCase.setCheckable(True)
        self.buttonCase.setObjectName("buttonCase")
        self.horizontalLayout_2.addWidget(self.buttonCase)
        self.buttonWords = QtWidgets.QPushButton(self.frameFindSettings)
        self.buttonWords.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonWords.setCheckable(True)
        self.buttonWords.setObjectName("buttonWords")
        self.horizontalLayout_2.addWidget(self.buttonWords)
        self.buttonRegex = QtWidgets.QPushButton(self.frameFindSettings)
        self.buttonRegex.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonRegex.setCheckable(True)
        self.buttonRegex.setObjectName("buttonRegex")
        self.horizontalLayout_2.addWidget(self.buttonRegex)
        self.verticalLayout_2.addWidget(self.frameFindSettings)
        self.frameFind = QtWidgets.QFrame(self.frameFindBox)
        self.frameFind.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameFind.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameFind.setObjectName("frameFind")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameFind)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editFind = QtWidgets.QLineEdit(self.frameFind)
        self.editFind.setObjectName("editFind")
        self.horizontalLayout.addWidget(self.editFind)
        self.buttonFind = QtWidgets.QPushButton(self.frameFind)
        self.buttonFind.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonFind.setObjectName("buttonFind")
        self.horizontalLayout.addWidget(self.buttonFind)
        self.buttonFindAll = QtWidgets.QPushButton(self.frameFind)
        self.buttonFindAll.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonFindAll.setObjectName("buttonFindAll")
        self.horizontalLayout.addWidget(self.buttonFindAll)
        self.verticalLayout_2.addWidget(self.frameFind)
        self.frameReplace = QtWidgets.QFrame(self.frameFindBox)
        self.frameReplace.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameReplace.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameReplace.setObjectName("frameReplace")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameReplace)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.editReplace = QtWidgets.QLineEdit(self.frameReplace)
        self.editReplace.setObjectName("editReplace")
        self.horizontalLayout_3.addWidget(self.editReplace)
        self.buttonReplace = QtWidgets.QPushButton(self.frameReplace)
        self.buttonReplace.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonReplace.setObjectName("buttonReplace")
        self.horizontalLayout_3.addWidget(self.buttonReplace)
        self.buttonReplaceAll = QtWidgets.QPushButton(self.frameReplace)
        self.buttonReplaceAll.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonReplaceAll.setObjectName("buttonReplaceAll")
        self.horizontalLayout_3.addWidget(self.buttonReplaceAll)
        self.verticalLayout_2.addWidget(self.frameReplace)
        self.verticalLayout.addWidget(self.frameFindBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFind = QtWidgets.QMenu(self.menubar)
        self.menuFind.setObjectName("menuFind")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewFile = QtWidgets.QAction(MainWindow)
        self.actionNewFile.setShortcut("Ctrl+N")
        self.actionNewFile.setObjectName("actionNewFile")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setShortcut("Ctrl+Shift+S")
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setShortcut("Ctrl+Z")
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setShortcut("Ctrl+Y")
        self.actionRedo.setObjectName("actionRedo")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setShortcut("Ctrl+C")
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setShortcut("Ctrl+X")
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setShortcut("Ctrl+V")
        self.actionPaste.setObjectName("actionPaste")
        self.actionSelectAll = QtWidgets.QAction(MainWindow)
        self.actionSelectAll.setShortcut("Ctrl+A")
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setShortcut("Ctrl+F")
        self.actionFind.setObjectName("actionFind")
        self.actionFindNext = QtWidgets.QAction(MainWindow)
        self.actionFindNext.setShortcut("F3")
        self.actionFindNext.setObjectName("actionFindNext")
        self.actionFindPrevious = QtWidgets.QAction(MainWindow)
        self.actionFindPrevious.setShortcut("Shift+F3")
        self.actionFindPrevious.setObjectName("actionFindPrevious")
        self.actionFindAll = QtWidgets.QAction(MainWindow)
        self.actionFindAll.setObjectName("actionFindAll")
        self.actionReplace = QtWidgets.QAction(MainWindow)
        self.actionReplace.setShortcut("Ctrl+R")
        self.actionReplace.setObjectName("actionReplace")
        self.actionReplaceNext = QtWidgets.QAction(MainWindow)
        self.actionReplaceNext.setObjectName("actionReplaceNext")
        self.actionReplaceAll = QtWidgets.QAction(MainWindow)
        self.actionReplaceAll.setObjectName("actionReplaceAll")
        self.actionFindSelectNext = QtWidgets.QAction(MainWindow)
        self.actionFindSelectNext.setEnabled(False)
        self.actionFindSelectNext.setShortcut("Ctrl+D")
        self.actionFindSelectNext.setObjectName("actionFindSelectNext")
        self.actionFindSelectAll = QtWidgets.QAction(MainWindow)
        self.actionFindSelectAll.setEnabled(False)
        self.actionFindSelectAll.setObjectName("actionFindSelectAll")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setShortcut("Ctrl+,")
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionNewFile)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionSelectAll)
        self.menuFind.addAction(self.actionFind)
        self.menuFind.addAction(self.actionFindNext)
        self.menuFind.addAction(self.actionFindPrevious)
        self.menuFind.addAction(self.actionFindAll)
        self.menuFind.addSeparator()
        self.menuFind.addAction(self.actionReplace)
        self.menuFind.addAction(self.actionReplaceNext)
        self.menuFind.addAction(self.actionReplaceAll)
        self.menuFind.addSeparator()
        self.menuFind.addAction(self.actionFindSelectNext)
        self.menuFind.addAction(self.actionFindSelectAll)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFind.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.buttonCloseFind.setText(QtWidgets.QApplication.translate("MainWindow", "Find", None, -1))
        self.buttonCase.setText(QtWidgets.QApplication.translate("MainWindow", "Match Case", None, -1))
        self.buttonWords.setText(QtWidgets.QApplication.translate("MainWindow", "Whole Words", None, -1))
        self.buttonRegex.setText(QtWidgets.QApplication.translate("MainWindow", "Use Regex", None, -1))
        self.editFind.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Find string", None, -1))
        self.buttonFind.setText(QtWidgets.QApplication.translate("MainWindow", "Find", None, -1))
        self.buttonFindAll.setText(QtWidgets.QApplication.translate("MainWindow", "Find All", None, -1))
        self.editReplace.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Replace string", None, -1))
        self.buttonReplace.setText(QtWidgets.QApplication.translate("MainWindow", "Replace", None, -1))
        self.buttonReplaceAll.setText(QtWidgets.QApplication.translate("MainWindow", "Replace All", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File(&F)", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help(&H)", None, -1))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit(&E)", None, -1))
        self.menuFind.setTitle(QtWidgets.QApplication.translate("MainWindow", "Find(&I)", None, -1))
        self.actionNewFile.setText(QtWidgets.QApplication.translate("MainWindow", "New File", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "Open...", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.actionSaveAs.setText(QtWidgets.QApplication.translate("MainWindow", "Save As...", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.actionUndo.setText(QtWidgets.QApplication.translate("MainWindow", "Undo", None, -1))
        self.actionRedo.setText(QtWidgets.QApplication.translate("MainWindow", "Redo", None, -1))
        self.actionCopy.setText(QtWidgets.QApplication.translate("MainWindow", "Copy", None, -1))
        self.actionCut.setText(QtWidgets.QApplication.translate("MainWindow", "Cut", None, -1))
        self.actionPaste.setText(QtWidgets.QApplication.translate("MainWindow", "Paste", None, -1))
        self.actionSelectAll.setText(QtWidgets.QApplication.translate("MainWindow", "Select All", None, -1))
        self.actionFind.setText(QtWidgets.QApplication.translate("MainWindow", "Find", None, -1))
        self.actionFindNext.setText(QtWidgets.QApplication.translate("MainWindow", "Find Next", None, -1))
        self.actionFindPrevious.setText(QtWidgets.QApplication.translate("MainWindow", "Find Previous", None, -1))
        self.actionFindAll.setText(QtWidgets.QApplication.translate("MainWindow", "Find All", None, -1))
        self.actionReplace.setText(QtWidgets.QApplication.translate("MainWindow", "Replace", None, -1))
        self.actionReplaceNext.setText(QtWidgets.QApplication.translate("MainWindow", "Replace Next", None, -1))
        self.actionReplaceAll.setText(QtWidgets.QApplication.translate("MainWindow", "Replace All", None, -1))
        self.actionFindSelectNext.setText(QtWidgets.QApplication.translate("MainWindow", "Select Next", None, -1))
        self.actionFindSelectAll.setText(QtWidgets.QApplication.translate("MainWindow", "Select All", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About Momiji", None, -1))
        self.actionSettings.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))

from widget.textedit import TextEdit
