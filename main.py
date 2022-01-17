from report_generator import CarsalesReport
from data_classes import Weblog, Transactions

weblog_location = 'data/'
transactions_location = 'data/'
report_location = 'data/'

weblog_file = f'{weblog_location}weblog.txt'
weblog_labels = ['ip', 'userid', 'time', 'request', 'status', 'size', 'referer', 'user_agent']
weblog_time_label = 'time'

transactions_file = f'{transactions_location}transactions.csv'
transactions_purchase_price_label = 'purchase_price'
transactions_time_label = 'purchase_timestamp'

if __name__ == '__main__':
    weblog = Weblog(weblog_file, weblog_labels, weblog_time_label)
    transactions = Transactions(transactions_file, transactions_purchase_price_label, transactions_time_label)

    report = CarsalesReport(transactions, weblog, exclude_zero_page_view_days=False, generate_report_profile=False)
    report.report_df.to_csv(f'{report_location}carsales_report.csv')
    if report.generate_report_profile:
        report.report_profile.to_file(f'{report_location}carsales_report.html')
