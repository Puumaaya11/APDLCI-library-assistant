def df_to_list(df):
    df_list = []
    for column in df.columns:
        df_list.append(df[column].tolist())
    return df_list[1:]