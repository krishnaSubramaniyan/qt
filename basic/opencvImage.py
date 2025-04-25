from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.QtGui import QImage, QPixmap
import cv2,sys

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    win.setGeometry(100,100,900,700)
    img = cv2.imread('./image/cars.jpg',cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    h,w,ch = img.shape
    bytesPerLine = 3 * w
    q_img = QImage(img.data,w,h,bytesPerLine,QImage.Format.Format_RGB888)

    imgLabel = QtWidgets.QLabel(win)
    imgLabel.resize(800,600)
    imgLabel.move(50,50)
    imgLabel.setPixmap(QPixmap.fromImage(q_img))
    imgLabel.setScaledContents(True)

    win.show()
    sys.exit(app.exec())

window()