from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class UiLogIn(object):
    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(333, 265)
        LogIn.setMouseTracking(False)
        LogIn.setWindowIcon(QtGui.QIcon('D:\\FinalProject\\Images\\SCElogo.png'))

        self.logIn = QtWidgets.QPushButton(LogIn)
        self.logIn.setGeometry(QtCore.QRect(50, 170, 93, 28))
        self.logIn.setObjectName("logIn")
        self.Register = QtWidgets.QPushButton(LogIn)
        self.Register.setGeometry(QtCore.QRect(190, 170, 93, 28))
        self.Register.setObjectName("Register")
        self.userNameInput = QtWidgets.QLineEdit(LogIn)
        self.userNameInput.setGeometry(QtCore.QRect(120, 60, 113, 22))
        self.userNameInput.setObjectName("userNameInput")
        self.userNameLbl = QtWidgets.QLabel(LogIn)
        self.userNameLbl.setGeometry(QtCore.QRect(30, 60, 81, 20))
        self.userNameLbl.setObjectName("userNameLbl")
        self.passwordLbl = QtWidgets.QLabel(LogIn)
        self.passwordLbl.setGeometry(QtCore.QRect(30, 110, 81, 20))
        self.passwordLbl.setObjectName("passwordLbl")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(LogIn)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 210, 191, 31))
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.passwordInput = QtWidgets.QLineEdit(LogIn)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setGeometry(QtCore.QRect(120, 110, 113, 22))
        self.passwordInput.setObjectName("passwordInput")

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "Log In"))
        self.logIn.setText(_translate("LogIn", "Log In"))
        self.Register.setText(_translate("LogIn", "Register"))
        self.userNameLbl.setText(_translate("LogIn", "User Name:"))
        self.passwordLbl.setText(_translate("LogIn", "Password:"))

def RunLogIn():
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QWidget()
    ui = UiLogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())
