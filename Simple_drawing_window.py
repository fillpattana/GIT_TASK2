import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing")
        self.rabbit = QPixmap("images/rabbit.png")
        
    def  paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([QPoint(50, 200), QPoint(100, 110), QPoint(130, 100), QPoint(100, 150)])
        
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180*6)
        
        p.drawPolygon([QPoint(50, 200), QPoint(150, 200), QPoint(100, 400)])
        
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()


class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing1")
        self.man = QPixmap("images/chinese man.png")
        self.ice = QPixmap("images/bing chilling.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(200, 100, 320, 320), self.man)
        p.drawPixmap(QRect(0, 100, 320, 320), self.ice)
        p.end()
        
class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Akararat Drawing")
        self.jesus = QPixmap("images/Jesus.png")
        self.sun = QPixmap("images/Sun.png")

    def paintEvent(self, e):  
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(200, 100, 320, 320), self.jesus)
        p.drawPixmap(QRect(100, 100, 100, 100), self.sun)

        p.end()
            
def main():
    app = QApplication(sys.argv)
    
    w = Simple_drawing_window()
    w.show()
    
    t = Simple_drawing_window1()
    t.show()
    
    z = Simple_drawing_window2()
    z.show()
        
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
                