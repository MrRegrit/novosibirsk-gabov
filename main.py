import sys
import random
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.uic


class Example(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        PyQt5.uic.loadUi("Ui.ui", self)
        self.setWindowTitle('Рисование')
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = PyQt5.QtGui.QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        r = random.randint(1, 100)
        qp.setBrush(PyQt5.QtGui.QColor(255, 255, 0))
        qp.drawEllipse(
            random.randint(1, 100),
            random.randint(1, 100),
            r,
            r,
        )


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
