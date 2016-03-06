__author__ = 'johnniemac'


from bottle import route, run

@route('/')
def index():
    return "<h1> hello OpenShift Ninja</h1>"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
