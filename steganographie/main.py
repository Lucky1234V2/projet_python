import sys

from PyQt5.QtWidgets import QApplication
from watermark_front import MyWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
