from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtCore import QTimer
import PyQt6.QtGui as QtGui
import cv2, sys


class myApp (QMainWindow):

    def videoScale(self,scale=0.0) -> None:
        self.videoWidth = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH) * scale)
        self.videoHeight = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT) * scale)
        print("resize value = ",self.videoWidth,self.videoHeight)

    def __init__(self):
        super(myApp,self).__init__()
        self.setWindowTitle("play video")
        self.setupUI()
        self.videoInit()
        self.setGeometry(0,10,self.videoWidth+20,self.videoHeight+20)
        
    def setupUI(self):
        self.timer = QTimer(self)
        self.videoLabel = QtWidgets.QLabel(self)
        self.videoLabel.move(10,10)
        self.videoLabel.setScaledContents(True)

    def videoInit(self):
        self.video = cv2.VideoCapture('./video/carsBridge.mp4')
        self.timer.start(int(self.video.get(cv2.CAP_PROP_FPS)))
        self.videoScale(0.7)
        self.videoLabel.resize(self.videoWidth,self.videoHeight)
        self.timer.timeout.connect(self.processVideo)

    def processVideo(self):
        if self.video.isOpened():
            ret, frame = self.video.read()
            if ret:
                frame = cv2.resize(frame,(self.videoWidth,self.videoHeight),interpolation=cv2.INTER_AREA)
                cvt = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                qimg = QtGui.QImage(cvt.data,cvt.shape[1],cvt.shape[0],(cvt.shape[1]*3),QtGui.QImage.Format.Format_RGB888)
                self.videoLabel.setPixmap(QtGui.QPixmap.fromImage(qimg))
            else:
                self.timer.stop()
                self.video.release()
                sys.exit()
    
app = QApplication(sys.argv)
win = myApp()
win.show()
sys.exit(app.exec())