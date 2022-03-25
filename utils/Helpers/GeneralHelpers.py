import json
from utils import routes
from PyQt5.QtWidgets import QTableWidgetItem


# this function will fill the tableWidget with the dataFrame it gets
def fillTableData(df, table):
    # set the amout of rows and cols
    table.setRowCount(len(df))
    table.setColumnCount(len(df.columns))

    # Fill the Headers in the Table
    table.setHorizontalHeaderLabels((colName for colName in df.columns))
    for rows in range(len(df)):
        for cols in range(len(df.columns)):
            table.setItem(rows, cols, QTableWidgetItem(df.iat[rows, cols]))


# this function will update the users.json file, with the analyst that is logged in right now.
def currentLoggedInUpdate(Username):
    with open(routes.usersFile) as DB:
        userDB = json.load(DB)

    userDB["currentUser"] = Username
    with open(routes.usersFile, 'w') as DB:
        json.dump(userDB, DB, indent=2)
