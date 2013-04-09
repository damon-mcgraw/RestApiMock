#!/usr/bin/python
from bottle import route, run, template

@route('/api/:request_path#.*#')
def index(request_path='World'):
	with open('log', 'a') as f:	
		f.write('{0}\n'.format(request_path))
	return ''

run(host='localhost', port=8080)
