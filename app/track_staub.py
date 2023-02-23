import http.client
import mimetypes
import ssl
import json
import tools
import requests
import re


def track_staub(*args):
    config = args[0]
    TOWHO = config['staub']['TOWHO']
    url = "https://www.zwilling.com/us/staub-cast-iron-12-inch-braiser-with-glass-lid-white-14813002/40502-240-0.html"
    r = requests.get(url)
    html_content = r.text
    matches = re.findall("This item is out of stock",html_content)
    if len(matches) == 0:
        text = 'Staub: You HUO LA'
        tools.sendSMS(config, TOWHO, text)
    return "done"

if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    track_staub(config)




