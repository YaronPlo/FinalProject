import pandas as pd
from utils import routes
from datetime import datetime


def open_csv(path):
    try:
        return pd.read_csv(path, low_memory=False)
    except:
        return pd.read_csv(f'..\\{path}', low_memory=False)


def table_description(_df):
    print('number of column:', _df.shape[1])
    print('number of columns which is NaN:',
          len(_df[_df.columns[_df.isnull().all()]].columns))  # ),'\n',df[df.columns[df.isnull().all()]].columns)
    print()


# Severity, Asset Security Grade, Asset Security Score, Asset Discoverability, Asset Attractiveness
# numeric columns: Asset Security Score(continuous),
# Alpha-betic columns:Severity(4),Asset Security Grade (16), Asset Discoverability(4), Asset Attractiveness(4)

pd.reset_option("max_columns")

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

issues_dataFrame = open_csv(routes.issues_path)

relevant_columns = {1: 'Severity',
                    2: 'Asset Security Grade',
                    3: 'Asset Security Score',
                    4: 'Asset Discoverability',
                    5: 'Asset Attractiveness',
                    6: 'Asset Type',
                    7: 'Potential Impact',
                    8: 'Asset First Seen',
                    9: 'Description'
                    }

catagories = {'low': 1,
              'moderate': 2,
              'medium': 2,
              'high': 3,
              'extreme': 4,
              'critical': 4
              }


def cat_to_num(df, col_list, catagories):
    df = df.copy()
    for _ in col_list:
        df.loc[:, _] = df[_].map(catagories)
    return df


def show_table_head(df):
    print(df.head().to_string())


def show_table(df1):
    print(df1.to_string())


def num_to_bins(df, col_list, num_of_bins):
    for _ in col_list:
        temp = pd.DataFrame(df[_])
        df[_] = pd.cut(df[_], num_of_bins, labels=range(num_of_bins))
        temp['bins'] = df[_]
        print(temp)
    return df


def sorting_df(df, col=['Asset Security Grade', 'Asset Security Score']):
    df_sorted = df.sort_values(by=col, inplace=False, ascending=[False, False])
    return df_sorted


def show_only(df, column_name, values):  # only_values:list
    # filtered_df = df.loc[df[column_name].isin(values)]
    # values = '&'.join(values)  # '&' for and statemennt
    for val in values:
        mask = df[column_name].apply(lambda sent: val in sent)
        filtered_df = df[mask]
    # filtered_df = df.loc[df[column_name].str.contains(values, na=False)]
    # filtered_df = df.loc[df[column_name].astype('str').str.contain(values,na=True)]#for Integer columns

    if len(filtered_df) == 0:
        print("The key words: ", values, "not exist in columns: ", column_name)
        return df
    print('filtered_df')

    return filtered_df


def dont_show(df, column_name, values):  # only_values:list
    df = df.loc[~df[column_name].isin(values)]
    return df


def str_to_datatime(df, col_list):
    for _ in col_list:
        df.loc[:, _] = df[_].apply(lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ'))
    # return df


def get_now():
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # time object
    return now


# def oldest(datatime_list):
#     df = df1.copy()
#     df = df.loc[df['Asset First Seen'] == min(datatime_list)]
#     return df

def return_N_oldest(df, n):
    df = df.sort_values(by=['Asset First Seen'])
    df.reset_index(drop=True, inplace=True)
    return df.head(n)


def letters_to_numbers(df, columns):
    for col in columns:
        df.loc[:, col] = [ord(x) - 64 if type(x) == str else x for x in df[col]]
    return df


def Potential_Impact_column(df):  # clean string
    banned = ['Loss', 'of', '|']
    df['Potential Impact'] = df['Potential Impact'].apply(
        lambda sent: (" ".join(x.lower() for x in sent.replace('|', '').split(' ') if x not in banned)).split(' '))
    # df = key_word(df, 'Potential Impact', key_word)
    # print('->',df['Potential Impact'])
    return df


def key_word(df, col='Description', word='HTTP'):
    df = df.loc[lambda sent: sent[col].apply(lambda l: word.lower() in l)]
    return df


def unique_to_numbers(df, col):
    unique = dict(enumerate(df[col].unique()))
    unique = {value: key for key, value in unique.items()}
    df[col].replace(unique, inplace=True)
    return df


def WSM(df):  # Weighted Sum Method – Multi Criteria Decision-Making
    col = ['Severity', 'Asset Security Grade', 'Asset Security Score', 'Asset Discoverability']
    df = df[col].copy()
    df = letters_to_numbers(df, columns=['Asset Security Grade'])
    weights = [0.2, 0.3, 0.25, 0.25]  # sum=1
    dictWsm = {}
    for idx in range(len(col)):
        dictWsm[col[idx]] = weights[idx]
    beneficial_col = col[:-1]
    non_beneficial_col = col[-1]
    df.loc[:, beneficial_col] = df[beneficial_col] / df[beneficial_col].max()
    df.loc[:, non_beneficial_col] = df[non_beneficial_col].min() / df[non_beneficial_col]
    for col, weight in dictWsm.items():
        calculate = df[col] * weight
        df.loc[:, col] = calculate
    df.loc[:, 'Performance Score'] = df.sum(axis=1)
    df.loc[:, 'rank'] = df['Performance Score'].rank(method='first', ascending=False)
    df.loc[:, 'classified'] = pd.cut(df['rank'], 5, labels=list(range(1, 5 + 1)))
    df.sort_values(by=['rank'], inplace=True)
    # df.reset_index(drop=True, inplace=True)
    # print(df.head(10).to_string())
    return df


def table_preprocess(df, relevant_col, catagories_list):
    print(df.shape)
    df = Potential_Impact_column(df)
    df['Description'] = df['Description'].apply(lambda sent: [x.lower() for x in sent.split(' ') if x.isalpha()])
    df = df[relevant_col.values()]
    df = cat_to_num(df, ['Severity', 'Asset Discoverability', 'Asset Attractiveness'], catagories_list)
    str_to_datatime(df, ['Asset First Seen'])
    return df


dataFrame = table_preprocess(issues_dataFrame, relevant_columns, catagories)
