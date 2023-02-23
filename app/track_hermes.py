import http.client
import mimetypes
import ssl
import json
import tools
import requests
import re


def track_hermes(*args):
    config = args[0]
    TOWHO = config['hermes']['TOWHO']


    url = "https://www.hermes.com/us/en/category/women/bags-and-small-leather-goods/bags-and-clutches/#||Category"
    r = requests.get(url)
    html_content = r.text.lower()
    matches = re.findall("picotin lock 18",html_content)
    if len(matches) != 0:
        text = 'Hermes: Picoin is on stock'
        tools.sendSMS(config, TOWHO, text)
    return "done"

if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    track_hermes(config)

