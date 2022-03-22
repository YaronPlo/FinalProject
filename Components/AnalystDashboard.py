import json
from utils import routes
from Components import Login
import Data.Utilities as Data
from PyQt5 import QtCore, QtGui, QtWidgets


def getUserName():
    with open(routes.usersFile) as DB:
        userDB = json.load(DB)

    return userDB["currentUser"]


def getUserRules(UserID):
    with open(routes.rulesFile) as rules:
        rulesDB = json.load(rules)
    with open(routes.usersFile) as users:
        usersDB = json.load(users)

    for analyst in usersDB["userDetails"]:
        if analyst["Username"] == UserID:
            userRules = analyst["analyst"]

    return rulesDB[userRules]


def getFilteredTable(rules):
    main_df = Data.dataFrame
    description = 'Description'
    Potential_Impact = 'Potential Impact'
    potential_impact_values = ["confidentiality", "integrity", "availability"]

    func_dict = {
        "wsm": Data.WSM,
        "date": Data.sorting_df,
    }

    potential_impact_items = [val for val in potential_impact_values if rules[val]]

    key_word_values = {
        "include": Data.show_only,  # Text
        "exclude": Data.dont_show,  # Text
    }

    for key, value in func_dict.items():
        if rules[key]:
            func_dict[key](main_df)

    for key, value in key_word_values.items():
        if rules[key] != '':
            main_df = key_word_values[key](main_df, description, [rules[key].lower()])

    for item in potential_impact_items:
        main_df = Data.show_only(main_df, Potential_Impact, [item])

    print(main_df.head().to_string())


def updateIssuesComboBox(issueComboBox, itemsList):
    fixedItemsList = map(lambda x: x if isinstance(x, str) else str(x), itemsList)
    issueComboBox.addItems(fixedItemsList)


class Ui_AnalystDashboard(object):
    def __init__(self):
        self.rulesForUser = None
        self.currUser = None

        self.loginUi = None
        self.LoginWindow = None

        self.tasksProgressLbl = None
        self.welcomeUserPageLbl = None

        self.fireBtn = None
        self.doneRadioBtn = None
        self.inProgressRadioBtn = None
        self.exitBtn = None

        self.issuesComboBox = None
        self.tasksProgressBar = None
        self.currTime = None
        self.timer = None
        self.tasksTableView = None

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

        self.tasksProgressLbl = QtWidgets.QLabel(AnalystDashboard)
        self.tasksProgressLbl.setGeometry(QtCore.QRect(790, 510, 101, 16))
        self.tasksProgressLbl.setObjectName("tasksProgressLbl")
        self.tasksProgressLbl.setText("Tasks Progress:")

        self.fireBtn = QtWidgets.QPushButton(AnalystDashboard)
        self.fireBtn.setGeometry(QtCore.QRect(90, 550, 93, 28))
        self.fireBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fireBtn.setDefault(False)
        self.fireBtn.setObjectName("fireBtn")
        self.fireBtn.setText("Fire")

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

        self.tasksProgressBar = QtWidgets.QProgressBar(AnalystDashboard)
        self.tasksProgressBar.setGeometry(QtCore.QRect(900, 502, 331, 31))
        self.tasksProgressBar.setProperty("value", 50)
        self.tasksProgressBar.setObjectName("tasksProgressBar")

        self.issuesComboBox = QtWidgets.QComboBox(AnalystDashboard)
        self.issuesComboBox.setGeometry(QtCore.QRect(20, 500, 251, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.issuesComboBox.sizePolicy().hasHeightForWidth())
        self.issuesComboBox.setSizePolicy(sizePolicy)
        self.issuesComboBox.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.issuesComboBox.setObjectName("issuesComboBox")
        updateIssuesComboBox(self.issuesComboBox, [1, "2", 3, 4, "5"])

        self.inProgressRadioBtn = QtWidgets.QRadioButton(AnalystDashboard)
        self.inProgressRadioBtn.setGeometry(QtCore.QRect(280, 500, 95, 20))
        self.inProgressRadioBtn.setObjectName("inProgressRadioBtn")
        self.inProgressRadioBtn.setText("In Progress")

        self.doneRadioBtn = QtWidgets.QRadioButton(AnalystDashboard)
        self.doneRadioBtn.setGeometry(QtCore.QRect(280, 530, 95, 20))
        self.doneRadioBtn.setObjectName("doneRadioBtn")
        self.doneRadioBtn.setText("Done")

        self.tasksTableView = QtWidgets.QTableView(AnalystDashboard)
        self.tasksTableView.setGeometry(QtCore.QRect(20, 80, 1211, 411))
        self.tasksTableView.setObjectName("tasksTableView")

        self.currUser = getUserName()
        self.rulesForUser = getUserRules(self.currUser)
        print("currUser: ", self.currUser)
        print("rulesForUser: ", self.rulesForUser)
        getFilteredTable(self.rulesForUser)

        # This line needs to be the last one in the class
        QtCore.QMetaObject.connectSlotsByName(AnalystDashboard)

# def runAnalystDashbard():
#     app = QtWidgets.QApplication(sys.argv)
#     AnalystDashboard = QtWidgets.QWidget()
#     ui = Ui_AnalystDashboard()
#     ui.setupUi(AnalystDashboard)
#     AnalystDashboard.show()
#     sys.exit(app.exec_())
