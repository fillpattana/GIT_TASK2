import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class Simple_freehand_drawing(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Simple Freehand Drawing")
        # self.window = QWidget()
        # self.layout = QVBoxLayout()
        #
        # self.rec = QLabel()
        # canvas = QPixmap(400, 300)
        # canvas.fill(QColor('white'))
        # self.rec.setPixmap(canvas)
        #
        # self.clear = QPushButton("clear")
        # self.layout.addWidget(self.rec)
        # self.layout.addWidget(self.clear)
        # self.window.setLayout(self.layout)
        self.rec = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(QColor('white'))
        self.rec.setPixmap(canvas)
        self.setCentralWidget(self.rec)

    def mouseMoveEvent(self, e):
        canvas = self.rec.pixmap()
        painter = QPainter(canvas)
        painter.drawPoint(e.x(), e.y())
        painter.end()
        self.rec.setPixmap(canvas)


def main():
    app = QApplication(sys.argv)
    w = Simple_freehand_drawing()
    w.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())

