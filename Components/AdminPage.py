from PyQt5 import QtCore, QtGui, QtWidgets
from Components import Login
import csv
import json
import sys

fileDB = ".\\info.json"


class UiAdminPage(object):
    def __init__(self):
        self.csvTuple = None
        self.filterBox2 = None
        self.filterBox3 = None
        self.filterBox4 = None
        self.filterBox5 = None
        self.filterLbl = None
        self.CSV = None
        self.importCsvBtn = None
        self.filterBox1 = None
        self.ExitBtn = None
        self.filteredDataListWidget = None
        self.FilteredData = None
        self.rawDataTableWidget = None
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
        self.rawDataTableWidget = QtWidgets.QTableWidget(self.rawCSVdata)
        self.rawDataTableWidget.setGeometry(QtCore.QRect(0, 0, 841, 471))
        self.rawDataTableWidget.setObjectName("rawDataTableWidget")
        self.rawDataTableWidget.setColumnCount(0)
        self.rawDataTableWidget.setRowCount(0)
        self.tabWidget.addTab(self.rawCSVdata, "")

        self.FilteredData = QtWidgets.QWidget()
        self.FilteredData.setObjectName("FilteredData")
        self.filteredDataListWidget = QtWidgets.QListWidget(self.FilteredData)
        self.filteredDataListWidget.setGeometry(QtCore.QRect(0, 0, 841, 471))
        self.filteredDataListWidget.setObjectName("filteredDataListWidget")
        self.tabWidget.addTab(self.FilteredData, "")

        self.ExitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ExitBtn.setGeometry(QtCore.QRect(890, 670, 93, 28))
        self.ExitBtn.setObjectName("ExitBtn")
        self.ExitBtn.clicked.connect(lambda: self.openLogin(AdminPage))

        self.importCsvBtn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.importCsvBtn.setGeometry(QtCore.QRect(410, 90, 191, 71))
        self.importCsvBtn.clicked.connect(lambda: self.fileDialog())
        # self.importCsvBtn.clicked.connect(lambda: self.parseAssetCSV())
        self.importCsvBtn.clicked.connect(lambda: self.parseTicketCSV())
        self.importCsvBtn.clicked.connect(lambda: self.fillTable())

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\Images\\csv1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importCsvBtn.setIcon(icon1)
        self.importCsvBtn.setIconSize(QtCore.QSize(45, 80))
        self.importCsvBtn.setObjectName("importCsvBtn")

        self.filterBox1 = QtWidgets.QCheckBox(self.centralwidget)
        self.filterBox1.setGeometry(QtCore.QRect(21, 228, 67, 20))
        self.filterBox1.setObjectName("filterBox1")

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

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rawCSVdata), _translate("AdminPage", "Raw Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FilteredData), _translate("AdminPage", "Filtered Data"))

        self.ExitBtn.setText(_translate("AdminPage", "Exit"))

        self.importCsvBtn.setText(_translate("AdminPage", "  Import CSV"))

        self.filterLbl.setText(_translate("AdminPage", "Filters:"))
        self.filterBox1.setText(_translate("AdminPage", "Filter 1"))
        self.filterBox2.setText(_translate("AdminPage", "Filter 2"))
        self.filterBox3.setText(_translate("AdminPage", "Filter 3"))
        self.filterBox4.setText(_translate("AdminPage", "Filter 4"))
        self.filterBox5.setText(_translate("AdminPage", "Filter 5"))

    def fileDialog(self):
        self.csvTuple = QtWidgets.QFileDialog.getOpenFileName(None, "File Explorer", "",
                                                              "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        self.CSV = self.csvTuple[0]
        print(self.CSV)

    # TODO: Continue paseCSV Function
    def parseAssetCSV(self):
        global fileDB
        with open(self.CSV, encoding='utf-8') as csvFile:
            csvReader = csv.DictReader(csvFile)
            with open(fileDB, 'r+', encoding='utf-8') as jsonDB:
                dataBase = json.load(jsonDB)
                for rows in csvReader:
                    data = rows
                    dataBase["Assets"].append(data)  # TODO: Change the indent
                jsonDB.seek(0)
                json.dump(dataBase, jsonDB, indent=3)


    def parseTicketCSV(self):
        global fileDB
        with open(self.CSV, encoding='utf-8') as csvFile:
            csvReader = csv.DictReader(csvFile)
            with open(fileDB, 'r+', encoding='utf-8') as jsonDB:
                dataBase = json.load(jsonDB)
                for rows in csvReader:
                    data = rows
                    dataBase["Tickets"].append(data)  # TODO: Change the indent
                jsonDB.seek(0)
                json.dump(dataBase, jsonDB, indent=3)

    def fillTable(self):
        global fileDB
        with open(fileDB, "r") as jsonDB:
            dataBase = json.load(jsonDB)
            # Make the Table Rows and Cols
            self.rawDataTableWidget.setRowCount(len(dataBase["Assets"]))
            self.rawDataTableWidget.setColumnCount(len(dataBase["Assets"][0]))
            # Fill the Headers in the Table
            self.rawDataTableWidget.setHorizontalHeaderLabels((key for key in dataBase["Assets"][0]))

            # for rowItem in range(dataBase["Assets"]):
            #     for columnItem in range(len(dataBase["Assets"][0])):
            #
            #         self.rawDataTableWidget.setItem(rowItem, columnItem, QtWidgets.QTableWidgetItem())

            for item in dataBase["Assets"]:
                print(item)




        print("Rows:")
        print(len(dataBase["Assets"]))
        print("Cols:")
        print(len(dataBase["Assets"][0]))




def RunAdminPage():
    app = QtWidgets.QApplication(sys.argv)
    AdminPage = QtWidgets.QMainWindow()
    ui = UiAdminPage()
    ui.setupUi(AdminPage)
    AdminPage.show()
    sys.exit(app.exec_())
