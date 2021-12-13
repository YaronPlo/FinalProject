from PyQt5 import QtCore, QtGui, QtWidgets
from PyPages import Login
import csv
import json
import sys

fileDB = ".\\info.json"


class UiAdminPage(object):
    def __init__(self):
        self.filterBox2 = None
        self.filterBox3 = None
        self.filterBox4 = None
        self.filterBox5 = None
        self.filterLbl = None
        self.CSV = None
        self.importCsvBtn = None
        self.filterBox1 = None
        self.ExitBtn = None
        self.listViewData = None
        self.FilteredData = None
        self.tableData = None
        self.rawCSVdata = None
        self.tabWidget = None
        self.welcomeLbl = None
        self.centralwidget = None
        self.LoginWindow = None
        self.ui = None

    def openLogin(self, AdminPage):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = Login.UiLogIn()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        AdminPage.close()

    def setupUi(self, AdminPage):
        AdminPage.setObjectName("AdminPage")
        AdminPage.resize(1024, 768)
        AdminPage.setWindowIcon(QtGui.QIcon('.\\Images\\SCElogo.png'))

        self.centralwidget = QtWidgets.QWidget(AdminPage)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomeLbl = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLbl.setGeometry(QtCore.QRect(250, 40, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.welcomeLbl.setFont(font)
        self.welcomeLbl.setObjectName("welcomeLbl")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(130, 150, 851, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.rawCSVdata = QtWidgets.QWidget()
        self.rawCSVdata.setObjectName("rawCSVdata")
        self.tableData = QtWidgets.QTableView(self.rawCSVdata)
        self.tableData.setGeometry(QtCore.QRect(0, 0, 841, 471))
        self.tableData.setObjectName("tableData")
        self.tabWidget.addTab(self.rawCSVdata, "")
        self.FilteredData = QtWidgets.QWidget()
        self.FilteredData.setObjectName("FilteredData")
        self.listViewData = QtWidgets.QListView(self.FilteredData)
        self.listViewData.setGeometry(QtCore.QRect(0, 0, 841, 471))
        self.listViewData.setObjectName("listViewData")
        self.tabWidget.addTab(self.FilteredData, "")
        self.ExitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ExitBtn.setGeometry(QtCore.QRect(890, 670, 93, 28))
        self.ExitBtn.setObjectName("ExitBtn")
        self.ExitBtn.clicked.connect(lambda: self.openLogin(AdminPage))


        self.filterBox1 = QtWidgets.QCheckBox(self.centralwidget)
        self.filterBox1.setGeometry(QtCore.QRect(21, 228, 67, 20))
        self.filterBox1.setObjectName("filterBox1")

        self.importCsvBtn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.importCsvBtn.setGeometry(QtCore.QRect(410, 90, 191, 71))
        self.importCsvBtn.clicked.connect(lambda: self.fileDialog())
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\Images\\csv1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importCsvBtn.setIcon(icon1)
        self.importCsvBtn.setIconSize(QtCore.QSize(45, 80))
        self.importCsvBtn.setObjectName("importCsvBtn")

        self.filterBox2 = QtWidgets.QCheckBox(self.centralwidget)
        self.filterBox2.setGeometry(QtCore.QRect(21, 255, 67, 20))
        self.filterBox2.setObjectName("filterBox2")
        self.filterBox3 = QtWidgets.QCheckBox(self.centralwidget)
        self.filterBox3.setGeometry(QtCore.QRect(21, 201, 67, 20))
        self.filterBox3.setObjectName("filterBox3")
        self.filterBox4 = QtWidgets.QCheckBox(self.centralwidget)
        self.filterBox4.setGeometry(QtCore.QRect(21, 309, 67, 20))
        self.filterBox4.setObjectName("filterBox4")
        self.filterBox5 = QtWidgets.QCheckBox(self.centralwidget)
        self.filterBox5.setGeometry(QtCore.QRect(21, 282, 67, 20))
        self.filterBox5.setObjectName("filterBox5")
        self.filterLbl = QtWidgets.QLabel(self.centralwidget)
        self.filterLbl.setGeometry(QtCore.QRect(10, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.filterLbl.setFont(font)
        self.filterLbl.setObjectName("filterLbl")
        AdminPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminPage)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminPage)

    def retranslateUi(self, AdminPage):
        _translate = QtCore.QCoreApplication.translate
        AdminPage.setWindowTitle(_translate("AdminPage", "Admins Page"))
        self.welcomeLbl.setText(_translate("AdminPage", "Welcome to Administrator Page!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rawCSVdata), _translate("AdminPage", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FilteredData), _translate("AdminPage", "Tab 2"))
        self.ExitBtn.setText(_translate("AdminPage", "Exit"))
        self.filterBox1.setText(_translate("AdminPage", "Filter 2"))
        self.importCsvBtn.setText(_translate("AdminPage", "  Import CSV"))
        self.filterBox2.setText(_translate("AdminPage", "Filter 3"))
        self.filterBox3.setText(_translate("AdminPage", "Filter 1"))
        self.filterBox4.setText(_translate("AdminPage", "Filter 5"))
        self.filterBox5.setText(_translate("AdminPage", "Filter 4"))
        self.filterLbl.setText(_translate("AdminPage", "Filters:"))


    def fileDialog(self):
        self.CSV = QtWidgets.QFileDialog.getOpenFileName(None, "File Explorer", "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        print(self.CSV)

    # TODO: Continue paseCSV Function
    def parseCSV(self):
        data = {}
        global fileDB

        # Open a csv reader called DictReader
        with open(self.CSV[0], encoding='utf-8') as csvFile:
            csvReader = csv.DictReader(csvFile)

            # Convert each row into a dictionary
            # and add it to data
            for rows in csvReader:
                key = rows['No']
                data[key] = rows

                # Open a json writer, and use the json.dumps()
                # function to dump data
            with open(fileDB, 'w', encoding='utf-8') as jsonDB:
                jsonDB.write(json.dumps(data, indent=4))  # TODO: Change the indent


def RunAdminPage():
    app = QtWidgets.QApplication(sys.argv)
    AdminPage = QtWidgets.QMainWindow()
    ui = UiAdminPage()
    ui.setupUi(AdminPage)
    AdminPage.show()
    sys.exit(app.exec_())
