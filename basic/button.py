from PyQt6.QtWidgets import QApplication
import sys
from buttonClass import MyWindow

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())

window()