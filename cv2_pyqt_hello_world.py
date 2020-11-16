import sys
from PyQt5.QtWidgets import QApplication, QWidget

#创建可以运行的主窗口
if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Hello World!')
    window.show()

    sys.exit(app.exec_())