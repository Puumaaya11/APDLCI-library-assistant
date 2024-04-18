def df_to_list(df):
    df_list = []
    for column in df.columns:
        df_list.append(df[column].tolist())
    return columns_to_rows(df_list)

def columns_to_rows(data_list):
    newList = []
    for i in range(len(data_list[0])):
        newList.append([x[i] for x in data_list])
    return newList