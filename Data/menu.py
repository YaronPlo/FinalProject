import Data.Utilities as Data

main_df = Data.dataFrame
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
    print("[6] Weighted Sum Method – Multi Criteria Decision Making")
    print("[9] Reset DataFrame")
    print("[0] Exit")
    print()


def switcher(df_filter, action):
    match action:
        case 1:
            # df_filter = Data.letters_to_numbers(df_filter, columns=['Asset Security Grade'])
            Data.show_table(df_filter)  # _head()
            return df_filter
        case 2:
            df_filter = Data.sorting_df(df_filter)
            Data.show_table(df_filter)
            return df_filter
        case 3:
            columns_list()
            choose_col = int(input("Choose column number: "))
            column = col[choose_col]
            unique_values = df_filter[column].unique()
            unique_dict = dict(zip(range(len(unique_values)), unique_values))
            print("values list: ", unique_dict)
            choose_val = int(input("Choose value to show: "))  # turn to multiple choose
            value = unique_dict[choose_val]
            df_filter = Data.show_only(df_filter, column, [value])
            Data.show_table(df_filter)
            return df_filter
        case 4:
            df_filter = main_df
            df_filter = df_filter.join(Data.issues_dataFrame['Description'])
            df_filter = Data.key_word(df_filter)
            Data.show_table(df_filter)
            return df_filter
        case 5:
            n = int(input("Enter number of Issues: "))
            temp_df = Data.return_N_oldest(df_filter, n)
            Data.show_table(temp_df)
            return (df_filter)

        case 6:
            Data.WSM(df_filter)
            return (df_filter)
        case 9:
            return Data.dataFrame
        case _:
            print("invalid input")
            return df_filter


def table_filter():
    table = main_df
    while True:
        menu()
        try:
            choose = int(input("enter your chose: "))
            if choose == 0:
                print('bye')
                break
            table = switcher(table, choose)
        except ValueError:
            print("invalid input")


table_filter()
