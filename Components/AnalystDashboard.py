from utils import routes
from Components import Login
from utils.Helpers.AnalystHelper import *
from utils.Helpers.GeneralHelpers import fillTableData
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnalystDashboard(object):
    def __init__(self):
        self.analystDf = None
        self.rulesForUser = None
        self.currUser = None
        self.loginUi = None
        self.LoginWindow = None
        self.welcomeUserPageLbl = None
        self.fireBtn = None
        self.doneRadioBtn = None
        self.inProgressRadioBtn = None
        self.exitBtn = None
        self.issuesComboBox = None
        self.currTime = None
        self.timer = None
        self.tasksTableView = None

    def updateAnalystTable(self):
        fixedAnalystDf = self.analystDf.astype(str)
        fillTableData(fixedAnalystDf, self.tasksTableView)

    def initCombo(self, itemsList=None):
        if itemsList is None:
            itemsList = [i for i in range(1, 11)]
        updateIssuesComboBox(self.issuesComboBox, itemsList)

    def openLoginWindow(self, AnalystDashboard):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.loginUi = Login.UiLogIn()
        self.loginUi.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        AnalystDashboard.close()

    def displayTime(self):
        currenTime = QtCore.QTime.currentTime()
        displayTime = currenTime.toString("hh:mm:ss")
        self.currTime.setDigitCount(8)
        self.currTime.display(displayTime)

    def setupUi(self, AnalystDashboard):
        AnalystDashboard.setObjectName("AnalystDashboard")
        AnalystDashboard.resize(1255, 633)
        AnalystDashboard.setWindowIcon(QtGui.QIcon(routes.sceLogo))
        AnalystDashboard.setWindowTitle("Analyst Dashboard")

        self.welcomeUserPageLbl = QtWidgets.QLabel(AnalystDashboard)
        self.welcomeUserPageLbl.setGeometry(QtCore.QRect(430, 30, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.welcomeUserPageLbl.setFont(font)
        self.welcomeUserPageLbl.setObjectName("welcomeUserPageLbl")
        self.welcomeUserPageLbl.setText("Welcome to Analyst Page!")

        self.fireBtn = QtWidgets.QPushButton(AnalystDashboard)
        self.fireBtn.setGeometry(QtCore.QRect(90, 550, 93, 28))
        self.fireBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fireBtn.setDefault(False)
        self.fireBtn.setObjectName("fireBtn")
        self.fireBtn.setText("Fire")
        self.fireBtn.clicked.connect(
            lambda: updateIssueStatus(self.analystDf, self.currUser, self.issuesComboBox, self.inProgressRadioBtn,
                                      self.doneRadioBtn))

        self.exitBtn = QtWidgets.QPushButton(AnalystDashboard)
        self.exitBtn.setGeometry(QtCore.QRect(1110, 580, 93, 28))
        self.exitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitBtn.setAutoFillBackground(False)
        self.exitBtn.setObjectName("exitBtn")
        self.exitBtn.setText("Exit")
        self.exitBtn.clicked.connect(lambda: self.openLoginWindow(AnalystDashboard))

        self.currTime = QtWidgets.QLCDNumber(AnalystDashboard)
        self.currTime.setGeometry(QtCore.QRect(1070, 10, 161, 61))
        self.currTime.setObjectName("currTime")

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.displayTime)
        self.timer.start(50)

        self.issuesComboBox = QtWidgets.QComboBox(AnalystDashboard)
        self.issuesComboBox.setGeometry(QtCore.QRect(20, 500, 251, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.issuesComboBox.sizePolicy().hasHeightForWidth())
        self.issuesComboBox.setSizePolicy(sizePolicy)
        self.issuesComboBox.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.issuesComboBox.setObjectName("issuesComboBox")

        self.inProgressRadioBtn = QtWidgets.QRadioButton(AnalystDashboard)
        self.inProgressRadioBtn.setGeometry(QtCore.QRect(280, 500, 95, 20))
        self.inProgressRadioBtn.setObjectName("inProgressRadioBtn")
        self.inProgressRadioBtn.setText("In Progress")

        # set as default instead of checking if none of radioBtn is chosen
        self.inProgressRadioBtn.setChecked(True)

        self.doneRadioBtn = QtWidgets.QRadioButton(AnalystDashboard)
        self.doneRadioBtn.setGeometry(QtCore.QRect(280, 530, 95, 20))
        self.doneRadioBtn.setObjectName("doneRadioBtn")
        self.doneRadioBtn.setText("Done")

        self.tasksTableView = QtWidgets.QTableWidget(AnalystDashboard)
        self.tasksTableView.setGeometry(QtCore.QRect(20, 80, 1211, 411))
        self.tasksTableView.setObjectName("tasksTableView")
        self.tasksTableView.setColumnCount(0)
        self.tasksTableView.setRowCount(0)

        self.currUser = getUserName()
        self.rulesForUser = getUserRules(self.currUser)
        print("currUser: ", self.currUser)
        print("rulesForUser: ", self.rulesForUser)

        # Start all helper funcs
        self.analystDf = getFilteredTable(self.rulesForUser, self.currUser)
        self.initCombo(getIssuesId(self.analystDf))
        self.updateAnalystTable()

        # This line needs to be the last one in the class
        QtCore.QMetaObject.connectSlotsByName(AnalystDashboard)
