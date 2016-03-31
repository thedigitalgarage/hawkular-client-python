__author__ = 'daviddimas'

import time
import json
import requests
from bottle import route, run, template

@route('/cpu-usage')
def get_cpu_usage():

	befdate = (time.time()-600) * 1000
	headers = { 'Content-Type': 'application/json', 'Hawkular-Tenant': 'sample', 'Authorization': 'Bearer y2nFTye8GdrQkiZ3XaX9mJBmvK0Uv6UjnaTt7Ypv_fQ'}
	url = 'https://hawkular-metrics.apps.10.2.2.2.xip.io/hawkular/metrics/counters/data?tags=descriptor_name:cpu/usage,pod_namespace:sample&buckets=1&start=' + repr(int(befdate))
	req = requests.get(url, headers=headers, verify=False)
	cpu_usage = req.json()[0]['max'] - req.json()[0]['min']
	uptime = req.json()[0]['end'] -req.json()[0]['start']
	core = cpu_usage / (uptime * 1000000)
	output = template('metrics_view', res= core)
	return output


@route('/memory-usage')
def get_memory_usage():

	befdate = (time.time()-600) * 1000
	headers = { 'Content-Type': 'application/json', 'Hawkular-Tenant': 'sample', 'Authorization': 'Bearer y2nFTye8GdrQkiZ3XaX9mJBmvK0Uv6UjnaTt7Ypv_fQ'}
	url = 'https://hawkular-metrics.apps.10.2.2.2.xip.io/hawkular/metrics/gauges/data?tags=descriptor_name:memory/usage,pod_namespace:sample&buckets=3&start=' + repr(int(befdate))
	req = requests.get(url, headers=headers, verify=False)
	memory_usage = req.json()[0]['max'] - req.json()[0]['min']
	for mem in req.json():
		memory_usage += mem['max']
	output = template('metrics_view', res= str(memory_usage/3) + ' Bytes')
	return output

run(host='0.0.0.0', port=8080)