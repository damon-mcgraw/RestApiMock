#!/usr/bin/python
from bottle import Bottle, run, request, template

app = Bottle()

@app.route('/<request_path:re:.*>', method='ANY')
def index(request_path='unknown'):
	with open('log', 'a') as f:	
		f.write('{0}\t'.format(request_path))
		for name, value in request.forms.iteritems():
			f.write('{0}={1}&'.format(name, value.replace("\r\n", "")))
		f.write('\n\n')
	return ''

run(app, host='localhost', port=8080, debug=True)
