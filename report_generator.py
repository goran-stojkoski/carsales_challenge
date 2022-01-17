import pandas as pd
from pandas_profiling import ProfileReport


class CarsalesReport():
    def __init__(self, transactions, weblog, exclude_zero_page_view_days=True, generate_report_profile=False):
        self.transactions = transactions
        self.weblog = weblog
        self.transactions_df = self.transactions.to_pandas_df()
        self.weblog_df = self.weblog.to_pandas_df()
        self.exclude_zero_page_view_days = exclude_zero_page_view_days
        self.report_df = self._generate_df_()
        self.generate_report_profile = generate_report_profile
        if self.generate_report_profile:
            self.report_profile = ProfileReport(self.report_df, title='Carsales Report')
        else:
            self.report_profile = None

    def _generate_df_(self):
        transactions_by_day = self.transactions_df.groupby(pd.Grouper(freq='d'))
        weblog_by_date = self.weblog_df.groupby(pd.Grouper(freq='d'))

        # 1. Report Number of page views aggregated by day
        page_views_by_day = weblog_by_date.size().rename('page_views')
        if self.exclude_zero_page_view_days:
            page_views_by_day = page_views_by_day[page_views_by_day != 0]

        # 2. Report Number of purchases by day
        purchases_per_day = transactions_by_day.size().rename('purchases')

        # 3. % Report conversions by the day. Conversion = Number of purchases / page views
        pct_report_conversions = (purchases_per_day / page_views_by_day).rename('purchases_per_page_view').round(2)

        # calculate total purchases by day and extract values as series (for onward calc)
        sum_purchases_per_day = transactions_by_day.sum(self.transactions.purchase_price_label)[
            self.transactions.purchase_price_label]

        # 4. % Revenue Conversion by the day. Revenue Conversion = Total Purchase Amount / pageviews
        pct_revenue_conversion = (sum_purchases_per_day / page_views_by_day).rename('revenue_per_page_view').round(2)

        report_df = pd.concat([purchases_per_day, page_views_by_day, pct_report_conversions, pct_revenue_conversion],
                              join='inner', axis=1)
        return report_df

    def __generate_report__(self):
        return ProfileReport(self.report_df, title='Carsales Report')

    def __repr__(self):
        return self.report_df.to_string()
