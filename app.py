__author__ = 'johnniemac'

import requests
from bottle import route, run


url = 'https://hawkular-metrics.apps.10.2.2.2.xip.io/hawkular/metrics/metrics'
headers = { 'Content-Type': 'application/json', 'Hawkular-Tenant': 'sample', 'Authorization': 'Bearer _WpbISNMpyzJ04iMVrppTt-epM8U5M1BN7cAsp5rLO4'}
req = requests.get(url, headers=headers, verify=False)

req.json()


@route('/')
def index():
    return "<h1>" + print(json.dumps(req, sort_keys=True, indent=4) + "</h1>"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
