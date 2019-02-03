from pygments import highlight
from pygments.formatter import Formatter
from pygments.lexers import get_lexer_for_filename
from pygments.util import ClassNotFound
from PySide2.QtCore import QObject
from PySide2.QtGui import QColor, QFont, QTextCharFormat, QTextLayout


class QtFormatter(Formatter):

    def __init__(self, document, **options):
        Formatter.__init__(self, **options)

        self.document = document

        # Prepare format by styles
        self.styles = {}
        for token, style in self.style:
            format = QTextCharFormat()
            if style['color']:
                format.setForeground(QColor('#' + style['color']))
            if style['bold']:
                format.setFontWeight(QFont.Bold)
            if style['italic']:
                format.setFontItalic(True)
            if style['underline']:
                format.setFontUnderline(True)
            self.styles[token] = format

    def format(self, tokensource, _outfile):
        lasttype = None
        index = 0
        length = 0
        formats = []

        for ttype, value in tokensource:
            while ttype not in self.styles:
                ttype = ttype.parent
            if ttype == lasttype:
                length += len(value)
                continue

            if length:
                formats.append((index, length, self.styles[lasttype]))
                index += length
            lasttype = ttype
            length = len(value)

        if length:
            formats.append((index, length, self.styles[lasttype]))
        self.applyFormats(formats)

    def applyFormats(self, formats):
        block = False
        ranges = []

        for index, length, format in formats:
            oldBlock = block
            block = self.document.findBlock(index)
            if oldBlock and oldBlock.blockNumber() != block.blockNumber():
                oldBlock.layout().setAdditionalFormats(ranges)
                ranges = []

            while length:
                indexInBlock = index - block.position()

                if indexInBlock + length <= block.length():
                    lengthInBlock = length
                    length = 0
                else:
                    lengthInBlock = block.length() - indexInBlock
                    length -= lengthInBlock

                range = QTextLayout.FormatRange()
                range.start = indexInBlock
                range.length = lengthInBlock
                range.format = format
                ranges.append(range)

                if length:
                    block.layout().setAdditionalFormats(ranges)
                    block = block.next()
                    index = block.position()
                    ranges = []


class SyntaxHighlighter(QObject):
    def __init__(self, document):
        super().__init__()

        self.document = document
        self.formatter = QtFormatter(self.document)
        self.lexer = None

        self.document.contentsChange.connect(self.highlight)

    def setTypeByFilename(self, filename):
        if not filename or filename.lower().endswith('.txt'):
            self.lexer = None
            return

        try:
            self.lexer = get_lexer_for_filename(filename)
        except ClassNotFound:
            self.lexer = None

    def clearType(self):
        self.lexer = None

    def typeName(self):
        return self.lexer.name if self.lexer else 'Text'

    def highlight(self):
        if not self.lexer:
            return

        highlight(self.document.toPlainText(), self.lexer, self.formatter)
