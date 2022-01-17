import pandas as pd


class Weblog:
    def __init__(self, weblog_file, labels, timestamp_label):
        self.weblog_file = weblog_file
        self.labels = labels
        self.timestamp_label = timestamp_label

    def to_pandas_df(self):
        df = pd.read_csv(
            self.weblog_file,
            sep=r'\s-\s|\s(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)(?![^\[]*\])',
            engine='python',
            header=None,
            names=self.labels,
            converters={
                'status': int,
                'size': int,
            }
        )
        df = df.replace('\[|\]|\"', '', regex=True)
        df.set_index(pd.to_datetime(df[self.timestamp_label], format='%d/%b/%Y:%H:%M:%S %z', utc=True), inplace=True)
        df.drop(columns=self.timestamp_label, inplace=True)
        return df


class Transactions:
    def __init__(self, transactions_file, purchase_price_label, timestamp_label):
        self.transactions_file = transactions_file
        self.purchase_price_label = purchase_price_label
        self.timestamp_label = timestamp_label

    def to_pandas_df(self):
        transactions_df = pd.read_csv(self.transactions_file, index_col=self.timestamp_label)
        transactions_df.set_index(pd.to_datetime(transactions_df.index), inplace=True)
        return transactions_df
