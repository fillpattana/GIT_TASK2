import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from sjjs import Ui_Form
        
class Calculator(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
    
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        canvas = QPixmap(400, 300)
        canvas.fill(QColor('white'))
        
        self.ui.label.setPixmap(canvas)
        self.ui.pushButton.clicked.connect(self.go)
    
    def mouseMoveEvent(self, e):
        canvas = self.ui.label.pixmap()
        painter = QPainter(canvas)
        painter.drawPoint(e.x(), e.y())
        painter.end()
        self.ui.label.setPixmap(canvas)
        
    def go(self):
        canvas = QPixmap(400, 300)
        canvas.fill(QColor('white'))
        self.ui.label.setPixmap(canvas)
        
        
        
class Simple_freehand_drawing(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Freehand Drawing")
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
        self.win = QWidget()
        self.vbox = QVBoxLayout()
        self.rec = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(QColor('white'))
        self.rec.setPixmap(canvas)
        self.clear = QPushButton("clear")
        self.vbox.addWidget(self.rec)
        self.vbox.addWidget(self.clear)
        self.win.setLayout(self.vbox)

    def mouseMoveEvent(self, e):
        canvas = self.rec.pixmap()
        painter = QPainter(canvas)
        painter.drawPoint(e.x(), e.y())
        painter.end()
        self.rec.setPixmap(canvas)


def main():
    app = QApplication(sys.argv)
    w = Calculator()
    w.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())

