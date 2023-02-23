import configparser
import pandas as pd
import numpy as np
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from track_gold import track_gold
from track_stock import track_stock
from track_staub import track_staub
from track_hermes import track_hermes
import tools
import time

config = configparser.ConfigParser()
config.read('config.ini')

scheduler = BlockingScheduler(timezone='UTC')  #America/Los_Angeles

# gold
if config['gold']['STATUS'] == 'ON':
    scheduler.add_job(
        func=track_gold,
        trigger=CronTrigger(hour=tools.la2utc(config['gold']['HOUR']),minute=config['gold']['MINUTE'], start_date=tools.getToday()),
        id='track_gold',
        name='track_gold',
        args=[config],
        replace_existing=True)

#stock
if config['stock']['STATUS'] == 'ON':
    scheduler.add_job(
        func=track_stock,
        trigger=CronTrigger(hour=tools.la2utc(config['stock']['HOUR']),minute=config['stock']['MINUTE'], start_date=tools.getToday()),
        id='track_stock',
        name='track_stock',
        args=[config],
        replace_existing=True)

#staub
if config['staub']['STATUS'] == 'ON':
    scheduler.add_job(
        func=track_staub,
        trigger=CronTrigger(hour=tools.la2utc(config['staub']['HOUR']), start_date=tools.getToday()),
        id='track_staub',
        name='track_staub',
        args=[config],
        replace_existing=True)


#hermes
if config['hermes']['STATUS'] == 'ON':
    scheduler.add_job(
        func=track_hermes,
        trigger=CronTrigger(hour=tools.la2utc(config['hermes']['HOUR']), start_date=tools.getToday()),
        id='track_hermes',
        name='track_hermes',
        args=[config],
        replace_existing=True)

# BC_10YEAR


# IYC

scheduler.start()











