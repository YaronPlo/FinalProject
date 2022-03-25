import json
from utils import routes
import Data.Utilities as Data


def updateIssuesComboBox(issueComboBox, itemsList):
    issueComboBox.clear()
    fixedItemsList = map(lambda x: x if isinstance(x, str) else str(x), itemsList)
    issueComboBox.addItems(fixedItemsList)


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


def getFilteredTable(rules, table):
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

    # fillTableData(main_df, table)

    print(main_df.head().to_string())
