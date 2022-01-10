import Data.Utilities as Data

df = Data.dataFrame
col = Data.relevant_columns


def columns_list():
    print("Column list:")
    for key, value in col.items():
        print(key, ": ", value)


def menu():
    print()
    print("======= MENU =======")
    print("[1] Show me the table")
    print("[2] Sort the table by columns")
    print("[3] Show only - values in column")
    print("[4] key_word(column:'Description', word:'HTTP')")
    print("[5] Show N oldest")
    print("[9] Reset DataFrame")
    print("[0] Exit")
    print()


def switcher(df, choose):
    match choose:
        case 1:
            df = Data.letters_to_numbers(df, columns=['Asset Security Grade'])
            Data.show_table(df)  # _head()

        case 2:
            Data.sorting_df(df)
            Data.show_table(df)
        case 3:
            columns_list()
            choose_col = int(input("Choose column number: "))
            column = col[choose_col]
            unique_values = df[column].unique()
            unique_dict = dict(zip(range(len(unique_values)), unique_values))
            print("values list: ", unique_dict)
            choose_val = int(input("Choose value to show: "))  # turn to multiple choose
            value = unique_dict[choose_val]
            Data.show_only(df, column, [value])
            Data.show_table(df)
        case 4:
            df = df.join(Data.dataFrame['Description'])
            df = Data.key_word(df)
            Data.show_table(df)
        case 5:
            n = int(input("Enter number of Issues: "))
            df = Data.return_N_oldest(df, n)
            Data.show_table(df)
        case 9:
            df = Data.dataFrame


while True:
    menu()
    choose = int(input("enter your chose: "))
    if not choose:
        print('bye')
        break
    switcher(df, choose)
