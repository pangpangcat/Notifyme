import http.client
import mimetypes
import ssl
import json
import tools

def track_gold(*args):
    config = args[0]
    threshold = float(config['gold']['THRESHOLD'])
    TOWHO = config['gold']['TOWHO']

    conn = http.client.HTTPSConnection("www.goldapi.io",context = ssl._create_unverified_context())
    payload = ''
    headers = {
        'x-access-token': 'goldapi-2oytcuklsxnrnz-io',
        'Content-Type': 'application/json'
    }
    conn.request("GET", "/api/XAU/USD", payload, headers)
    res = conn.getresponse()
    data = res.read()
    quote = json.loads(data.decode("utf-8"))

    ts = quote['timestamp']
    low_price = quote['low_price']
    print('low_price={},threhold={}'.format(low_price,threshold))

    # low price trigger
    if low_price <= threshold:
        print('triggered')
        text = 'Track GOLD! Recent low price was {} (threshold: {})'.format(low_price,threshold)
        tools.sendSMS(config,TOWHO,text)

    return 'done'


if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    track_gold(config)




