import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtTest import QTest

from Components import Login
from utils import routes


def CheckUserExistence(username, textbox):
    with open(routes.usersFile) as DB:
        dataBase = json.load(DB)
    for user in dataBase["userDetails"]:
        if user["Username"] == username:
            textbox.setPlainText("User name already exists!")
            textbox.setStyleSheet("color: red")
            QTest.qWait(1000)
            textbox.setPlainText("")
            return True
    return False


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(310, 263)
        Register.setWindowTitle("Register")
        Register.setMouseTracking(False)
        Register.setAcceptDrops(False)
        Register.setWindowIcon(QtGui.QIcon(routes.sceLogo))

        self.RegisterBtn = QtWidgets.QPushButton(Register, clicked=lambda: self.registerToJSON())
        self.RegisterBtn.setText("Register")
        self.RegisterBtn.setGeometry(QtCore.QRect(50, 170, 93, 28))
        self.RegisterBtn.setObjectName("RegisterBtn")

        self.closeBtn = QtWidgets.QPushButton(Register, clicked=lambda: self.openLogin(Register))
        self.closeBtn.setText("Close")
        self.closeBtn.setGeometry(QtCore.QRect(160, 170, 93, 28))
        self.closeBtn.setObjectName("closeBtn")

        self.fullNameInput = QtWidgets.QLineEdit(Register)
        self.fullNameInput.setGeometry(QtCore.QRect(22, 40, 271, 22))
        self.fullNameInput.setObjectName("fullNameInput")

        self.userNameInput = QtWidgets.QLineEdit(Register)
        self.userNameInput.setGeometry(QtCore.QRect(20, 90, 271, 22))
        self.userNameInput.setObjectName("userNameInput")

        self.passwordInput = QtWidgets.QLineEdit(Register)
        self.passwordInput.setGeometry(QtCore.QRect(20, 140, 271, 22))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")

        self.userNameLbl = QtWidgets.QLabel(Register)
        self.userNameLbl.setText("User Name:")
        self.userNameLbl.setGeometry(QtCore.QRect(20, 70, 81, 20))
        self.userNameLbl.setObjectName("userNameLbl")

        self.passwordLbl = QtWidgets.QLabel(Register)
        self.passwordLbl.setText("Password:")
        self.passwordLbl.setGeometry(QtCore.QRect(20, 120, 81, 20))
        self.passwordLbl.setObjectName("passwordLbl")

        self.registerMsg = QtWidgets.QPlainTextEdit(Register)
        self.registerMsg.setEnabled(False)
        self.registerMsg.setGeometry(QtCore.QRect(20, 210, 271, 31))
        self.registerMsg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.registerMsg.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.registerMsg.setObjectName("registerMsg")

        self.fullNameLbl = QtWidgets.QLabel(Register)
        self.fullNameLbl.setText("Full Name:")
        self.fullNameLbl.setGeometry(QtCore.QRect(20, 20, 71, 20))
        self.fullNameLbl.setObjectName("fullNameLbl")

        QtCore.QMetaObject.connectSlotsByName(Register)

    def openLogin(self, Register):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = Login.UiLogIn()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        Register.close()

    def registerToJSON(self):
        with open(routes.usersFile) as uFile:
            users = json.load(uFile)

        newDate = {
            "FullName": self.fullNameInput.text(),
            "Username": self.userNameInput.text(),
            "Password": self.passwordInput.text(),
            "Admin": False,
            "analyst": f'analyst_{users["usersCount"]}'
        }

        if self.userNameInput.text() == "" and self.passwordInput.text() == "":
            self.fullNameInput.clear()
            self.userNameInput.clear()
            self.passwordInput.clear()
            self.registerMsg.setPlainText("Invalid Username & Password!")
            self.registerMsg.setStyleSheet("color: red")
            QTest.qWait(1000)
            self.registerMsg.setPlainText("")
            return

        if not CheckUserExistence(self.userNameInput.text(), self.registerMsg):
            with open(routes.usersFile, "r+") as DB:
                # First we load existing data into a dict.
                dataBase = json.load(DB)
                # Join new_data with file_data inside user_details
                dataBase["userDetails"].append(newDate)
                # Sets DB's current position at offset.
                DB.seek(0)
                dataBase["usersCount"] = dataBase["usersCount"] + 1
                # convert back to json.
                json.dump(dataBase, DB, indent=2)

            self.fullNameInput.clear()
            self.userNameInput.clear()
            self.passwordInput.clear()
            self.registerMsg.setPlainText("Succesfully added new User")
            self.registerMsg.setStyleSheet("color: green")
            QTest.qWait(1000)
            self.registerMsg.setPlainText("")
