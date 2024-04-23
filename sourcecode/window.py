# MADE BY theoriginalgrasshopper GPL LICENSE
# INIT
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QFrame, QWidget
import sys
import re
from PIL import Image

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

# IMAGE IN WINDOW
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, imagewidth, imageheight)) # <---------THIS IS THE SIZE OF THE GIF
        self.label.setMinimumSize(QtCore.QSize(imagewidth, imageheight)) # <---------THIS IS THE SIZE OF THE GIF
        self.label.setObjectName("label")


        MainWindow.setCentralWidget(self.centralwidget)

        self.movie = QMovie("MovingImages/image.gif")
        self.label.setMovie(self.movie)
        self.movie.start()


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