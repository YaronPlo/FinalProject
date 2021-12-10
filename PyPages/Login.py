from PyQt5 import QtCore, QtGui, QtWidgets
from PyPages import AdminPage, UserPage
import sys
import json

# import time

fileDB = ".\\info.json"


class UiLogIn(object):
    global fileDB

    def __init__(self):
        self.plainTextEdit = None
        self.UserWindow = None
        self.userNameLbl = None
        self.userNameInput = None
        self.passwordLbl = None
        self.passwordInput = None
        self.AdminWindow = None
        self.logIn = None
        self.Register = None
        self.ui = None

    def openAdminPage(self, LogIn):
        self.AdminWindow = QtWidgets.QMainWindow()
        self.ui = AdminPage.UiAdminPage()
        self.ui.setupUi(self.AdminWindow)
        self.AdminWindow.show()
        LogIn.close()

    def openUserPage(self, LogIn):
        self.UserWindow = QtWidgets.QMainWindow()
        self.ui = UserPage.UiUserPage()
        self.ui.setupUi(self.UserWindow)
        self.UserWindow.show()
        LogIn.close()

    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(333, 265)
        LogIn.setMouseTracking(False)
        LogIn.setWindowIcon(QtGui.QIcon('.\\Images\\SCElogo.png'))

        self.userNameInput = QtWidgets.QLineEdit(LogIn)
        self.userNameInput.setGeometry(QtCore.QRect(120, 60, 113, 22))
        self.userNameInput.setObjectName("userNameInput")

        self.userNameLbl = QtWidgets.QLabel(LogIn)
        self.userNameLbl.setGeometry(QtCore.QRect(30, 60, 81, 20))
        self.userNameLbl.setObjectName("userNameLbl")

        self.passwordLbl = QtWidgets.QLabel(LogIn)
        self.passwordLbl.setGeometry(QtCore.QRect(30, 110, 81, 20))
        self.passwordLbl.setObjectName("passwordLbl")

        self.passwordInput = QtWidgets.QLineEdit(LogIn)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setGeometry(QtCore.QRect(120, 110, 113, 22))
        self.passwordInput.setObjectName("passwordInput")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(LogIn)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 210, 191, 31))
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.logIn = QtWidgets.QPushButton(LogIn)
        self.logIn.setGeometry(QtCore.QRect(50, 170, 93, 28))
        self.logIn.setObjectName("logIn")
        self.logIn.clicked.connect(lambda: self.LoginCheck(LogIn))

        self.Register = QtWidgets.QPushButton(LogIn)
        self.Register.setGeometry(QtCore.QRect(190, 170, 93, 28))
        self.Register.setObjectName("Register")
        self.Register.clicked.connect(self.write_json)

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "Log In"))
        self.logIn.setText(_translate("LogIn", "Log In"))
        self.Register.setText(_translate("LogIn", "Register"))
        self.userNameLbl.setText(_translate("LogIn", "User Name:"))
        self.passwordLbl.setText(_translate("LogIn", "Password:"))

    # Function that writes to JSON the userName and Password
    def write_json(self):
        newDate = {
            "Username": self.userNameInput.text(),
            "Password": self.passwordInput.text()
        }
        if self.userNameInput.text() == "" and self.passwordInput.text() == "":
            self.plainTextEdit.setPlainText("Invalid Username & Password!")
            self.plainTextEdit.setStyleSheet("color: red")
            return

        if self.CheckUserExistence():
            with open(fileDB, "r+") as DB:
                # First we load existing data into a dict.
                dataBase = json.load(DB)
                # Join new_data with file_data inside user_details
                dataBase["userDetails"].append(newDate)
                # Sets DB's current position at offset.
                DB.seek(0)
                # convert back to json.
                json.dump(dataBase, DB, indent=3)

                self.plainTextEdit.setPlainText("Succesfully added new User")
                self.plainTextEdit.setStyleSheet("color: green")

    # function checks if the userName Exists
    def CheckUserExistence(self):
        with open(fileDB, "r") as DB:
            dataBase = json.load(DB)
        for user in dataBase["userDetails"]:
            if user["Username"] == self.userNameInput.text():
                self.plainTextEdit.setPlainText("User name already exists!")
                self.plainTextEdit.setStyleSheet("color: red")
                return False
        return True

    def TypeUserCheck(self):
        pass

    def LoginCheck(self, LogIn):
        with open(fileDB, "r") as DB:
            dataBase = json.load(DB)
        for user in dataBase["userDetails"]:
            if self.userNameInput.text() == "" or self.passwordInput.text() == "":
                self.plainTextEdit.setPlainText("input Wrong!")
                self.plainTextEdit.setStyleSheet("color: red")
                return
            if user["Username"] == self.userNameInput.text() and user["Password"] == self.passwordInput.text():
                self.plainTextEdit.setPlainText("Success!")
                self.plainTextEdit.setStyleSheet("color: green")
                if self.userNameInput.text() == "123":
                    self.openAdminPage(LogIn)
                    return
                elif self.userNameInput.text() == "1232":
                    self.openUserPage(LogIn)
                    return
        self.plainTextEdit.setPlainText("User Doesn't Exists!")
        self.plainTextEdit.setStyleSheet("color: red")

    def UpdateMessage(self):
        if self.plainTextEdit.toPlainText() != "":
            self.plainTextEdit.setPlainText("")


def RunLogIn():
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QWidget()
    ui = UiLogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())
