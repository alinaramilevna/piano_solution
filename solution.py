import sys
import io

from PyQt5 import uic
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>540</width>
    <height>221</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>32</y>
      <width>41</width>
      <height>121</height>
     </rect>
    </property>
    <property name="text">
     <string>ДО</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>30</y>
      <width>41</width>
      <height>121</height>
     </rect>
    </property>
    <property name="text">
     <string>РЕ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_3">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>30</y>
      <width>41</width>
      <height>121</height>
     </rect>
    </property>
    <property name="text">
     <string>МИ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_5">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>30</y>
      <width>41</width>
      <height>121</height>
     </rect>
    </property>
    <property name="text">
     <string>СОЛЬ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_6">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>30</y>
      <width>41</width>
      <height>121</height>
     </rect>
    </property>
    <property name="text">
     <string>ЛЯ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_7">
    <property name="geometry">
     <rect>
      <x>460</x>
      <y>30</y>
      <width>41</width>
      <height>121</height>
     </rect>
    </property>
    <property name="text">
     <string>СИ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_4">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>30</y>
      <width>41</width>
      <height>121</height>
     </rect>
    </property>
    <property name="text">
     <string>ФА</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>160</y>
      <width>371</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Ну оно не падает с ошибкой даже, так что наверное все нормально:)</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>540</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.sounds = {
            'ДО': '1.mp3',
            'РЕ': '2.mp3',
            'МИ': '3.mp3',
            'ФА': '4.mp3',
            'СОЛЬ': '5.mp3',
            'ЛЯ': '6.mp3',
            'СИ': '7.mp3'
        }
        self.pushButton.clicked.connect(self.sound)
        self.pushButton_3.clicked.connect(self.sound)
        self.pushButton_2.clicked.connect(self.sound)
        self.pushButton_4.clicked.connect(self.sound)
        self.pushButton_5.clicked.connect(self.sound)
        self.pushButton_6.clicked.connect(self.sound)
        self.pushButton_7.clicked.connect(self.sound)

    def sound(self):
        send = self.sender().text()
        self.load_mp3('data/' + self.sounds[send])
        self.player.play()

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
