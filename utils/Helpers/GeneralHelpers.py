import json
from utils import routes
from PyQt5.QtWidgets import QTableWidgetItem
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import pandas as pd

__all__ = ["fillTableData", "currentLoggedInUpdate", "find_most_influential", "cosine_sim_vectors", "clean_string"]


# this function will fill the tableWidget with the dataFrame it gets
def fillTableData(df, table):
    # set the amout of rows and cols
    table.setRowCount(len(df))
    table.setColumnCount(len(df.columns))

    # Fill the Headers rows and cols in the Table
    table.setHorizontalHeaderLabels(colName for colName in df.columns)
    table.setVerticalHeaderLabels(str(rowName) for rowName in df.index)
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


stopwords = stopwords.words('english')
stopwords += ['open', 'source', 'vulnerable', 'deference', 'vulnerabilities', 'later', 'function', 'version',
              'vulnerability', 'multiple']


def clean_string(text):
    text = ''.join([word.lower() for word in text if word not in string.punctuation])
    # text = text.lower()
    text = ' '.join([word for word in text.split() if (word not in stopwords and word.isalpha())])
    return text


def cosine_sim_vectors(vec1, vec2):
    vectorizer = CountVectorizer().fit_transform([vec1, vec2])
    vectors = vectorizer.toarray()
    vec1 = vectors[0].reshape(1, -1)
    vec2 = vectors[1].reshape(1, -1)
    return cosine_similarity(vec1, vec2)[0][0]



def find_most_influential(df, raw_df):
    # return dictinary with index as key and list of indexes as value which influenced after treat this key
    similarity = 'similarity'
    round = 0
    result = {}
    df = adding_similarity_column(df, raw_df)
    for index1, row1 in df.iterrows():  # iterate over df rows
        round += 1
        if index1 in [x for xs in result.values() for x in xs]:  # if this issue already treated skip it
            continue
        result[index1] = affected_issues(df[round:], result.values(), row1[similarity])
    return result


def affected_issues(sub_df, result_values, issue_similarity_col):  # inner_loop_most_influential
    similarity = 'similarity'
    result_array = []
    for index2, row2 in sub_df.iterrows():  # iterate over df rows from index1 + 1
        if index2 in [x for xs in result_values for x in xs]:
            continue
        cos_sim = cosine_sim_vectors(issue_similarity_col, row2[similarity])  # calculate similarity
        if cos_sim > 0.7:
            result_array += [index2]
    return result_array


def adding_similarity_column(df, raw_df):
    similarity = 'similarity'
    df = pd.merge(df, raw_df[['Title', 'Remediation Steps']], left_index=True,
                  right_index=True)  # adding two columns to df from origin df
    df[similarity] = df['Remediation Steps'] + ' ' + df['Title']  # unite two added columns to one
    df.loc[:, similarity] = df[similarity].apply(lambda x: clean_string(x))
    return df


# example of using adding_similarity_column for single issue:
# arr = affected_issues(cleaned_df,[],cleaned_df.loc[2]['similarity'])
