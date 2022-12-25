from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import  QIcon
from threading import Thread
import ChristmasTree
import DrawBDD
import drawSnow
import sys
import os
import rc_aaa
import time

qmut_3 = QMutex()

class Thread_3(QThread):
    _signal =pyqtSignal()
    def __init__(self):
        super().__init__()

    def run(self):
        qmut_3.lock() # 加锁
        drawSnow.snow()
        import pygame
        play()
        qmut_3.unlock() # 解锁
        self._signal.emit()

class mainUI:
    # _startThread = pyqtSignal()

    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi("Christmas2.ui")
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        self.ui.button1.clicked.connect(self.drawOne)
        self.ui.button2.clicked.connect(self.drawTwo)
        self.ui.button3.clicked.connect(self.click_3)
        # self.ui.label.setText("圣诞快乐！")
        self.ui.exitButton.clicked.connect(app.instance().quit)

    def drawOne(self):
        self.ui.label.setText("圣诞快乐！")
        ChristmasTree.drawmain()
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def drawTwo(self):
        self.ui.label.setText("圣诞快乐！")
        DrawBDD.drawBDD()
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def click_3(self):
        self.ui.button3.setEnabled(False)
        self.ui.thread_3 = Thread_3()
        self.ui.thread_3._signal.connect(self.set_btn3)
        # play()
        self.ui.thread_3.start()

    def set_btn3(self):
        self.ui.button3.setEnabled(True)


def playmusic():
    import os
    from mutagen.mp3 import MP3
    """播放音乐。"""
    Path = r'qrc\\music'
    try:
        list1 = os.listdir(Path)  # 获取指定路径下所有的 mp3 文件
        for x in list1:
            if not (x.endswith('.mp3')):
                list1.remove(x)

        list2 = []
        for i in list1:
            s = os.path.join(Path, i)  # 对路径与文件进行拼接
            list2.append(s)

        while True:
            # 获取每一首歌的时长
            for n in list2:
                path = n
                audio = MP3(path)
                music_volume = 10
                pygame.mixer.init()  # 初始化所有引入的模块
                pygame.mixer.music.set_volume(music_volume/100.0)
                pygame.mixer.music.load(path)  # 载入音乐，音乐可以是 ogg、mp3 等格式
                pygame.mixer.music.play()  # 播放载入的音乐
                time.sleep(int(audio.info.length))  # 获取每一首歌曲的时长，使程序存活的时长等于歌曲时长


    except Exception as e:
        print("Exception: %s" % e)

def play():
    import pygame
    m = Thread(target=playmusic)
    m.setDaemon(True)
    m.start()  # 启动线程

if __name__ == '__main__':
    import pygame
    app = QApplication([])
    app.setWindowIcon(QIcon('icon.jpg'))

    # play()
    m = Thread(target=playmusic)
    m.setDaemon(True)
    m.start()  # 启动线程

    app.setQuitOnLastWindowClosed(False)
    stats = mainUI()
    stats.ui.setWindowFlags(Qt.WindowMinimizeButtonHint)
    stats.ui.show()
    app.exec_()