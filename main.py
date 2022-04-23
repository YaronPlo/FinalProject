import sys
from PyQt5 import QtCore, QtWidgets
from Components import Login



def Main():
    app = QtWidgets.QApplication(sys.argv).qu
    Login.RunLogIn()
    sys.exit(app.exec_())


"""
Main
"""
if __name__ == "__main__":
    Main()
