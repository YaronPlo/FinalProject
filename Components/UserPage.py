from PyQt5 import QtCore, QtGui, QtWidgets
from Components import Login
from utils import routes
import sys
import json
import Data.Utilities as Data


def getUserName():
    with open(routes.usersFile) as DB:
        userDB = json.load(DB)

    return userDB["currentUser"]


def getUserRuels(UserID):
    names = {"yaniv": "analyst_1"}
    with open(routes.rulesFile) as rules:
        rulesDB = json.load(rules)
    return rulesDB[names[UserID]]


def getFilteredTable(rules):
    main_df = Data.dataFrame
    print(main_df.to_string())
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
        main_df = Data.key_word(main_df, Potential_Impact, item)

    print(main_df.to_string())


class UiUserPage(object):
    def __init__(self):
        self.rulesForUser = None
        self.currUser = None
        self.List_of_unchecked = None
        self.List_of_checked = None
        self.List = None
        self.calendarWidget = None
        self.taskProgressBar = None
        self.graphicsView = None
        self.widget = None
        self.verticalLayout = None
        self.Task4 = None
        self.Task5 = None
        self.Task3 = None
        self.Task2 = None
        self.Task1 = None
        self.currTime = None
        self.timer = None
        self.exitBtn = None
        self.tasksLbl = None
        self.welcomeUserPageLbl = None
        self.ui = None
        self.LoginWindow = None

    def openLoginWindow(self, UserPage):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = Login.UiLogIn()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        UserPage.close()

    def setupUi(self, UserPage):
        UserPage.setObjectName("UserPage")
        UserPage.resize(857, 675)
        UserPage.setEnabled(True)
        UserPage.setWindowIcon(QtGui.QIcon(routes.sceLogo))

        self.tasksLbl = QtWidgets.QLabel(UserPage)
        self.tasksLbl.setGeometry(QtCore.QRect(70, 130, 69, 27))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)

        self.tasksLbl.setFont(font)
        self.tasksLbl.setObjectName("tasksLbl")

        self.welcomeUserPageLbl = QtWidgets.QLabel(UserPage)
        self.welcomeUserPageLbl.setGeometry(QtCore.QRect(280, 20, 351, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)

        self.welcomeUserPageLbl.setFont(font)
        self.welcomeUserPageLbl.setObjectName("welcomeUserPageLbl")

        self.exitBtn = QtWidgets.QPushButton(UserPage)
        self.exitBtn.setGeometry(QtCore.QRect(720, 620, 93, 28))
        self.exitBtn.setObjectName("exitBtn")
        self.exitBtn.clicked.connect(lambda: self.openLoginWindow(UserPage))

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.displayTime)
        self.timer.start(1000)

        self.currTime = QtWidgets.QLCDNumber(UserPage)
        self.currTime.setGeometry(QtCore.QRect(630, 120, 161, 61))
        self.currTime.setObjectName("currTime")
        self.currTime.setDigitCount(8)
        self.currTime.display("")

        self.calendarWidget = QtWidgets.QCalendarWidget(UserPage)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 430, 392, 236))
        self.calendarWidget.setObjectName("calendarWidget")

        self.taskProgressBar = QtWidgets.QProgressBar(UserPage)
        self.taskProgressBar.setGeometry(QtCore.QRect(70, 360, 118, 23))
        self.taskProgressBar.setProperty(
            "value", (10 / 100) * 100
        )  # TODO: Change it to dynamicly
        self.taskProgressBar.setObjectName("taskProgressBar")

        self.graphicsView = QtWidgets.QGraphicsView(UserPage)
        self.graphicsView.setGeometry(QtCore.QRect(250, 120, 341, 271))
        self.graphicsView.setObjectName("graphicsView")

        self.widget = QtWidgets.QWidget(UserPage)
        self.widget.setGeometry(QtCore.QRect(60, 170, 91, 170))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.Task1 = QtWidgets.QCheckBox(self.widget)
        self.Task1.setObjectName("Task1")

        self.verticalLayout.addWidget(self.Task1)

        self.Task2 = QtWidgets.QCheckBox(self.widget)
        self.Task2.setObjectName("Task2")
        self.verticalLayout.addWidget(self.Task2)

        self.Task3 = QtWidgets.QCheckBox(self.widget)
        self.Task3.setObjectName("Task3")
        self.verticalLayout.addWidget(self.Task3)

        self.Task4 = QtWidgets.QCheckBox(self.widget)
        self.Task4.setObjectName("Task4")
        self.verticalLayout.addWidget(self.Task4)

        self.Task5 = QtWidgets.QCheckBox(self.widget)
        self.Task5.setObjectName("Task5")

        self.verticalLayout.addWidget(self.Task5)

        self.retranslateUi(UserPage)
        QtCore.QMetaObject.connectSlotsByName(UserPage)

        self.currUser = getUserName()
        self.rulesForUser = getUserRuels(self.currUser)
        print("currUser: ", self.currUser)
        print("rulesForUser: ", self.rulesForUser)
        getFilteredTable(self.rulesForUser)

    def displayTime(self):
        currenTime = QtCore.QTime.currentTime()
        displayTime = currenTime.toString("hh:mm:ss")
        self.currTime.setDigitCount(8)
        self.currTime.display(displayTime)

    # TODO: Fix Checked Boxes
    def countCheckedBox(self):
        self.List = [
            (self.Task1.isChecked(), "Task1"),
            (self.Task2.isChecked(), "Task2"),
            (self.Task3.isChecked(), "Task3"),
            (self.Task4.isChecked(), "Task4"),
            (self.Task5.isChecked(), "Task5"),
        ]
        self.List_of_checked = []
        self.List_of_unchecked = []

        with open(routes.usersFile, "w") as DB:
            dataBase = json.load(DB)
            # for task in dataBase["Tasks"]:
            for i, v in self.List:
                if i:
                    self.List_of_checked.append(v)
                    dataBase["Task"].append({"isCompleted": i})
                else:
                    self.List_of_unchecked.append(v)
                    dataBase["Task"].append({"isCompleted": i})

    def retranslateUi(self, UserPage):
        _translate = QtCore.QCoreApplication.translate
        UserPage.setWindowTitle(_translate("UserPage", "User Page"))
        self.exitBtn.setText(_translate("UserPage", "Exit"))
        self.tasksLbl.setText(_translate("UserPage", "Tasks:"))
        self.welcomeUserPageLbl.setText(_translate("UserPage", "Welcome to User Page!"))
        self.Task1.setText(_translate("UserPage", "Task 1"))
        self.Task2.setText(_translate("UserPage", "Task 2"))
        self.Task3.setText(_translate("UserPage", "Task 3"))
        self.Task4.setText(_translate("UserPage", "Task 4"))
        self.Task5.setText(_translate("UserPage", "Task 5"))


def RunUserPage():
    app = QtWidgets.QApplication(sys.argv)
    UserPage = QtWidgets.QWidget()
    ui = UiUserPage()
    ui.setupUi(UserPage)
    UserPage.show()
    sys.exit(app.exec_())
