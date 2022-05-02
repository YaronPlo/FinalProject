import sys

from PyQt5 import QtWidgets

from Components import Login
from utils.Helpers.GeneralHelpers import default_rules


def Main():
    default_rules()

    app = QtWidgets.QApplication(sys.argv)
    Login.RunLogIn()
    sys.exit(app.exec_())


"""
Main
"""
if __name__ == "__main__":
    Main()
