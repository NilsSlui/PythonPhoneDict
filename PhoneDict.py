from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QLabel
import sys

nato = ['alfa', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliett', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'x-ray', 'yankee', 'zulu']
telefoon = ['anton', 'bernard', 'cornelis', 'dirk', 'eduard', 'ferninand', 'gerard', 'hendrik', 'izak', 'johan', 'karel', 'lodewijk', 'marie', 'nico', 'otto', 'pieter', 'quotiënt', 'rudolf', 'simon', 'theodoor', 'utrecht', 'victor', 'willem', 'xantippe', 'ypsilon', 'zacharias']
numbers = ['0','1','2','3','4','5','6','7','8','9','$','&','+',',','/',':',';','=','?','@']

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
        self.lineedit.setText(Func.contstruct_sentence(Func.anal_sentence(telefoon, self.lineedit.text())))

class Func():
    def anal_sentence(dictionary, sentence):
        answer = []
        for letter in sentence:
            if letter == ' ':
                answer.append('[space]')
            elif letter in numbers:
                answer.append(letter)
            else:
                for word in dictionary:
                    if letter == word[0]:
                        answer.append(word)
        return answer

    def contstruct_sentence(answer):
        stylized_sentence = ''
        for word in answer:
            stylized_sentence += (word.capitalize() + ' ')
        return stylized_sentence

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())