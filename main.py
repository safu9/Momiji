import sys

from PySide2.QtCore import QFile, QObject
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QFileDialog, QMessageBox


class Window(QObject):

    def __init__(self, filename, parent=None):
        super().__init__(parent)

        # Load UI File
        file = QFile(filename)
        file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(file)
        file.close()

        # Connect events
        self.window.actionNew.triggered.connect(self.onNewClick)
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

        self.window.actionUndo.setEnabled(False)
        self.window.actionRedo.setEnabled(False)
        self.window.actionCopy.setEnabled(False)
        self.window.actionCut.setEnabled(False)

        self.setTitle()
        self.window.resize(800, 600)
        self.window.show()

    def setTitle(self, title=''):
        if not title:
            title = 'untitled'
        self.window.setWindowTitle(title + ' - Momiji')

    def onNewClick(self):
        self.window.textEdit.setPlainText('')

    def onOpenClick(self):
        ret = QFileDialog.getOpenFileName(self.window, 'Open File', '', 'Text files (*.txt);;Any files (*)')
        if ret and ret[0]:
            filepath = ret[0]
            with open(filepath, 'r') as file:
                self.window.textEdit.setPlainText(file.read())
            self.window.textEdit.setDocumentTitle(filepath)
            self.setTitle(filepath)

    def onSaveClick(self):
        filepath = self.window.textEdit.documentTitle()
        if filepath:
            with open(filepath, 'w') as file:
                file.write(self.window.textEdit.toPlainText())
        else:
            self.onSaveAsClick()

    def onSaveAsClick(self):
        ret = QFileDialog.getSaveFileName(self.window, 'Save File', '', 'Text files (*.txt);;Any files (*)')
        if ret and ret[0]:
            filepath = ret[0]
            with open(filepath, 'w') as file:
                file.write(self.window.textEdit.toPlainText())
            self.window.textEdit.setDocumentTitle(filepath)
            self.setTitle(filepath)

    def onExitClick(self):
        app.exit()

    def onAboutClick(self):
        QMessageBox.about(self.window, 'About Momiji', 'Momiji v0.1\nsimple cross-platform text editor')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window('window.ui')
    sys.exit(app.exec_())
