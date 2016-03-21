__author__ = 'johnniemac'

import requests
from bottle import route, run


url = 'https://hawkular-metrics.apps.10.2.2.2.xip.io:8443/hawkular/metrics/metrics'
headers = { 'Content-Type': 'application/json', 'Hawkular-Tenant': 'sample', 'Authorization': 'Bearer EW4COhQplP_SOkhvDaIJJwW6R4z4BI3DUg1vzHF197I'}
req = requests.get(url, headers=headers)

req.json()

@route('/')
def index():
    return "<h1> This is a test</h1>"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
