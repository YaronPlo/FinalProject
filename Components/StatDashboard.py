from utils import routes
from utils.Helpers.StatisticsHelper import MplWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import numpy as np
import random


class Ui_StatisticsDashboard(object):
    def setupUi(self, StatisticsDashboard):
        StatisticsDashboard.setObjectName("StatisticsDashboard")
        StatisticsDashboard.resize(949, 648)
        StatisticsDashboard.setWindowIcon(QtGui.QIcon(routes.sceLogo))
        StatisticsDashboard.setWindowTitle("Statistics Dashboard")

        self.centralwidget = QtWidgets.QWidget(StatisticsDashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(410, 540, 121, 41))
        self.exitBtn.setObjectName("exitBtn")
        self.exitBtn.setText("Exit")
        self.exitBtn.clicked.connect(StatisticsDashboard.close)

        self.showBtn = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn.setGeometry(QtCore.QRect(210, 10, 93, 31))
        self.showBtn.setObjectName("showBtn")
        self.showBtn.setText("Show")
        self.showBtn.clicked.connect(self.update_graph)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("1")
        self.comboBox.addItem("2")

        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(9, 49, 931, 491))
        self.MplWidget.setObjectName("MplWidget")
        StatisticsDashboard.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(StatisticsDashboard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 26))
        self.menubar.setObjectName("menubar")
        StatisticsDashboard.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StatisticsDashboard)
        self.statusbar.setObjectName("statusbar")
        StatisticsDashboard.setStatusBar(self.statusbar)

        StatisticsDashboard.addToolBar(NavigationToolbar(self.MplWidget.canvas, StatisticsDashboard))

        QtCore.QMetaObject.connectSlotsByName(StatisticsDashboard)

    def update_graph(self):
        fs = 500
        f = random.randint(1, 100)
        ts = 1 / fs
        length_of_signal = 100
        t = np.linspace(0, 1, length_of_signal)

        cosinus_signal = np.cos(2 * np.pi * f * t)
        sinus_signal = np.sin(2 * np.pi * f * t)

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(t, cosinus_signal)
        self.MplWidget.canvas.axes.plot(t, sinus_signal)
        self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
        self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.MplWidget.canvas.draw()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    StatisticsDashboard = QtWidgets.QMainWindow()
    ui = Ui_StatisticsDashboard()
    ui.setupUi(StatisticsDashboard)
    StatisticsDashboard.show()
    sys.exit(app.exec_())
