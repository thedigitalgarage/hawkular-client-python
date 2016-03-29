__author__ = 'johnniemac'

import json
import requests
from bottle import route, run


url = 'https://hawkular-metrics.apps.10.2.2.2.xip.io/hawkular/metrics/metrics'

req = requests.get(url, headers=headers, verify=False)

req.json()


@route('/')
def index():
    return "<h1>This is a test</h1>"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
