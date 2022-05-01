import json
from statistics import mean

import numpy as np
import pandas as pd

import Data.Utilities as Data
from utils import routes
from utils.Helpers.GeneralHelpers import *

__all__ = ["getIssuesId", "getUserName", "getUserRules", "getFilteredTable", "updateIssuesComboBox",
           "updateIssueStatus", "hide_handled_issues", "daily_avg_issues", "done_issue_avg", "duration_and_impact"]


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


def getFilteredTable(rules, userID):
    main_df = Data.dataFrame
    raw_df = Data.raw_dataFrame
    status_table = pd.read_csv(routes.status_table, index_col=[0])
    main_df = hide_handled_issues(main_df, status_table, userID)

    # dictinary of issues and their influence
    if rules['most_impact']:
        most_influential = find_most_influential(main_df, raw_df)
        most_influential_descend = sorted(most_influential, key=lambda k: len(most_influential[k]), reverse=True)
        main_df = main_df.reindex(most_influential_descend)
        return main_df

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

    if rules['wsm']['state']:
        sliders_values = list(rules['wsm'].values())[1:]
        func_dict['wsm'](main_df, sliders_values)

    if rules['date']:
        func_dict['date'](main_df)

    for key, value in key_word_values.items():
        if rules[key] != '':
            main_df = key_word_values[key](main_df, description, [rules[key].lower()])

    for item in potential_impact_items:
        main_df = Data.show_only(main_df, Potential_Impact, [item])

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

    # issuesComboBox values created from df so check here not relevant, index exist
    if issue_index in status_table.index.values:
        # get the issue from status_table by index and remove
        current_issue = status_table.loc[[issue_index]]
        status_table = status_table.drop(issue_index)
    else:
        current_issue = df.loc[[issue_index]].copy()
        current_issue['Analyst Handler'] = currUser

    if inProgressRadioBtn.isChecked():
        current_issue['Current Status'] = 'inProgress'
        current_issue['InProgress Time'] = Data.get_now()
    else:
        current_issue['Current Status'] = 'done'
        current_issue['Done Time'] = Data.get_now()

    # status_table = status_table.append(current_issue)
    status_table = pd.concat([status_table, current_issue])
    # status_table.loc[getIssuesId(current_issue)] = current_issue
    # status_table = pd.concat([status_table, current_issue])
    # print('status_table\n', status_table.to_string())
    status_table.to_csv(routes.status_table)
    print('Status table updated')


def hide_handled_issues(df, status_df, userId):
    # show analyst issues handled by him and in progress
    in_prog_table = status_df.loc[(status_df['Analyst Handler'] == userId) &
                                  (status_df['Current Status'] == 'inProgress')]
    in_prog_ind = getIssuesId(in_prog_table)
    handled_issues = getIssuesId(status_df)
    handled_list = [int(x) for x in handled_issues if x not in in_prog_ind]
    df = df.drop(handled_list, axis=0)
    print('Handled issues removed')
    if len(df) == 0:
        print('hide_handled_issues returned empty dataframe')
    return df


def daily_avg_issues(df, userId):
    user_df = df.loc[df['Analyst Handler'] == userId]
    date_col = pd.to_datetime(user_df['InProgress Time'])
    daily_df = date_col.groupby(date_col.dt.floor('d')).size().reset_index(name='count')
    daily_counter = daily_df['count'].tolist()
    details_dict = {'daily_counter': daily_counter, 'ave_per_day': mean(daily_counter)}
    return details_dict


def done_issue_avg(df, userId):
    user_df = df.loc[(df['Analyst Handler'] == userId) &
                     (df['InProgress Time'].notnull()) &
                     (df['Done Time'].notnull())].copy()
    user_df[['InProgress Time', 'Done Time']] = user_df[['InProgress Time', 'Done Time']].apply(
        pd.to_datetime)  # if conversion required
    duration = (user_df['Done Time'] - user_df['InProgress Time']).dt.seconds / 60
    duration = list(np.around(np.array(duration), 2))
    details_dict = {'duration': duration, 'duration_mean': mean(duration)}
    return details_dict


def duration_and_impact(df, userId):
    raw_df = Data.raw_dataFrame
    user_df = df.loc[(df['Analyst Handler'] == userId) &
                     (df['InProgress Time'].notnull()) &
                     (df['Done Time'].notnull())].copy()
    user_df[['InProgress Time', 'Done Time']] = user_df[['InProgress Time', 'Done Time']].apply(
        pd.to_datetime)  # if conversion required
    if not np.issubdtype(user_df.dtypes['Done Time'], np.datetime64):
        return {}
    duration = (user_df['Done Time'] - user_df['InProgress Time']).dt.seconds / 60
    duration = list(np.around(np.array(duration), 2))
    issues_id_list = getIssuesId(user_df)
    analyst_counter = {}  # {issue_id:[duration,impact]
    impact_global = find_most_influential(df, raw_df)

    for _ in range(len(issues_id_list)):
        id = int(issues_id_list[_])
        analyst_counter[id] = [duration[_], 0]
        if id in impact_global.keys():
            analyst_counter[id][1] = len(impact_global[id])
        else:
            for values_list in impact_global.values():
                if id in values_list:
                    analyst_counter[id][1] = len(values_list)
                    break

    return analyst_counter
