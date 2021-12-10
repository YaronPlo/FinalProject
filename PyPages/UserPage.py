from PyQt5 import QtCore, QtGui, QtWidgets
from PyPages import Login
import sys

class UiUserPage(object):

    def openLoginWindow(self, UserPage):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = Login.UiLogIn()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        UserPage.close()

    def setupUi(self, UserPage):
        UserPage.setObjectName("UserPage")
        UserPage.resize(857, 675)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/SCElogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        UserPage.setWindowIcon(icon)

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
        self.exitBtn.clicked.connect(lambda : self.openLoginWindow(UserPage))

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
        self.taskProgressBar.setProperty("value", (50/100)*100)
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



    def displayTime(self):
        currenTime = QtCore.QTime.currentTime()
        displayTime = currenTime.toString('hh:mm:ss')
        self.currTime.setDigitCount(8)
        self.currTime.display(displayTime)


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