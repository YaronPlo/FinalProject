import sys
import json
from utils import routes
from PyQt5 import QtCore, QtGui, QtWidgets
from Components import Admin, Register, UserPage


class UiLogIn(object):

    def __init__(self):
        self.RegisterWindow = None
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

    def openRegister(self, LogIn):
        self.RegisterWindow = QtWidgets.QMainWindow()
        self.ui = Register.Ui_Register()
        self.ui.setupUi(self.RegisterWindow)
        self.RegisterWindow.show()
        LogIn.close()

    def openAdminPage(self, LogIn):
        self.AdminWindow = QtWidgets.QMainWindow()
        self.ui = Admin.Ui_AdminPage()
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
        LogIn.setWindowIcon(QtGui.QIcon(routes.sceLogo))

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
        self.Register.clicked.connect(lambda: self.openRegister(LogIn))

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle("Log In")
        self.logIn.setText("Log In")
        self.Register.setText("Register")
        self.userNameLbl.setText("User Name:")
        self.passwordLbl.setText("Password:")

    def TypeUserCheck(self):
        pass

    def updateLoginInput(self):
        pass

    def LoginCheck(self, LogIn):
        with open(routes.usersFile, "r") as DB:
            dataBase = json.load(DB)

        for user in dataBase["userDetails"]:
            if self.userNameInput.text() == "" or self.passwordInput.text() == "":
                self.plainTextEdit.setPlainText("input Wrong!")
                self.plainTextEdit.setStyleSheet("color: red")
                return
            elif (
                    user["Username"] == self.userNameInput.text()
                    and user["Password"] != self.passwordInput.text()
            ):
                self.plainTextEdit.setPlainText("Wrong Password!")
                self.plainTextEdit.setStyleSheet("color: red")
                return
            elif (
                    user["Username"] == self.userNameInput.text()
                    and user["Password"] == self.passwordInput.text()
            ):
                self.plainTextEdit.setPlainText("Success!")
                self.plainTextEdit.setStyleSheet("color: green")
                if (
                        user["Username"] == self.userNameInput.text()
                        and user["Password"] == self.passwordInput.text()
                        and user["Admin"] == True
                ):
                    self.openAdminPage(LogIn)
                    return
                elif (
                        user["Username"] == self.userNameInput.text()
                        and user["Password"] == self.passwordInput.text()
                        and user["Admin"] == False
                ):
                    self.openUserPage(LogIn)
                    return
        self.plainTextEdit.setPlainText("User Doesn't Exists!")
        self.plainTextEdit.setStyleSheet("color: red")
        return

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
