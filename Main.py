import io
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QColor, QPolygon
import sys
import random

screen_size = [600, 600]

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Желтые окружности')
        self.pushButton.clicked.connect(self.draw)
        self.tof = False

    def draw(self):
        self.size = random.randint(10, 100)
        self.tof = True
        self.update()

    def paintEvent(self, event):
        if self.tof:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('yellow'))
            self.x, self.y = random.randint(self.size, screen_size[0] - self.size), random.randint(self.size, screen_size[1] - self.size)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
