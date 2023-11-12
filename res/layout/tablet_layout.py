from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from  PyQt5 import QtGui

import sys


class TabletViewWindow(QWidget):
    """"
    Окно с отображением полученных таблиц и их настройка перед сохранением
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.resize(841, 674)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/img/wiki.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowTitle("Table view page")
        self.label = QLabel("Tablet view page")
        layout.addWidget(self.label)
        self.setLayout(layout)

    def view_tabel(self, tabel_list):
        print("get tabel list")

