import http.client
import mimetypes
import ssl
import json
import tools
import re
import requests
from datetime import datetime
import numpy as np



def track_stock(*args):
    config = args[0]
    THRESHOLD = config['stock']['THRESHOLD']
    AV_APIKEY = config['alphavantage']['AV_APIKEY']
    TOWHO = config['stock']['TOWHO']

    stocks = []
    for x in THRESHOLD.split(';'):
        ticker = re.search('\[(.+),',x).group(1).strip()
        threshold = float(re.search(',(.+)\]',x).group(1).strip())
        stocks.append({'ticker':ticker,'threshold':threshold})
    print(stocks)

    text = ''
    for stock in stocks:
        ticker = stock['ticker']
        threshold = stock['threshold']

        # get price
        av_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}'.format(ticker,AV_APIKEY)
        response = requests.get(av_url)
        av_data = response.json()
        timeseries = av_data['Time Series (Daily)']
        days = list(timeseries.keys())
        days.sort(reverse = True)
        last_day = days[0]
        close_price = float(timeseries[last_day]['4. close'])

        if close_price <= threshold:
            text_this = 'Track STOCK! Recent {} close price was {} (threshold: {})'.format(ticker,close_price,threshold)
            text += text_this + '\n'

    # send combined text
    if len(text)>0:
        tools.sendSMS(config,TOWHO,text)

    return 'done'


if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    track_stock(config)




