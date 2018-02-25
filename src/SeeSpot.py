import sys
import random
import tweepy
from keys import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import glob

# from PyQt4 import QtGui
from SeeSpotRun import *

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Rate Dogs!'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 300
        self.imageShow = ["dog.jpg",
        "WoofYou.jpg", #42k
        "Yawn.jpg",    #28k
        "Daisy.jpg",   #48k
        "Snow.jpg",    #59k
        "TootToot.jpg"]
        self.initUI()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        
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
        self.pic.setPixmap(QPixmap(self.imageShow[0]))

        # Show button 
        btn = QPushButton('Rate', self)
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
        countdown = ["3","2","1"]
        for i in range(3):
            print(countdown[i])
            time.sleep(1)
        print("GO")
        self.imageShow = glob.glob("C:/Users/MLH Admin/Desktop/woofWoof/woofwoof/face_classification-master/src/*.jpg")
        random.shuffle(self.imageShow)
        print(self.imageShow[0])
        self.pic.setPixmap(QPixmap(self.imageShow[0]))
        rating = r8k9()
        self.pic.setPixmap(QPixmap("Graph.png"))
        self.api.update_with_media(self.imageShow[0],"I r8 this k9: "+ str(rating)+ "/10. Like us on devpost tinyurl.com/spothackcu. #HackCU #Unmanned #Unmannedsbestfried")

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