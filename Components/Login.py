import json
from utils import routes
from PyQt5.QtTest import QTest
from PyQt5 import QtCore, QtGui, QtWidgets
from Components import Admin, Register, AnalystDashboard


def currentLogedInUpdate(Username):
    with open(routes.usersFile) as DB:
        userDB = json.load(DB)

    userDB["currentUser"] = Username
    with open(routes.usersFile, 'w') as DB:
        json.dump(userDB, DB, indent=2)


class UiLogIn(object):

    def __init__(self):
        self.RegisterWindow = None
        self.loginMessage = None
        self.analsyDashboardWindow = None
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

    def openAnalystDashboard(self, LogIn):
        self.analsyDashboardWindow = QtWidgets.QMainWindow()
        self.ui = AnalystDashboard.Ui_AnalystDashboard()
        self.ui.setupUi(self.analsyDashboardWindow)
        self.analsyDashboardWindow.show()
        LogIn.close()

    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(333, 265)
        LogIn.setMouseTracking(False)
        LogIn.setWindowIcon(QtGui.QIcon(routes.sceLogo))

        self.userNameInput = QtWidgets.QLineEdit(LogIn)
        self.userNameInput.setGeometry(QtCore.QRect(120, 60, 113, 22))
        self.userNameInput.setObjectName("userNameInput")
        self.userNameInput.returnPressed.connect(lambda: self.LoginCheck(LogIn))

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
        self.passwordInput.returnPressed.connect(lambda: self.LoginCheck(LogIn))

        self.loginMessage = QtWidgets.QPlainTextEdit(LogIn)
        self.loginMessage.setEnabled(False)
        self.loginMessage.setGeometry(QtCore.QRect(70, 210, 191, 31))
        self.loginMessage.setFocusPolicy(QtCore.Qt.NoFocus)
        self.loginMessage.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.loginMessage.setObjectName("plainTextEdit")

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

    def LoginCheck(self, LogIn):
        with open(routes.usersFile, "r") as DB:
            dataBase = json.load(DB)

        if self.userNameInput.text() == "" or self.passwordInput.text() == "":
            self.loginMessage.setPlainText("Blank Input Try Again!")
            self.loginMessage.setStyleSheet("color: red")
            QTest.qWait(1000)
            self.loginMessage.setPlainText("")
            return

        for user in dataBase["userDetails"]:
            if user["Username"] == self.userNameInput.text() and user["Password"] != self.passwordInput.text():
                self.loginMessage.setPlainText("Wrong Password!")
                self.loginMessage.setStyleSheet("color: red")
                QTest.qWait(1000)
                self.loginMessage.setPlainText("")
                return

            elif user["Username"] == self.userNameInput.text() and user["Password"] == self.passwordInput.text():
                if (user["Username"] == self.userNameInput.text() and user["Password"] == self.passwordInput.text() and
                        user["Admin"] is True):
                    self.loginMessage.setPlainText("Loging in, Please Wait...")
                    self.loginMessage.setStyleSheet("color: green")
                    self.openAdminPage(LogIn)
                    return
                else:
                    self.loginMessage.setPlainText("Loging in, Please Wait...")
                    self.loginMessage.setStyleSheet("color: green")
                    QTest.qWait(0)
                    currentLogedInUpdate(self.userNameInput.text())
                    self.openAnalystDashboard(LogIn)
                    return

        self.loginMessage.setPlainText("User Doesn't Exists!")
        self.loginMessage.setStyleSheet("color: red")
        QTest.qWait(1000)
        self.loginMessage.setPlainText("")
        return


def RunLogIn():
    LogIn = QtWidgets.QWidget()
    ui = UiLogIn()
    ui.setupUi(LogIn)
    LogIn.show()
