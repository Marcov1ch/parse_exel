import pandas as pd

def summarize_remarks(df, group_by_columns, remark_column):
    return df.groupby(group_by_columns)[remark_column].apply(lambda x: '; '.join(x)).reset_index()

