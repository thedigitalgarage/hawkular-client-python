__author__ = 'daviddimas'

import subprocess, json
from bottle import route, run, template

@route('/')
def get_metrics():

	#bash_com = 'curl -k -H "Authorization: Bearer iwcdmHj1of6GMVpg0TJgpcWaR2J5c9BIoIfU9ankbFA" -H "hawkular-tenant: sample" -X GET https://hawkular-metrics.apps.10.2.2.2.xip.io/hawkular/metrics/metrics | python -m json.tool'
	bash_com = 'curl -k -H "Authorization: Bearer iwcdmHj1of6GMVpg0TJgpcWaR2J5c9BIoIfU9ankbFA" -H "hawkular-tenant: sample" -X GET https://hawkular-metrics.apps.10.2.2.2.xip.io/hawkular/metrics/metrics?tags=descriptor_name:cpu/usage  | python -m json.tool'
	subprocess.Popen(bash_com)
	data = subprocess.check_output(['bash','-c', bash_com])
	#output = template('metrics_view', res=json.loads(data))
	output = template('metrics_view', res=data)
	return output

run(host='0.0.0.0', port=8080)