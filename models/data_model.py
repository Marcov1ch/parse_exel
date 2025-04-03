import pandas as pd

class DataModel:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def summarize_remarks(self, group_by_columns, remark_column):
        return self.dataframe.groupby(group_by_columns)[remark_column].apply(lambda x: '; '.join(x)).reset_index()
