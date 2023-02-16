import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 30, 221, 221))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
    
        
        
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 221, 171))
        
        canvas = QPixmap(400, 300)
        canvas.fill(QColor('white'))
        self.label.setPixmap(canvas)
        
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 190, 211, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Clear", None))
        
    def mouseMoveEvent(self, e):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        painter.drawPoint(e.x(), e.y())
        painter.end()
        self.label.setPixmap(canvas)
        
class Calculator(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
    
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        
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

