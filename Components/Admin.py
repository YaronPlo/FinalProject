from PyQt5 import QtCore, QtGui, QtWidgets
from Components import Login
import csv
import json
import sys

fileDB = ".\\utils\\DataBase\\info.json"


class Ui_AdminPage(object):
    def __init__(self):
        self.CSV = None
        self.sortByDate_4 = None
        self.wsmSort_4 = None
        self.integrity_3 = None
        self.confideality_3 = None
        self.impactLabel_3 = None
        self.lineEdit_4 = None
        self.lineEdit_3 = None
        self.bakeBtn_3 = None
        self.rulesLabel_3 = None
        self.sortByDate_3 = None
        self.latestDate_3 = None
        self.earliestDate_3 = None
        self.grid_3 = None
        self.wsmSort_3 = None
        self.lineEdit_5 = None
        self.bakeBtn_2 = None
        self.analyst3 = None
        self.integrity_4 = None
        self.confideality_4 = None
        self.impactLabel_4 = None
        self.latestDate_4 = None
        self.earliestDate_4 = None
        self.lineEdit = None
        self.bakeBtn_4 = None
        self.rulesLabel_4 = None
        self.grid_4 = None
        self.gridLayoutWidget_4 = None
        self.analyst4 = None
        self.availability_3 = None
        self.lineEdit_6 = None
        self.impactLabel_2 = None
        self.integrity_2 = None
        self.availability_2 = None
        self.confideality_2 = None
        self.wsmSort_2 = None
        self.latestDate_2 = None
        self.grid_2 = None
        self.earliestDate_2 = None
        self.sortByDate_2 = None
        self.gridLayoutWidget_2 = None
        self.rulesLabel_2 = None
        self.analyst2 = None
        self.availability = None
        self.integrity = None
        self.confideality = None
        self.lineEdit_2 = None
        self.availability_4 = None
        self.gridLayoutWidget_3 = None
        self.importCsvBtn = None
        self.impactLabel = None
        self.lineEdit_9 = None
        self.lineEdit_10 = None
        self.bakeBtn = None
        self.wsmSort = None
        self.latestDate = None
        self.sortByDate = None
        self.earliestDate = None
        self.grid = None
        self.gridLayoutWidget = None
        self.rulesLabel = None
        self.analyst1 = None
        self.rawDataTableWidget = None
        self.rawData = None
        self.ExitBtn = None
        self.toolBox = None
        self.welcomeLbl = None
        self.centralwidget = None
        self.ui = None
        self.LoginWindow = None
        self.csvTuple = None

    def openLogin(self, AdminPage):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = Login.UiLogIn()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        AdminPage.close()

    def setupUi(self, AdminPage):
        AdminPage.setObjectName("AdminPage")
        AdminPage.setEnabled(True)
        AdminPage.resize(990, 768)
        AdminPage.setWindowIcon(QtGui.QIcon(".\\utils\\Images\\SCElogo.png"))

        self.centralwidget = QtWidgets.QWidget(AdminPage)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomeLbl = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLbl.setGeometry(QtCore.QRect(280, 20, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.welcomeLbl.setFont(font)
        self.welcomeLbl.setObjectName("welcomeLbl")

        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(80, 140, 831, 561))
        self.toolBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.toolBox.setFrameShape(QtWidgets.QFrame.Box)
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolBox.setLineWidth(1)
        self.toolBox.setMidLineWidth(1)
        self.toolBox.setObjectName("toolBox")

        self.rawData = QtWidgets.QWidget()
        self.rawData.setObjectName("rawData")
        self.rawDataTableWidget = QtWidgets.QTableWidget(self.rawData)
        self.rawDataTableWidget.setGeometry(QtCore.QRect(0, 0, 841, 471))
        self.rawDataTableWidget.setObjectName("rawDataTableWidget")
        self.rawDataTableWidget.setColumnCount(0)
        self.rawDataTableWidget.setRowCount(0)
        self.toolBox.addItem(self.rawData, "")

        # -----------------Analyst1-------------------
        self.analyst1 = QtWidgets.QWidget()
        self.analyst1.setObjectName("analyst1")
        self.rulesLabel = QtWidgets.QLabel(self.analyst1)
        self.rulesLabel.setGeometry(QtCore.QRect(10, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.rulesLabel.setFont(font)
        self.rulesLabel.setObjectName("rulesLabel")

        self.gridLayoutWidget = QtWidgets.QWidget(self.analyst1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 50, 191, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setObjectName("grid")

        self.earliestDate = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.earliestDate.setDateTime(
            QtCore.QDateTime(QtCore.QDate(2023, 3, 13), QtCore.QTime(0, 0, 0))
        )
        self.earliestDate.setCalendarPopup(True)
        self.earliestDate.setDate(QtCore.QDate(2023, 3, 13))
        self.earliestDate.setObjectName("earliestDate")

        self.grid.addWidget(self.earliestDate, 2, 0, 1, 1)
        self.sortByDate = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.sortByDate.setObjectName("sortByDate")
        self.grid.addWidget(self.sortByDate, 0, 0, 1, 1)
        self.latestDate = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.latestDate.setCalendarPopup(True)
        self.latestDate.setDate(QtCore.QDate(2022, 3, 19))
        self.latestDate.setObjectName("latestDate")
        self.grid.addWidget(self.latestDate, 1, 0, 1, 1)
        self.wsmSort = QtWidgets.QCheckBox(self.analyst1)
        self.wsmSort.setGeometry(QtCore.QRect(310, 60, 111, 20))
        self.wsmSort.setObjectName("wsmSort")
        self.bakeBtn = QtWidgets.QPushButton(self.analyst1)
        self.bakeBtn.setGeometry(QtCore.QRect(360, 350, 111, 41))
        self.bakeBtn.setObjectName("bakeBtn")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.analyst1)
        self.lineEdit_9.setGeometry(QtCore.QRect(10, 310, 601, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.analyst1)
        self.lineEdit_10.setGeometry(QtCore.QRect(10, 250, 601, 22))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.impactLabel = QtWidgets.QLabel(self.analyst1)
        self.impactLabel.setGeometry(QtCore.QRect(520, 60, 181, 21))
        self.impactLabel.setObjectName("impactLabel")
        self.confideality = QtWidgets.QCheckBox(self.analyst1)
        self.confideality.setGeometry(QtCore.QRect(540, 80, 111, 20))
        self.confideality.setObjectName("confideality")
        self.integrity = QtWidgets.QCheckBox(self.analyst1)
        self.integrity.setGeometry(QtCore.QRect(540, 100, 81, 20))
        self.integrity.setObjectName("integrity")
        self.availability = QtWidgets.QCheckBox(self.analyst1)
        self.availability.setGeometry(QtCore.QRect(540, 120, 111, 20))
        self.availability.setObjectName("availability")
        self.toolBox.addItem(self.analyst1, "")

        # ------------------- Analyst2 -----------------------------
        self.analyst2 = QtWidgets.QWidget()
        self.analyst2.setObjectName("analst2")
        self.rulesLabel_2 = QtWidgets.QLabel(self.analyst2)
        self.rulesLabel_2.setGeometry(QtCore.QRect(10, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.rulesLabel_2.setFont(font)
        self.rulesLabel_2.setObjectName("rulesLabel_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.analyst2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 50, 191, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.grid_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid_2.setContentsMargins(0, 0, 0, 0)
        self.grid_2.setObjectName("grid_2")
        self.earliestDate_2 = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.earliestDate_2.setDateTime(
            QtCore.QDateTime(QtCore.QDate(2023, 3, 13), QtCore.QTime(0, 0, 0))
        )
        self.earliestDate_2.setCalendarPopup(True)
        self.earliestDate_2.setDate(QtCore.QDate(2023, 3, 13))
        self.earliestDate_2.setObjectName("earliestDate_2")
        self.grid_2.addWidget(self.earliestDate_2, 2, 0, 1, 1)
        self.sortByDate_2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.sortByDate_2.setObjectName("sortByDate_2")
        self.grid_2.addWidget(self.sortByDate_2, 0, 0, 1, 1)
        self.latestDate_2 = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.latestDate_2.setCalendarPopup(True)
        self.latestDate_2.setDate(QtCore.QDate(2022, 3, 19))
        self.latestDate_2.setObjectName("latestDate_2")
        self.grid_2.addWidget(self.latestDate_2, 1, 0, 1, 1)
        self.wsmSort_2 = QtWidgets.QCheckBox(self.analyst2)
        self.wsmSort_2.setGeometry(QtCore.QRect(310, 60, 111, 20))
        self.wsmSort_2.setObjectName("wsmSort_2")
        self.bakeBtn_2 = QtWidgets.QPushButton(self.analyst2)
        self.bakeBtn_2.setGeometry(QtCore.QRect(360, 350, 111, 41))
        self.bakeBtn_2.setObjectName("bakeBtn_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.analyst2)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 310, 601, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.analyst2)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 260, 601, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.impactLabel_2 = QtWidgets.QLabel(self.analyst2)
        self.impactLabel_2.setGeometry(QtCore.QRect(520, 60, 181, 21))
        self.impactLabel_2.setObjectName("impactLabel_2")
        self.confideality_2 = QtWidgets.QCheckBox(self.analyst2)
        self.confideality_2.setGeometry(QtCore.QRect(550, 80, 111, 20))
        self.confideality_2.setObjectName("confideality_2")
        self.integrity_2 = QtWidgets.QCheckBox(self.analyst2)
        self.integrity_2.setGeometry(QtCore.QRect(550, 100, 81, 20))
        self.integrity_2.setObjectName("integrity_2")
        self.availability_2 = QtWidgets.QCheckBox(self.analyst2)
        self.availability_2.setGeometry(QtCore.QRect(550, 120, 101, 20))
        self.availability_2.setObjectName("availability_2")
        self.toolBox.addItem(self.analyst2, "")

        # ----------------- Analyst3 --------------------------------
        self.analyst3 = QtWidgets.QWidget()
        self.analyst3.setObjectName("analyst3")
        self.wsmSort_3 = QtWidgets.QCheckBox(self.analyst3)
        self.wsmSort_3.setGeometry(QtCore.QRect(310, 50, 111, 20))
        self.wsmSort_3.setObjectName("wsmSort_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.analyst3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 50, 191, 111))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.grid_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.grid_3.setContentsMargins(0, 0, 0, 0)
        self.grid_3.setObjectName("grid_3")
        self.earliestDate_3 = QtWidgets.QDateEdit(self.gridLayoutWidget_3)
        self.earliestDate_3.setDateTime(
            QtCore.QDateTime(QtCore.QDate(2023, 3, 13), QtCore.QTime(0, 0, 0))
        )
        self.earliestDate_3.setCalendarPopup(True)
        self.earliestDate_3.setDate(QtCore.QDate(2023, 3, 13))
        self.earliestDate_3.setObjectName("earliestDate_3")
        self.grid_3.addWidget(self.earliestDate_3, 3, 0, 1, 1)
        self.latestDate_3 = QtWidgets.QDateEdit(self.gridLayoutWidget_3)
        self.latestDate_3.setCalendarPopup(True)
        self.latestDate_3.setDate(QtCore.QDate(2022, 3, 19))
        self.latestDate_3.setObjectName("latestDate_3")
        self.grid_3.addWidget(self.latestDate_3, 2, 0, 1, 1)
        self.sortByDate_3 = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.sortByDate_3.setObjectName("sortByDate_3")
        self.grid_3.addWidget(self.sortByDate_3, 1, 0, 1, 1)
        self.rulesLabel_3 = QtWidgets.QLabel(self.analyst3)
        self.rulesLabel_3.setGeometry(QtCore.QRect(10, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.rulesLabel_3.setFont(font)
        self.rulesLabel_3.setObjectName("rulesLabel_3")
        self.bakeBtn_3 = QtWidgets.QPushButton(self.analyst3)
        self.bakeBtn_3.setGeometry(QtCore.QRect(360, 350, 111, 41))
        self.bakeBtn_3.setObjectName("bakeBtn_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.analyst3)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 310, 601, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.analyst3)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 250, 601, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.impactLabel_3 = QtWidgets.QLabel(self.analyst3)
        self.impactLabel_3.setGeometry(QtCore.QRect(520, 50, 181, 21))
        self.impactLabel_3.setObjectName("impactLabel_3")
        self.confideality_3 = QtWidgets.QCheckBox(self.analyst3)
        self.confideality_3.setGeometry(QtCore.QRect(550, 70, 101, 20))
        self.confideality_3.setObjectName("confideality_3")
        self.integrity_3 = QtWidgets.QCheckBox(self.analyst3)
        self.integrity_3.setGeometry(QtCore.QRect(550, 90, 81, 20))
        self.integrity_3.setObjectName("integrity_3")
        self.availability_3 = QtWidgets.QCheckBox(self.analyst3)
        self.availability_3.setGeometry(QtCore.QRect(550, 110, 111, 20))
        self.availability_3.setObjectName("availability_3")
        self.toolBox.addItem(self.analyst3, "")

        # -------------------------- Analyst4 -------------------------------
        self.analyst4 = QtWidgets.QWidget()
        self.analyst4.setObjectName("analyst4")
        self.wsmSort_4 = QtWidgets.QCheckBox(self.analyst4)
        self.wsmSort_4.setGeometry(QtCore.QRect(310, 60, 111, 20))
        self.wsmSort_4.setObjectName("wsmSort_4")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.analyst4)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 50, 191, 111))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.grid_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.grid_4.setContentsMargins(0, 0, 0, 0)
        self.grid_4.setObjectName("grid_4")
        self.earliestDate_4 = QtWidgets.QDateEdit(self.gridLayoutWidget_4)
        self.earliestDate_4.setDateTime(
            QtCore.QDateTime(QtCore.QDate(2023, 3, 13), QtCore.QTime(0, 0, 0))
        )
        self.earliestDate_4.setCalendarPopup(True)
        self.earliestDate_4.setDate(QtCore.QDate(2023, 3, 13))
        self.earliestDate_4.setObjectName("earliestDate_4")
        self.grid_4.addWidget(self.earliestDate_4, 2, 0, 1, 1)
        self.sortByDate_4 = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.sortByDate_4.setObjectName("sortByDate_4")
        self.grid_4.addWidget(self.sortByDate_4, 0, 0, 1, 1)
        self.latestDate_4 = QtWidgets.QDateEdit(self.gridLayoutWidget_4)
        self.latestDate_4.setCalendarPopup(True)
        self.latestDate_4.setDate(QtCore.QDate(2022, 3, 19))
        self.latestDate_4.setObjectName("latestDate_4")
        self.grid_4.addWidget(self.latestDate_4, 1, 0, 1, 1)
        self.rulesLabel_4 = QtWidgets.QLabel(self.analyst4)
        self.rulesLabel_4.setGeometry(QtCore.QRect(10, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.rulesLabel_4.setFont(font)
        self.rulesLabel_4.setObjectName("rulesLabel_4")
        self.bakeBtn_4 = QtWidgets.QPushButton(self.analyst4)
        self.bakeBtn_4.setGeometry(QtCore.QRect(360, 340, 111, 41))
        self.bakeBtn_4.setObjectName("bakeBtn_4")
        self.lineEdit = QtWidgets.QLineEdit(self.analyst4)
        self.lineEdit.setGeometry(QtCore.QRect(10, 220, 601, 22))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.analyst4)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 280, 601, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.impactLabel_4 = QtWidgets.QLabel(self.analyst4)
        self.impactLabel_4.setGeometry(QtCore.QRect(520, 60, 181, 21))
        self.impactLabel_4.setObjectName("impactLabel_4")
        self.confideality_4 = QtWidgets.QCheckBox(self.analyst4)
        self.confideality_4.setGeometry(QtCore.QRect(540, 80, 101, 20))
        self.confideality_4.setObjectName("confideality_4")
        self.integrity_4 = QtWidgets.QCheckBox(self.analyst4)
        self.integrity_4.setGeometry(QtCore.QRect(540, 100, 81, 20))
        self.integrity_4.setObjectName("integrity_4")
        self.availability_4 = QtWidgets.QCheckBox(self.analyst4)
        self.availability_4.setGeometry(QtCore.QRect(540, 120, 101, 20))
        self.availability_4.setObjectName("availability_4")
        self.toolBox.addItem(self.analyst4, "")

        self.ExitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ExitBtn.setGeometry(QtCore.QRect(460, 730, 81, 28))
        self.ExitBtn.setObjectName("ExitBtn")
        self.ExitBtn.clicked.connect(lambda: self.openLogin(AdminPage))

        self.importCsvBtn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.importCsvBtn.setGeometry(QtCore.QRect(390, 60, 191, 71))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\utils\\Images\\csv1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importCsvBtn.setIcon(icon1)
        self.importCsvBtn.setIconSize(QtCore.QSize(45, 80))
        self.importCsvBtn.setCheckable(False)
        self.importCsvBtn.setObjectName("importCsvBtn")
        self.importCsvBtn.clicked.connect(lambda: self.fileDialog())

        AdminPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminPage)
        QtCore.QMetaObject.connectSlotsByName(AdminPage)

    def retranslateUi(self, AdminPage):
        _translate = QtCore.QCoreApplication.translate
        AdminPage.setWindowTitle(_translate("AdminPage", "Admins Page"))
        self.welcomeLbl.setText(
            _translate("AdminPage", "Welcome to Administrator Page!")
        )
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.rawData), _translate("AdminPage", "Raw Data")
        )
        self.rulesLabel.setText(_translate("AdminPage", "Rules for Analyst:"))
        self.sortByDate.setText(_translate("AdminPage", "Sort by Date"))
        self.wsmSort.setText(_translate("AdminPage", "WSM rating"))
        self.bakeBtn.setText(_translate("AdminPage", "Bake Rules"))
        self.impactLabel.setText(_translate("AdminPage", "Potential Impact values:"))
        self.confideality.setText(_translate("AdminPage", "Confideality"))
        self.integrity.setText(_translate("AdminPage", "Integrity"))
        self.availability.setText(_translate("AdminPage", "Availability"))
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.analyst1), _translate("AdminPage", "Analyst1")
        )
        self.rulesLabel_2.setText(_translate("AdminPage", "Rules for Analyst:"))
        self.sortByDate_2.setText(_translate("AdminPage", "Sort by Date"))
        self.wsmSort_2.setText(_translate("AdminPage", "WSM rating"))
        self.bakeBtn_2.setText(_translate("AdminPage", "Bake Rules"))
        self.impactLabel_2.setText(_translate("AdminPage", "Potential Impact values:"))
        self.confideality_2.setText(_translate("AdminPage", "Confideality"))
        self.integrity_2.setText(_translate("AdminPage", "Integrity"))
        self.availability_2.setText(_translate("AdminPage", "Availability"))
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.analyst2), _translate("AdminPage", "Analyst2")
        )
        self.wsmSort_3.setText(_translate("AdminPage", "WSM rating"))
        self.sortByDate_3.setText(_translate("AdminPage", "Sort by Date"))
        self.rulesLabel_3.setText(_translate("AdminPage", "Rules for Analyst:"))
        self.bakeBtn_3.setText(_translate("AdminPage", "Bake Rules"))
        self.impactLabel_3.setText(_translate("AdminPage", "Potential Impact values:"))
        self.confideality_3.setText(_translate("AdminPage", "Confideality"))
        self.integrity_3.setText(_translate("AdminPage", "Integrity"))
        self.availability_3.setText(_translate("AdminPage", "Availability"))
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.analyst3), _translate("AdminPage", "Analyst3")
        )
        self.wsmSort_4.setText(_translate("AdminPage", "WSM rating"))
        self.sortByDate_4.setText(_translate("AdminPage", "Sort by Date"))
        self.rulesLabel_4.setText(_translate("AdminPage", "Rules for Analyst:"))
        self.bakeBtn_4.setText(_translate("AdminPage", "Bake Rules"))
        self.impactLabel_4.setText(_translate("AdminPage", "Potential Impact values:"))
        self.confideality_4.setText(_translate("AdminPage", "Confideality"))
        self.integrity_4.setText(_translate("AdminPage", "Integrity"))
        self.availability_4.setText(_translate("AdminPage", "Availability"))
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.analyst4), _translate("AdminPage", "Analyst4")
        )
        self.ExitBtn.setText(_translate("AdminPage", "Exit"))
        self.importCsvBtn.setText(_translate("AdminPage", "  Import CSV"))

    def fileDialog(self):
        self.csvTuple = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "File Explorer",
            "",
            "All Files (*);;Python Files (*.py);;Text Files (*.txt)",
        )
        self.CSV = self.csvTuple[0]
        print(self.CSV)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AdminPage = QtWidgets.QMainWindow()
    ui = Ui_AdminPage()
    ui.setupUi(AdminPage)
    AdminPage.show()
    sys.exit(app.exec_())
