# 教育机构:1
# 讲   师:2
# 开发时间:${1} ${1}

import sys
import time
from PyQt5 import uic
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication


class MyThread(QThread):
    def __init__(self):
        super().__init__()
    def run(self):
        for i in range(5):
            print("正在登录%s" % i)
            time.sleep(1)
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.ui=uic.loadUi("./login.ui")
        self.user_name=self.ui.lineEdit
        self.password=self.ui.lineEdit_2
        self.login=self.ui.pushButton
        self.forget=self.ui.pushButton_2
        self.text=self.ui.textBrowser

        self.login.clicked.connect(self.login1)#绑定槽函数
    def login1(self):
        username=self.user_name.text()
        password=self.password.text()
        self.my_thread=MyThread()
        self.my_thread.start()

        if username=="1" and password=="2":
            self.text.setText("欢迎%s" % username)
            self.text.repaint()
        else:
            self.text.setText("错了")
            self.text.repaint()

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=MyWindow()
    w.ui.show()
    app.exec()


