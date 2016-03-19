__author__ = 'johnniemac'

import urllib2
import ssl
import SSLContext
from hawkular.metrics import *
from bottle import route, run

req = urllib2.Request(url=url)
req.add_header('Content-Type', 'application/json')
req.add_header('Hawkular-Tenant', self.tenant_id)
req.add_header('Authorization', 'Bearer QCKcZ2eA9FiD_tT0QlNyY5nQmrmcNcaVjQU0w40tRsI')
req.get_method = lambda: method
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

f = urllib2.urlopen('https://hawkular-metrics.apps.10.2.2.2.xip.io/hawkular/metrics/metrics')
print f.read(100)

@route('/')
def index():
    return "<h1> This is a test</h1>"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
