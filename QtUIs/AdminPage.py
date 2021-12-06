from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class UiAdminPage(object):
    def setupUi(self, AdminPage):
        AdminPage.setObjectName("AdminPage")
        AdminPage.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/SCElogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AdminPage.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(AdminPage)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomeLbl = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLbl.setGeometry(QtCore.QRect(200, 40, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.welcomeLbl.setFont(font)
        self.welcomeLbl.setObjectName("welcomeLbl")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(340, 100, 135, 80))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.ExitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ExitBtn.setGeometry(QtCore.QRect(670, 550, 93, 28))
        self.ExitBtn.setObjectName("ExitBtn")
        self.ExitBtn.clicked.connect(AdminPage.close)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(340, 180, 81, 20))
        self.checkBox.setObjectName("checkBox")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(340, 220, 95, 20))
        self.radioButton.setObjectName("radioButton")

        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(300, 400, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.importCsvBtn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.importCsvBtn.setGeometry(QtCore.QRect(280, 310, 222, 48))
        self.importCsvBtn.setObjectName("importCsvBtn")
        AdminPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminPage)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminPage)

    def retranslateUi(self, AdminPage):
        _translate = QtCore.QCoreApplication.translate
        AdminPage.setWindowTitle(_translate("AdminPage", "Admins Page"))
        self.welcomeLbl.setText(_translate("AdminPage", "Welcome to Administrator Page!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("AdminPage", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AdminPage", "Tab 2"))
        self.ExitBtn.setText(_translate("AdminPage", "Exit"))
        self.checkBox.setText(_translate("AdminPage", "CheckBox"))
        self.radioButton.setText(_translate("AdminPage", "RadioButton"))
        self.importCsvBtn.setText(_translate("AdminPage", "Import Csv"))

def Exit(self):
    self.close()

def RunAdminPage():
    app = QtWidgets.QApplication(sys.argv)
    AdminPage = QtWidgets.QMainWindow()
    ui = UiAdminPage()
    ui.setupUi(AdminPage)
    AdminPage.show()
    sys.exit(app.exec_())