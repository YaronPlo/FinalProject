import json
import pandas as pd
from utils import routes
import Data.Utilities as Data

__all__ = ["getIssuesId", "getUserName", "getUserRules", "getFilteredTable", "updateIssuesComboBox",
           "updateIssueStatus"]


# values for combobox
def getIssuesId(df):
    return [str(x) for x in list(df.index.values)]


def getUserName():
    with open(routes.usersFile) as DB:
        userDB = json.load(DB)

    return userDB["currentUser"]


def getUserRules(UserID):
    with open(routes.rulesFile) as rules:
        rulesDB = json.load(rules)
    with open(routes.usersFile) as users:
        usersDB = json.load(users)

    for analyst in usersDB["userDetails"]:
        if analyst["Username"] == UserID:
            userRules = analyst["analyst"]

    return rulesDB[userRules]


def getFilteredTable(rules):
    main_df = Data.dataFrame
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
        main_df = Data.show_only(main_df, Potential_Impact, [item])
    print(main_df.head().to_string())

    return main_df


def updateIssuesComboBox(issueComboBox, itemsList):
    issueComboBox.clear()
    fixedItemsList = map(lambda x: x if isinstance(x, str) else str(x), itemsList)
    issueComboBox.addItems(fixedItemsList)


def updateIssueStatus(df, currUser, issuesComboBox, inProgressRadioBtn, doneRadioBtn):
    status_table = pd.read_csv(routes.status_table, index_col=[0])
    issue_index = int(issuesComboBox.currentText())

    # will be added when issuesComboBox return relevant values
    # current_issue = df.iloc[[int(issue_index)]]
    # print('here', current_issue)

    # issuesComboBox values created from df so check here not relevant, index exist
    if issue_index in status_table.index.values:
        # get the issue from status_table and remove
        current_issue = status_table.loc[[issue_index]]
        status_table = status_table.drop(issue_index)
    else:
        current_issue = df.loc[[issue_index]].copy()
        current_issue['Analyst Handler'] = currUser

    if inProgressRadioBtn.isChecked():
        print('inProgress')
        current_issue['Current Status'] = 'inProgress'
        current_issue['InProgress Time'] = Data.get_now()
    else:
        print('done')
        current_issue['Current Status'] = 'done'
        current_issue['Done Time'] = Data.get_now()

    status_table = status_table.append(current_issue)
    # print('status_table\n', status_table.to_string())
    # # print('getIssuesId', getIssuesId(current_issue))
    # # status_table.loc[getIssuesId(current_issue)] = current_issue
    # # # status_table = pd.concat([status_table, current_issue])
    # # print('status_table\n', status_table.to_string())
    status_table.to_csv(routes.status_table)
