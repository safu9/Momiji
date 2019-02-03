from PySide2.QtGui import QColor, QTextFormat
from PySide2.QtWidgets import QPlainTextEdit, QTextEdit

from widget.linenumberview import LineNumberView


class TextEdit(QPlainTextEdit):

    def __init__(self, parent):
        super().__init__(parent)

        self.lineNumberView = LineNumberView(self)
        self.enablehighlightCurrentLine = False

        if self.enablehighlightCurrentLine:
            self.cursorPositionChanged.connect(self.highlightCurrentLine)
            self.highlightCurrentLine()

    def resizeEvent(self, event):
        super().resizeEvent(event)

        cr = self.contentsRect()
        self.lineNumberView.setGeometry(cr.left(), cr.top(), self.lineNumberView.viewWidth(), cr.height())

    def highlightCurrentLine(self):
        selection = QTextEdit.ExtraSelection()
        selection.format.setBackground(QColor('#ffffdd'))
        selection.format.setProperty(QTextFormat.FullWidthSelection, True)
        selection.cursor = self.textCursor()
        selection.cursor.clearSelection()

        self.setExtraSelections([selection])
