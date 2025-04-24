from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        winWidth,winHeight = 300,300
        screenWid,screenHei = 1920,1080
        self.setGeometry((screenWid-winWidth)//2, (screenHei-winHeight)//2, winWidth, winHeight)
        self.setWindowTitle("qt application")
        self.initUI()
    
    def initUI(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("message")
        self.label1.move(120,130)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("Click me")
        self.btn1.move(95,160)
        self.btn1.clicked.connect(self.click)

    def click(self):
        self.label1.setText("hello world this test print")
        self.label1.adjustSize()