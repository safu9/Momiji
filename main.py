import os
import sys

import chardet
from PySide2.QtCore import QLocale, QObject, QRegExp, QSettings, QTranslator
from PySide2.QtGui import QColor, QFont, QIcon, QTextCursor, QTextDocument
from PySide2.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow, QMessageBox, QStyle, QTextEdit

from settingsdialog import SettingsDialog
from syntaxhighlight import SyntaxHighlighter
from ui.window import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Load UI File
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Settings
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, 'Momiji', 'Momiji')

        # Menu
        self.ui.actionNewFile.triggered.connect(self.onNewFileClick)
        self.ui.actionOpen.triggered.connect(self.onOpenClick)
        self.ui.actionSave.triggered.connect(self.onSaveClick)
        self.ui.actionSaveAs.triggered.connect(self.onSaveAsClick)
        self.ui.actionSettings.triggered.connect(self.onSettingsClick)
        self.ui.actionExit.triggered.connect(self.onExitClick)

        self.ui.actionUndo.triggered.connect(self.ui.textEdit.undo)
        self.ui.actionRedo.triggered.connect(self.ui.textEdit.redo)
        self.ui.actionCopy.triggered.connect(self.ui.textEdit.copy)
        self.ui.actionCut.triggered.connect(self.ui.textEdit.cut)
        self.ui.actionPaste.triggered.connect(self.ui.textEdit.paste)
        self.ui.actionSelectAll.triggered.connect(self.ui.textEdit.selectAll)

        self.ui.actionFind.triggered.connect(self.onFindClick)
        self.ui.actionFindNext.triggered.connect(self.onFindNextClick)
        self.ui.actionFindPrevious.triggered.connect(self.onFindPreviousClick)
        self.ui.actionFindAll.triggered.connect(self.onFindAllClick)
        self.ui.actionReplace.triggered.connect(self.onReplaceClick)
        self.ui.actionReplaceNext.triggered.connect(self.onReplaceNextClick)
        self.ui.actionReplaceAll.triggered.connect(self.onReplaceAllClick)
        self.ui.actionFindSelectNext.triggered.connect(self.onFindSelectNextClick)
        self.ui.actionFindSelectAll.triggered.connect(self.onFindSelectAllClick)

        self.ui.actionAbout.triggered.connect(self.onAboutClick)

        self.ui.textEdit.undoAvailable.connect(self.ui.actionUndo.setEnabled)
        self.ui.textEdit.redoAvailable.connect(self.ui.actionRedo.setEnabled)
        self.ui.textEdit.copyAvailable.connect(self.ui.actionCopy.setEnabled)
        self.ui.textEdit.copyAvailable.connect(self.ui.actionCut.setEnabled)
        self.ui.textEdit.modificationChanged.connect(self.setTitle)

        self.ui.actionUndo.setEnabled(False)
        self.ui.actionRedo.setEnabled(False)
        self.ui.actionCopy.setEnabled(False)
        self.ui.actionCut.setEnabled(False)

        # Editor
        font = QFont()
        font.setFamily(self.settings.value('editor/font', font.defaultFamily()))
        font.setPointSize(int(self.settings.value('editor/size', 9)))
        self.ui.textEdit.setFont(font)

        self.highlighter = SyntaxHighlighter(self.ui.textEdit.document())

        # Find box
        self.ui.buttonCloseFind.clicked.connect(self.onCloseFindClicked)
        self.ui.buttonFind.clicked.connect(self.onFindNextClick)
        self.ui.buttonFindAll.clicked.connect(self.onFindAllClick)
        self.ui.buttonReplace.clicked.connect(self.onReplaceNextClick)
        self.ui.buttonReplaceAll.clicked.connect(self.onReplaceAllClick)

        self.ui.frameFindBox.hide()

        # Statusbar
        self.labelStatus = QLabel()
        self.labelStatus.setMargin(2)
        self.statusBar().addPermanentWidget(self.labelStatus, stretch=1)
        self.labelNewLine = QLabel()
        self.labelNewLine.setMargin(2)
        self.statusBar().addPermanentWidget(self.labelNewLine)
        self.labelEncoding = QLabel()
        self.labelEncoding.setMargin(2)
        self.statusBar().addPermanentWidget(self.labelEncoding)
        self.labelType = QLabel()
        self.labelType.setMargin(2)
        self.statusBar().addPermanentWidget(self.labelType)

        self.newline = 'LF'
        self.labelNewLine.setText(self.newline)
        self.encoding = 'UTF-8'
        self.labelEncoding.setText(self.encoding)
        self.labelType.setText(self.highlighter.typeName())

        self.setTitle()
        self.setWindowIcon(QIcon('./res/icon.png'))

        self.move(int(self.settings.value('main/x', 300)), int(self.settings.value('main/y', 200)))
        self.resize(int(self.settings.value('main/width', 800)), int(self.settings.value('main/height', 600)))

        self.show()

    def closeEvent(self, event):
        self.onExitClick()
        event.ignore()

    def setTitle(self):
        title = self.ui.textEdit.documentTitle()
        if not title:
            title = self.tr('untitled')
        if self.ui.textEdit.document().isModified():
            title += ' *'
        self.setWindowTitle(title + ' - Momiji')

    def confirmToSave(self):
        discard = False
        if self.ui.textEdit.document().isModified():
            ret = QMessageBox.question(self, self.tr('Confirm'), self.tr('This file has chages, do you want to save them?'))
            if ret == QMessageBox.Yes:
                self.onSaveClick()
            elif ret == QMessageBox.No:
                discard = True
        return not self.ui.textEdit.document().isModified() or discard

    # File Menu

    def onNewFileClick(self):
        if self.confirmToSave():
            self.ui.textEdit.setPlainText('')
            self.setTitle()
            self.highlighter.clearType()
            self.labelType.setText(self.highlighter.typeName())

    def onOpenClick(self):
        if self.confirmToSave():
            filters = self.tr('Text files (*.txt);;Any files (*)')
            defaultFilter = self.settings.value('mainwindow/filter')
            defaultPath = self.settings.value('mainwindow/path')
            filepath, filter = QFileDialog.getOpenFileName(self, self.tr('Open File'), defaultPath, filters, defaultFilter)
            if filepath:
                self.settings.setValue('mainwindow/path', os.path.dirname(filepath))
                self.settings.setValue('mainwindow/filter', filter)
                with open(filepath, 'rb') as file:
                    bin = file.read()
                    det = chardet.detect(bin)

                    if not det['encoding'] or det['encoding'].upper() == 'ASCII':
                        self.encoding = 'UTF-8'
                    else:
                        self.encoding = det['encoding'].upper()

                    data = bin.decode(self.encoding)
                    self.ui.textEdit.setPlainText(data)
                self.newline = 'CRLF' if '\r\n' in data else 'LF'
                self.labelNewLine.setText(self.newline)
                self.labelEncoding.setText(self.encoding)
                self.ui.textEdit.setDocumentTitle(filepath)
                self.setTitle()
                self.highlighter.setTypeByFilename(filepath)
                self.highlighter.highlight()
                self.labelType.setText(self.highlighter.typeName())

    def onSaveClick(self):
        filepath = self.ui.textEdit.documentTitle()
        if filepath:
            newline = '\r\n' if self.newline == 'CRLF' else '\n'
            with open(filepath, 'w', encoding=self.encoding, newline=newline) as file:
                file.write(self.ui.textEdit.toPlainText())
            self.ui.textEdit.document().setModified(False)
            self.setTitle()
        else:
            self.onSaveAsClick()

    def onSaveAsClick(self):
        ret = QFileDialog.getSaveFileName(self, self.tr('Save File'), '', self.tr('Text files (*.txt);;Any files (*)'))
        if ret and ret[0]:
            filepath = ret[0]
            newline = '\r\n' if self.newline == 'CRLF' else '\n'
            with open(filepath, 'w', encoding=self.encoding, newline=newline) as file:
                file.write(self.ui.textEdit.toPlainText())
            self.ui.textEdit.setDocumentTitle(filepath)
            self.ui.textEdit.document().setModified(False)
            self.setTitle()

    def onSettingsClick(self):
        if not getattr(self, 'settingsDialog', None):
            self.settingsDialog = SettingsDialog(self.settings)
            self.settingsDialog.finished.connect(self.onSettingsClosed)

    def onSettingsClosed(self, result):
        if result:
            font = QFont()
            font.setFamily(self.settings.value('editor/font', font.defaultFamily()))
            font.setPointSize(self.settings.value('editor/size', 9))
            self.ui.textEdit.setFont(font)
        self.settingsDialog = None

    def onExitClick(self):
        if self.confirmToSave():
            self.settings.setValue('main/x', self.pos().x())
            self.settings.setValue('main/y', self.pos().y())
            self.settings.setValue('main/width', self.size().width())
            self.settings.setValue('main/height', self.size().height())
            app.exit()

    # Find Menu

    def getFindFlags(self):
        flags = QTextDocument.FindFlags()
        if self.ui.buttonCase.isChecked():
            flags = flags | QTextDocument.FindCaseSensitively
        if self.ui.buttonWords.isChecked():
            flags = flags | QTextDocument.FindWholeWords
        return flags

    def getFindText(self):
        text = self.ui.editFind.text()
        if self.ui.buttonRegex.isChecked():
            return QRegExp(text)
        else:
            return text

    def onFindClick(self):
        self.ui.frameFindBox.show()
        self.ui.frameReplace.hide()

    def onFindNextClick(self):
        # This didn't work!
        # self.ui.textEdit.find(self.getFindText())
        cursor = self.ui.textEdit.textCursor()
        flags = self.getFindFlags()
        cursor = self.ui.textEdit.document().find(self.getFindText(), cursor, flags)
        if not cursor.isNull():
            self.ui.labelFindResult.setText('')
            self.ui.textEdit.setTextCursor(cursor)
        else:
            self.ui.labelFindResult.setText(self.tr('Not found'))
            self.ui.labelFindResult.setStyleSheet('color: red;')
        self.ui.textEdit.setFocus()

    def onFindPreviousClick(self):
        cursor = self.ui.textEdit.textCursor()
        flags = self.getFindFlags() | QTextDocument.FindBackward
        cursor = self.ui.textEdit.document().find(self.getFindText(), cursor, flags)
        if not cursor.isNull():
            self.ui.labelFindResult.setText('')
            self.ui.textEdit.setTextCursor(cursor)
        else:
            self.ui.labelFindResult.setText(self.tr('Not found'))
            self.ui.labelFindResult.setStyleSheet('color: red;')
        self.ui.textEdit.setFocus()

    def onFindAllClick(self):
        extraSelections = []
        flags = self.getFindFlags()
        self.ui.textEdit.moveCursor(QTextCursor.Start)
        cursor = self.ui.textEdit.textCursor()
        while True:
            cursor = self.ui.textEdit.document().find(self.getFindText(), cursor, flags)
            if cursor.isNull():
                break
            selection = QTextEdit.ExtraSelection()
            selection.format.setBackground(QColor(191, 191, 191, 189))
            selection.cursor = cursor
            extraSelections.append(selection)

        if len(extraSelections):
            self.ui.labelFindResult.setText(self.tr('%d found') % len(extraSelections))
            self.ui.labelFindResult.setStyleSheet('color: green;')
            self.ui.textEdit.setExtraSelections(extraSelections)
            self.ui.textEdit.moveCursor(QTextCursor.End)
        else:
            self.ui.labelFindResult.setText(self.tr('Not found'))
            self.ui.labelFindResult.setStyleSheet('color: red;')
        self.ui.textEdit.setFocus()

    def onReplaceClick(self):
        self.ui.frameFindBox.show()
        self.ui.frameReplace.show()

    def onReplaceNextClick(self):
        cursor = self.ui.textEdit.textCursor()
        flags = flags = self.getFindFlags()
        cursor = self.ui.textEdit.document().find(self.getFindText(), cursor, flags)
        if not cursor.isNull():
            self.ui.labelFindResult.setText('')
            self.ui.textEdit.setTextCursor(cursor)
            cursor.beginEditBlock()
            cursor.removeSelectedText()
            cursor.insertText(self.ui.editReplace.text())
            cursor.endEditBlock()
        else:
            self.ui.labelFindResult.setText(self.tr('Not found'))
            self.ui.labelFindResult.setStyleSheet('color: red;')
        self.ui.textEdit.setFocus()

    def onReplaceAllClick(self):
        results = 0
        flags = self.getFindFlags()
        self.ui.textEdit.moveCursor(QTextCursor.Start)
        cursor = self.ui.textEdit.textCursor()
        cursor.beginEditBlock()
        while True:
            resultCursor = self.ui.textEdit.document().find(self.getFindText(), cursor, flags)
            if resultCursor.isNull():
                break
            cursor.setPosition(resultCursor.anchor())
            cursor.setPosition(resultCursor.position(), QTextCursor.KeepAnchor)
            cursor.removeSelectedText()
            cursor.insertText(self.ui.editReplace.text())
            results += 1
        cursor.endEditBlock()

        if results:
            self.ui.labelFindResult.setText(self.tr('%d replaced') % results)
            self.ui.labelFindResult.setStyleSheet('color: green;')
            self.ui.textEdit.moveCursor(QTextCursor.End)
        else:
            self.ui.labelFindResult.setText(self.tr('Not found'))
            self.ui.labelFindResult.setStyleSheet('color: red;')
        self.ui.textEdit.setFocus()

    def onFindSelectNextClick(self):
        # TODO: implement this
        pass

    def onFindSelectAllClick(self):
        # TODO: implement this
        pass

    def onCloseFindClicked(self):
        self.ui.frameFindBox.hide()
        self.ui.textEdit.setExtraSelections([])

    # Help Menu

    def onAboutClick(self):
        QMessageBox.about(self, self.tr('About Momiji'), 'Momiji v0.1\nsimple cross-platform text editor')


if __name__ == '__main__':
    translator = QTranslator()
    translator.load(QLocale(), 'i18n/')

    app = QApplication(sys.argv)
    app.installTranslator(translator)
    window = MainWindow()
    sys.exit(app.exec_())
