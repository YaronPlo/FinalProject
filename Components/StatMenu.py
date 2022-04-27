from utils import routes
from PyQt5 import QtCore, QtGui, QtWidgets
from utils.Helpers.StatisticsHelper import *


class Ui_StatisticsMenu(object):
    def setupUi(self, StatisticsMenu):
        StatisticsMenu.setObjectName("StatisticsMenu")
        StatisticsMenu.resize(400, 368)
        StatisticsMenu.setWindowIcon(QtGui.QIcon(routes.sceLogo))
        StatisticsMenu.setWindowTitle("Statistics Menu")

        self.centralwidget = QtWidgets.QWidget(StatisticsMenu)
        self.centralwidget.setObjectName("centralwidget")

        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(140, 310, 121, 41))
        self.exitBtn.setObjectName("exitBtn")
        self.exitBtn.setText("Exit")
        self.exitBtn.clicked.connect(StatisticsMenu.close)

        self.showBtn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn_1.setGeometry(QtCore.QRect(270, 30, 101, 61))
        self.showBtn_1.setObjectName("showBtn_1")
        self.showBtn_1.setText("Show")
        self.showBtn_1.clicked.connect(
            lambda: call_stat_graph(get_graphs_pdf))

        self.showBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn_2.setGeometry(QtCore.QRect(150, 30, 101, 61))
        self.showBtn_2.setObjectName("showBtn_2")

        self.showBtn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn_3.setGeometry(QtCore.QRect(30, 30, 101, 61))
        self.showBtn_3.setObjectName("showBtn_3")

        self.showBtn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn_4.setGeometry(QtCore.QRect(270, 120, 101, 61))
        self.showBtn_4.setObjectName("showBtn_4")

        self.showBtn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn_5.setGeometry(QtCore.QRect(150, 120, 101, 61))
        self.showBtn_5.setObjectName("showBtn_5")

        self.showBtn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn_6.setGeometry(QtCore.QRect(30, 120, 101, 61))
        self.showBtn_6.setObjectName("showBtn_6")

        self.showBtn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn_7.setGeometry(QtCore.QRect(270, 210, 101, 61))
        self.showBtn_7.setObjectName("showBtn_7")

        self.showBtn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn_8.setGeometry(QtCore.QRect(150, 210, 101, 61))
        self.showBtn_8.setObjectName("showBtn_8")

        self.showBtn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn_9.setGeometry(QtCore.QRect(30, 210, 101, 61))
        self.showBtn_9.setObjectName("showBtn_9")

        StatisticsMenu.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(StatisticsMenu)
