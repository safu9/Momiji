from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QColor, QPainter
from PySide2.QtWidgets import QWidget


class LineNumberView(QWidget):

    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor
        self.margin = 4

        self.editor.blockCountChanged.connect(self.updateViewWidth)
        self.editor.updateRequest.connect(self.updateView)

        self.updateViewWidth()

    def sizeHint(self):
        return QSize(self.viewWidth(), 0)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(event.rect(), QColor('#ffffff'))

        block = self.editor.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.editor.blockBoundingGeometry(block).translated(self.editor.contentOffset()).top()
        bottom = top + self.editor.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                painter.setPen(QColor('#999999'))
                painter.drawText(
                    self.margin, int(top), self.width() - self.margin * 2, self.editor.fontMetrics().height(),
                    Qt.AlignRight, str(blockNumber + 1)
                )

            block = block.next()
            blockNumber += 1
            top = bottom
            bottom = top + self.editor.blockBoundingRect(block).height()

    def viewWidth(self):
        digits = max(len(str(self.editor.blockCount())), 3)
        return self.margin * 2 + self.editor.fontMetrics().horizontalAdvance('9') * digits

    def updateViewWidth(self):
        self.editor.setViewportMargins(self.viewWidth(), 0, 0, 0)

    def updateView(self, rect, dy):
        if dy:
            self.scroll(0, dy)
        else:
            self.update(0, rect.y(), self.width(), rect.height())

        if rect.contains(self.editor.viewport().rect()):
            self.updateViewWidth()
