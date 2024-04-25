# MADE BY theoriginalgrasshopper GPL LICENSE
# INIT
import subprocess
import math
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QFrame, QWidget
import sys
import re
from PIL import Image

# INPUT RESIZE CONFIG FROM USER

imageresizeoption = input('ENABLE GIF RESIZING? y/n (recommended for bigger GIFs)')
if imageresizeoption == ('y'):
    imageresizeoption = True
    imageresizeto = input('RESIZE TIMES WHAT? ENTER INT (e: 2, GIF will be 2x smaller)')
    imageresizeto = int(imageresizeto)

if imageresizeoption == ('n'):
    imageresizeoption = False

# OPEN AND GET THE SIZE OF THE MOVING IMAGE
img = Image.open("MovingImages/image.gif")

imgsize = img.size

if imgsize:
    print(imgsize)  # <------IMAGE SIZE IN CONSOLE FOR DEBUG. REMOVE IF I'M NOT LAZY
    image_size = imgsize # <-------- I'M LAZY I'M NOT RENAMING THE VARIABLE --------------------
else:                                                                  #                       |
    print("ERR:Size not found, most likely not a GIF.")                #                       |
#-put the edited size into a variable-                                 #                       |
                                                                       #                       |
imagewidth, imageheight = image_size                                   #                       |
print (imageheight) # <-------PROPERTIES FOR IMAGE IN CONSOLE, DEBUG. REMOVE IF I'M NOT LAZY <-|
print (imagewidth) # <--------PROPERTIES FOR IMAGE IN CONSOLE, DEBUG. REMOVE IF I'M NOT LAZY <-|  ?

#-if the gif is too damn big-#
if imageresizeoption == True:
    print('HEIGHT TOO BIG, RESIZING')
    imageheight = imageheight / imageresizeto
    imageheight = round(imageheight)
    print ('RESIZED H')
    print (imageheight)
    imagetoobig = True
    print('WIDTH TOO BIG, RESIZING')
    imagewidth = imagewidth / imageresizeto 
    imagewidth = round(imagewidth)
    print ('RESIZED W')
    print (imagewidth)
    imagetoobig = True

if imageresizeoption == False:
    imagetoobig = False
    print('THE TEXT BELOW IS NOT TRUE, DO NOT LISTEN TO THEM!!!!')

# IMAGE IN WINDOW
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, imagewidth, imageheight)) # <---------THIS IS THE SIZE OF THE GIF <----- IT'S ACTUALLY NOT, NEVERMIND
        self.label.setMinimumSize(QtCore.QSize(imagewidth, imageheight)) # <---------THIS IS THE SIZE OF THE GIF <----- IT'S ACTUALLY NOT, NEVERMIND
        self.label.setObjectName("label")


        MainWindow.setCentralWidget(self.centralwidget)

        self.movie = QMovie("MovingImages/image.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        if imagetoobig == True:
            self.movie.setScaledSize(QSize(imagewidth, imageheight))
        else:
            print('No resize operation was executed.')
#-stop function-

        self.label.mousePressEvent = self.mousePressEvent

        self.paused = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.paused:
                self.movie.start()
                self.paused = False
            else:
                self.movie.stop()
                self.paused = True
# GIF RESIZE INFO

if imagetoobig == True:
    print('INFO:The size is not alright. Resize operation needed')
else:
    print('INFO:The size is alright. No resize operation needed.')

# CREATE THE WINDOW AND MAKE THE APPLICATION

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.resize(imagewidth, imageheight)
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.setAttribute(Qt.WA_TranslucentBackground, True)
    window.setWindowFlags(Qt.Window | Qt.FramelessWindowHint) 
    window.show()  
    sys.exit(app.exec_())