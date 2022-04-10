from utils import routes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random


class Ui_Statistics(object):
    def setupUi(self, Statistics):
        Statistics.setObjectName("Statistics")
        Statistics.resize(1541, 751)
        Statistics.setWindowTitle("Statistics Dashboard")
        Statistics.setWindowIcon(QtGui.QIcon(routes.sceLogo))

        self.statisticsComboBox = QtWidgets.QComboBox(Statistics)
        self.statisticsComboBox.setGeometry(QtCore.QRect(10, 680, 191, 22))
        self.statisticsComboBox.setObjectName("statisticsComboBox")
        self.statisticsComboBox.addItem("1")
        self.statisticsComboBox.addItem("2")
        self.statisticsComboBox.addItem("3")

        self.showStatisticsBtn = QtWidgets.QPushButton(Statistics)
        self.showStatisticsBtn.setGeometry(QtCore.QRect(60, 710, 93, 28))
        self.showStatisticsBtn.setObjectName("showStatisticsBtn")
        self.showStatisticsBtn.setText("Show")

        self.exit = QPushButton(Statistics)
        self.exit.setGeometry(QtCore.QRect(1430, 710, 93, 28))
        self.exit.setObjectName("exit")
        self.exit.setText("Exit")
        self.exit.clicked.connect(lambda: Statistics.close())

        QtCore.QMetaObject.connectSlotsByName(Statistics)





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Statistics = QtWidgets.QDialog()
    ui = Ui_Statistics()
    ui.setupUi(Statistics)
    Statistics.show()
    sys.exit(app.exec_())
