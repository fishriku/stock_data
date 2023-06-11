!pip install pandas_datareader pandas

import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

# ユーザーから株価データを取得したい企業のシンボルを入力してもらいます。
ticker_symbol = input('Enter the ticker symbol of the company: ')

# ユーザーからデータを取得したい期間を入力してもらいます。
start_date = input('Enter the start date (YYYY-MM-DD): ')
end_date = input('Enter the end date (YYYY-MM-DD): ')

# Yahoo Financeからデータを取得します。
data = pdr.get_data_yahoo(ticker_symbol, start=start_date, end=end_date)

# データをCSVファイルに保存します。ファイル名もユーザーが指定した企業のシンボルに基づきます。
data.to_csv(f'{ticker_symbol}_stock.csv')