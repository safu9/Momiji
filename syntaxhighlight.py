from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatter import Formatter
from pygments.util import ClassNotFound
from PySide2.QtGui import QColor, QFont, QSyntaxHighlighter, QTextCharFormat


class QtFormatter(Formatter):

    def __init__(self, highlighter, **options):
        Formatter.__init__(self, **options)

        self.highlighter = highlighter

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

        for ttype, value in tokensource:
            while ttype not in self.styles:
                ttype = ttype.parent
            if ttype == lasttype:
                length += len(value)
                continue

            if length:
                self.highlighter.setFormat(index, length, self.styles[lasttype])
                index += length
            lasttype = ttype
            length = len(value)

        if length:
            self.highlighter.setFormat(index, length, self.styles[lasttype])


class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super().__init__(parent)

        self.formatter = QtFormatter(self)
        self.lexer = None

    def setType(self, filename):
        try:
            self.lexer = get_lexer_for_filename(filename)
            print(self.lexer.name)
        except ClassNotFound:
            self.lexer = None

    def highlightBlock(self, text):
        if not self.lexer:
            return
        highlight(text, self.lexer, self.formatter)
