import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt4 import QtGui
import /face_classification-master/src/SeeSpotRun.py

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Rate Dogs!'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.imageShow = "1.jpg"
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
       
        # Create widget
        # label = QLabel(self)
        # pixmap = QPixmap('1.jpg')
        # label.setPixmap(pixmap)
        # self.resize(pixmap.width(),pixmap.height())

        #call r8k9, returns rating (float)

        # Show  image
        self.pic = QLabel(self)
        self.pic.setGeometry(10, 10, 800, 800)
        self.pic.setPixmap(QPixmap(self.imageShow))

        # Show button 
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.fun)
        btn.move(50, 50)
        #btn.clicked.connect(n(r8k9())


        self.setGeometry(300, 300, 2000, 1500)
        self.setWindowTitle('Rate Dogs!')
        self.show()

    # Connect button to image updating 
    def fun(self):
        #self.imageShow = '2.jpg'
        #self.pic.setPixmap(QPixmap(self.imageShow))
        r8k9()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  



# def main():

#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()