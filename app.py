__author__ = 'johnniemac'

import urllib2
from hawkular.metrics import *
from bottle import route, run

f = urllib2.urlopen('http://www.python.org/')
print f.read(100)

@route('/')
def index():
    return "<h1> This is a test</h1>"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
