import sys

import chardet
from PySide2.QtCore import QEvent, QLocale, QObject, QRegExp, QTranslator
from PySide2.QtGui import QColor, QTextCursor, QTextDocument
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QFileDialog, QLabel, QMessageBox, QStyle, QTextEdit

from syntaxhighlight import SyntaxHighlighter


class MainWindow(QObject):

    def __init__(self, filename):
        super().__init__()

        # Load UI File
        loader = QUiLoader()
        self.window = loader.load(filename)

        # Menu
        self.window.actionNewFile.triggered.connect(self.onNewFileClick)
        self.window.actionOpen.triggered.connect(self.onOpenClick)
        self.window.actionSave.triggered.connect(self.onSaveClick)
        self.window.actionSaveAs.triggered.connect(self.onSaveAsClick)
        self.window.actionExit.triggered.connect(self.onExitClick)

        self.window.actionUndo.triggered.connect(self.window.textEdit.undo)
        self.window.actionRedo.triggered.connect(self.window.textEdit.redo)
        self.window.actionCopy.triggered.connect(self.window.textEdit.copy)
        self.window.actionCut.triggered.connect(self.window.textEdit.cut)
        self.window.actionPaste.triggered.connect(self.window.textEdit.paste)
        self.window.actionSelectAll.triggered.connect(self.window.textEdit.selectAll)

        self.window.actionFind.triggered.connect(self.onFindClick)
        self.window.actionFindNext.triggered.connect(self.onFindNextClick)
        self.window.actionFindPrevious.triggered.connect(self.onFindPreviousClick)
        self.window.actionFindAll.triggered.connect(self.onFindAllClick)
        self.window.actionReplace.triggered.connect(self.onReplaceClick)
        self.window.actionReplaceNext.triggered.connect(self.onReplaceNextClick)
        self.window.actionReplaceAll.triggered.connect(self.onReplaceAllClick)
        self.window.actionFindSelectNext.triggered.connect(self.onFindSelectNextClick)
        self.window.actionFindSelectAll.triggered.connect(self.onFindSelectAllClick)

        self.window.actionAbout.triggered.connect(self.onAboutClick)

        self.window.textEdit.undoAvailable.connect(self.window.actionUndo.setEnabled)
        self.window.textEdit.redoAvailable.connect(self.window.actionRedo.setEnabled)
        self.window.textEdit.copyAvailable.connect(self.window.actionCopy.setEnabled)
        self.window.textEdit.copyAvailable.connect(self.window.actionCut.setEnabled)
        self.window.textEdit.modificationChanged.connect(self.setTitle)

        self.window.actionUndo.setEnabled(False)
        self.window.actionRedo.setEnabled(False)
        self.window.actionCopy.setEnabled(False)
        self.window.actionCut.setEnabled(False)

        # Syntax Highlight
        self.highlighter = SyntaxHighlighter(self.window.textEdit.document())

        # Find box
        self.window.buttonCloseFind.clicked.connect(self.onCloseFindClicked)
        self.window.buttonFind.clicked.connect(self.onFindNextClick)
        self.window.buttonFindAll.clicked.connect(self.onFindAllClick)
        self.window.buttonReplace.clicked.connect(self.onReplaceNextClick)
        self.window.buttonReplaceAll.clicked.connect(self.onReplaceAllClick)

        self.window.frameFindBox.hide()

        # Statusbar
        self.labelStatus = QLabel()
        self.window.statusBar().addPermanentWidget(self.labelStatus, stretch=1)
        self.labelNewLine = QLabel()
        self.window.statusBar().addPermanentWidget(self.labelNewLine)
        self.labelEncoding = QLabel()
        self.window.statusBar().addPermanentWidget(self.labelEncoding)
        self.labelType = QLabel()
        self.window.statusBar().addPermanentWidget(self.labelType)

        self.newline = 'LF'
        self.labelNewLine.setText(self.newline)
        self.encoding = 'UTF-8'
        self.labelEncoding.setText(self.encoding)
        self.labelType.setText(self.highlighter.typeName())

        self.setTitle()
        self.window.installEventFilter(self)
        self.window.resize(800, 600)
        self.window.show()

    def eventFilter(self, obj, event):
        if obj is self.window and event.type() == QEvent.Close:
            self.onExitClick()
            event.ignore()
            return True
        return super().eventFilter(obj, event)

    def setTitle(self):
        title = self.window.textEdit.documentTitle()
        if not title:
            title = self.tr('untitled')
        if self.window.textEdit.document().isModified():
            title += ' *'
        self.window.setWindowTitle(title + ' - Momiji')

    def confirmToSave(self):
        discard = False
        if self.window.textEdit.document().isModified():
            ret = QMessageBox.question(self.window, self.tr('Confirm'), self.tr('This file has chages, do you want to save them?'))
            if ret == QMessageBox.Yes:
                self.onSaveClick()
            elif ret == QMessageBox.No:
                discard = True
        return not self.window.textEdit.document().isModified() or discard

    # File Menu

    def onNewFileClick(self):
        if self.confirmToSave():
            self.window.textEdit.setPlainText('')
            self.setTitle()
            self.highlighter.clearType()
            self.labelType.setText(self.highlighter.typeName())

    def onOpenClick(self):
        if self.confirmToSave():
            ret = QFileDialog.getOpenFileName(self.window, self.tr('Open File'), '', self.tr('Text files (*.txt);;Any files (*)'))
            if ret and ret[0]:
                filepath = ret[0]
                with open(filepath, 'rb') as file:
                    bin = file.read()
                    det = chardet.detect(bin)

                    if not det['encoding'] or det['encoding'].upper() == 'ASCII':
                        self.encoding = 'UTF-8'
                    else:
                        self.encoding = det['encoding'].upper()

                    data = bin.decode(self.encoding)
                    self.window.textEdit.setPlainText(data)
                self.newline = 'CRLF' if '\r\n' in data else 'LF'
                self.labelNewLine.setText(self.newline)
                self.labelEncoding.setText(self.encoding)
                self.window.textEdit.setDocumentTitle(filepath)
                self.setTitle()
                self.highlighter.setTypeByFilename(filepath)
                self.highlighter.highlight()
                self.labelType.setText(self.highlighter.typeName())

    def onSaveClick(self):
        filepath = self.window.textEdit.documentTitle()
        if filepath:
            newline = '\r\n' if self.newline == 'CRLF' else '\n'
            with open(filepath, 'w', encoding=self.encoding, newline=newline) as file:
                file.write(self.window.textEdit.toPlainText())
            self.window.textEdit.document().setModified(False)
            self.setTitle()
        else:
            self.onSaveAsClick()

    def onSaveAsClick(self):
        ret = QFileDialog.getSaveFileName(self.window, self.tr('Save File'), '', self.tr('Text files (*.txt);;Any files (*)'))
        if ret and ret[0]:
            filepath = ret[0]
            newline = '\r\n' if self.newline == 'CRLF' else '\n'
            with open(filepath, 'w', encoding=self.encoding, newline=newline) as file:
                file.write(self.window.textEdit.toPlainText())
            self.window.textEdit.setDocumentTitle(filepath)
            self.window.textEdit.document().setModified(False)
            self.setTitle()

    def onExitClick(self):
        if self.confirmToSave():
            self.window.removeEventFilter(self)
            app.exit()

    # Find Menu

    def getFindFlags(self):
        flags = QTextDocument.FindFlags()
        if self.window.buttonCase.isChecked():
            flags = flags | QTextDocument.FindCaseSensitively
        if self.window.buttonWords.isChecked():
            flags = flags | QTextDocument.FindWholeWords
        return flags

    def getFindText(self):
        text = self.window.editFind.text()
        if self.window.buttonRegex.isChecked():
            return QRegExp(text)
        else:
            return text

    def onFindClick(self):
        self.window.frameFindBox.show()
        self.window.frameReplace.hide()

    def onFindNextClick(self):
        # This didn't work!
        # self.window.textEdit.find(self.getFindText())
        cursor = self.window.textEdit.textCursor()
        flags = self.getFindFlags()
        cursor = self.window.textEdit.document().find(self.getFindText(), cursor, flags)
        if not cursor.isNull():
            self.window.labelFindResult.setText('')
            self.window.textEdit.setTextCursor(cursor)
        else:
            self.window.labelFindResult.setText(self.tr('Not found'))
            self.window.labelFindResult.setStyleSheet('color: red;')
        self.window.textEdit.setFocus()

    def onFindPreviousClick(self):
        cursor = self.window.textEdit.textCursor()
        flags = self.getFindFlags() | QTextDocument.FindBackward
        cursor = self.window.textEdit.document().find(self.getFindText(), cursor, flags)
        if not cursor.isNull():
            self.window.labelFindResult.setText('')
            self.window.textEdit.setTextCursor(cursor)
        else:
            self.window.labelFindResult.setText(self.tr('Not found'))
            self.window.labelFindResult.setStyleSheet('color: red;')
        self.window.textEdit.setFocus()

    def onFindAllClick(self):
        extraSelections = []
        flags = self.getFindFlags()
        self.window.textEdit.moveCursor(QTextCursor.Start)
        cursor = self.window.textEdit.textCursor()
        while True:
            cursor = self.window.textEdit.document().find(self.getFindText(), cursor, flags)
            if cursor.isNull():
                break
            selection = QTextEdit.ExtraSelection()
            selection.format.setBackground(QColor(191, 191, 191, 189))
            selection.cursor = cursor
            extraSelections.append(selection)

        if len(extraSelections):
            self.window.labelFindResult.setText(self.tr('%d found') % len(extraSelections))
            self.window.labelFindResult.setStyleSheet('color: green;')
            self.window.textEdit.setExtraSelections(extraSelections)
            self.window.textEdit.moveCursor(QTextCursor.End)
        else:
            self.window.labelFindResult.setText(self.tr('Not found'))
            self.window.labelFindResult.setStyleSheet('color: red;')
        self.window.textEdit.setFocus()

    def onReplaceClick(self):
        self.window.frameFindBox.show()
        self.window.frameReplace.show()

    def onReplaceNextClick(self):
        cursor = self.window.textEdit.textCursor()
        flags = flags = self.getFindFlags()
        cursor = self.window.textEdit.document().find(self.getFindText(), cursor, flags)
        if not cursor.isNull():
            self.window.labelFindResult.setText('')
            self.window.textEdit.setTextCursor(cursor)
            cursor.beginEditBlock()
            cursor.removeSelectedText()
            cursor.insertText(self.window.editReplace.text())
            cursor.endEditBlock()
        else:
            self.window.labelFindResult.setText(self.tr('Not found'))
            self.window.labelFindResult.setStyleSheet('color: red;')
        self.window.textEdit.setFocus()

    def onReplaceAllClick(self):
        results = 0
        flags = self.getFindFlags()
        self.window.textEdit.moveCursor(QTextCursor.Start)
        cursor = self.window.textEdit.textCursor()
        cursor.beginEditBlock()
        while True:
            resultCursor = self.window.textEdit.document().find(self.getFindText(), cursor, flags)
            if resultCursor.isNull():
                break
            cursor.setPosition(resultCursor.anchor())
            cursor.setPosition(resultCursor.position(), QTextCursor.KeepAnchor)
            cursor.removeSelectedText()
            cursor.insertText(self.window.editReplace.text())
            results += 1
        cursor.endEditBlock()

        if results:
            self.window.labelFindResult.setText(self.tr('%d replaced') % results)
            self.window.labelFindResult.setStyleSheet('color: green;')
            self.window.textEdit.moveCursor(QTextCursor.End)
        else:
            self.window.labelFindResult.setText(self.tr('Not found'))
            self.window.labelFindResult.setStyleSheet('color: red;')
        self.window.textEdit.setFocus()

    def onFindSelectNextClick(self):
        # TODO: implement this
        pass

    def onFindSelectAllClick(self):
        # TODO: implement this
        pass

    def onCloseFindClicked(self):
        self.window.frameFindBox.hide()
        self.window.textEdit.setExtraSelections([])

    # Help Menu

    def onAboutClick(self):
        QMessageBox.about(self.window, self.tr('About Momiji'), 'Momiji v0.1\nsimple cross-platform text editor')


if __name__ == '__main__':
    translator = QTranslator()
    translator.load(QLocale(), 'i18n/')

    app = QApplication(sys.argv)
    app.installTranslator(translator)
    window = MainWindow('window.ui')
    sys.exit(app.exec_())
