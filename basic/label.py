from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# find center coordinates
def centerCoordinate(width,height,winWidth,winHeight) -> tuple:
    width = (width-winWidth)//2
    height = (height-winHeight)//2
    return (width, height)

def window() -> None:
    app = QApplication(sys.argv)
    win = QMainWindow()
    centerPoint = centerCoordinate(1920,1080,300,300)
    win.setGeometry(centerPoint[0],centerPoint[1],300,300)
    win.setWindowTitle("Qt application")

    label = QtWidgets.QLabel(win)
    label.setText("my first label")
    shape = label.size()
    coordinate = centerCoordinate(300,300,shape.width(),shape.height())

    label.move(coordinate[0],coordinate[1])

    win.show()
    sys.exit(app.exec())

window()