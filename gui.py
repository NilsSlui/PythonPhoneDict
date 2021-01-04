from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QLabel
import sys

import ali

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PhoneAlphabet"
        self.top = 200
        self.left = 200
        self.width = 500
        self.height = 80
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        hbox = QHBoxLayout()
        self.lineedit = QLineEdit(self)
        self.lineedit.returnPressed.connect(self.onPressed)
        hbox.addWidget(self.lineedit)
        self.setLayout(hbox)
        self.show()

    def onPressed(self):
        self.lineedit.setText(ali.contstruct_sentence(ali.anal_sentence(ali.telefoon, self.lineedit.text())))

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())