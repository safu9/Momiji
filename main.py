import sys

from PySide2.QtCore import QLocale, QTranslator
from PySide2.QtWidgets import QApplication

from core.main import MainWindow


if __name__ == '__main__':
    translator = QTranslator()
    translator.load(QLocale(), 'i18n/')

    app = QApplication(sys.argv)
    app.installTranslator(translator)
    window = MainWindow()
    sys.exit(app.exec_())
