__author__ = 'johnniemac'

import json
import requests
from bottle import route, run


url = 'https://hawkular-metrics.apps.10.2.2.2.xip.io/hawkular/metrics/metrics'
headers = { 'Content-Type': 'application/json', 'Hawkular-Tenant': 'sample', 'Authorization': 'Bearer _WpbISNMpyzJ04iMVrppTt-epM8U5M1BN7cAsp5rLO4'}
req = requests.get(url, headers=headers, verify=False)

req.json()

html = "<h1> It is working. The ID is: " + req.json()[2]['id'] + "</h1>"


@route('/')
def index():
    return html

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
