import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.click)
        self.is_draw = False

    def click(self):
        self.is_draw = True
        self.repaint()

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        if self.is_draw is True:
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw(qp)
            # Завершаем рисование
            qp.end()

    def draw(self, qp):
        a = randint(0, 255)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(200, 200, a, a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())