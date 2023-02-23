# -*- coding: utf-8 -*-

from requests import post,get
import json
from contextlib import closing
import csv
from twilio.rest import Client
import numpy as np
# from sqlalchemy import create_engine,text
from datetime import datetime,timedelta,date


def queryAVtimeseries(function=None,symbol=None,interval=None,outputsize=None,apikey=None,datatype='json'):

    url = 'https://www.alphavantage.co/query'

    payload = {'function': function,
               'symbol': symbol,
               'interval': interval,
               'outputsize': outputsize,
               'apikey': apikey,
               'datatype': datatype}

    if datatype == 'json':

        r = get(url, params=payload)
        print(r.url)
        data_json = r.text
        data_dict = json.loads(data_json)
        # print(data_dict)

        if function == 'GLOBAL_QUOTE':
            price = float(data_dict['Global Quote']['05. price'])
            volume = float(data_dict['Global Quote']['06. volume'])
            stockinfo = {'price':price,'volume':volume}

    return stockinfo

def getToday():
    todayD = datetime.combine(date.today(), datetime.min.time())
    return todayD

def getYesterD():
    todayD = datetime.combine(date.today(), datetime.min.time())
    yesterD = todayD + timedelta(days=-1)
    return yesterD

def getTomorrD():
    todayD = datetime.combine(date.today(), datetime.min.time())
    tomorrD = todayD + timedelta(days=1)
    return tomorrD


def sendSMS(config,towho,text):
    twilio_sid = config['twilio']['TWILIO_SID']
    twilio_token = config['twilio']['TWILIO_TOKEN']
    fromwho =config['twilio']['FROMWHO']

    client = Client(twilio_sid, twilio_token)

    numbers = towho.split(',')
    for this_number in numbers:
        message = client.messages.create(to= this_number,
                                         from_= fromwho,
                                         body = text)
    return 'done'


def la2utc(hour_la):
    all_la_hour = hour_la.split(',')
    all_utc_list = []
    for x in all_la_hour:
        temp = int(x)+7
        all_utc_list.append(str(temp-24 if temp>=24 else temp))
    all_utc_hour = ','.join(all_utc_list)
    return all_utc_hour




if __name__ == '__main__':

    #tests:
    #0: test getToday()
    #1: test sendSMS(config,text)
    #2: test la2utc(hour_la)

    test = 2

    # test
    if test == 0:
        todayD,tomorrD,yesterD = getToday()
        print(todayD)
        print(tomorrD)
        print(yesterD)

    if test == 1:
        import configparser
        config = configparser.ConfigParser()
        config.read('config.ini')
        sendSMS(config, 'li hai le!')
    if test == 2:
        import configparser
        config = configparser.ConfigParser()
        config.read('config.ini')
        print(la2utc(config['staub']['HOUR']))


    



