from PySide2.QtGui import QFont
from PySide2.QtWidgets import QDialog

from settings_ui import Ui_SettingsDialog


class SettingsDialog(QDialog):

    def __init__(self, settings):
        super().__init__()

        self.settings = settings

        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

        self.font = QFont()
        self.font.setFamily(self.settings.value('editor/font', self.font.defaultFamily()))
        self.font.setPointSize(int(self.settings.value('editor/size', 9)))

        self.ui.fontComboBox.setCurrentFont(self.font)
        self.ui.spinBoxSize.setValue(self.font.pointSize())
        self.ui.labelPreviewFont.setFont(self.font)

        self.ui.fontComboBox.currentFontChanged.connect(self.onChangeFont)
        self.ui.spinBoxSize.valueChanged.connect(self.onChangeSize)

        self.setWindowTitle(self.tr('Settings'))
        self.open()

    def onChangeFont(self, f):
        self.font.setFamily(f.family())
        self.ui.labelPreviewFont.setFont(self.font)

    def onChangeSize(self, size):
        self.font.setPointSize(size)
        self.ui.labelPreviewFont.setFont(self.font)

    def accept(self):
        self.settings.setValue('editor/font', self.font.family())
        self.settings.setValue('editor/size', self.font.pointSize())
        super().accept()
