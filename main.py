import sys

from PySide2.QtCore import QEvent, QFile, QLocale, QObject, QTranslator
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QFileDialog, QMessageBox


class MainWindow(QObject):

    def __init__(self, filename):
        super().__init__()

        # Load UI File
        file = QFile(filename)
        file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(file)
        file.close()

        # Connect events
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

    def onNewFileClick(self):
        if self.confirmToSave():
            self.window.textEdit.setPlainText('')

    def onOpenClick(self):
        if self.confirmToSave():
            ret = QFileDialog.getOpenFileName(self.window, self.tr('Open File'), '', self.tr('Text files (*.txt);;Any files (*)'))
            if ret and ret[0]:
                filepath = ret[0]
                with open(filepath, 'r') as file:
                    self.window.textEdit.setPlainText(file.read())
                self.window.textEdit.setDocumentTitle(filepath)
                self.setTitle()

    def onSaveClick(self):
        filepath = self.window.textEdit.documentTitle()
        if filepath:
            with open(filepath, 'w') as file:
                file.write(self.window.textEdit.toPlainText())
            self.window.textEdit.document().setModified(False)
            self.setTitle()
        else:
            self.onSaveAsClick()

    def onSaveAsClick(self):
        ret = QFileDialog.getSaveFileName(self.window, self.tr('Save File'), '', self.tr('Text files (*.txt);;Any files (*)'))
        if ret and ret[0]:
            filepath = ret[0]
            with open(filepath, 'w') as file:
                file.write(self.window.textEdit.toPlainText())
            self.window.textEdit.setDocumentTitle(filepath)
            self.window.textEdit.document().setModified(False)
            self.setTitle()

    def onExitClick(self):
        if self.confirmToSave():
            self.window.removeEventFilter(self)
            app.exit()

    def onAboutClick(self):
        QMessageBox.about(self.window, self.tr('About Momiji'), 'Momiji v0.1\nsimple cross-platform text editor')


if __name__ == '__main__':
    translator = QTranslator()
    translator.load(QLocale(), 'i18n/')

    app = QApplication(sys.argv)
    app.installTranslator(translator)
    window = MainWindow('window.ui')
    sys.exit(app.exec_())
