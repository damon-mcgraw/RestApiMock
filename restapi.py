from bottle import Bottle, run, request, response, template

class baseHandler(object):
	def handler(self, request):
		return False
	
	def updateResponse(self, response):
		return 

class logHandler(baseHandler):
	def handle(self, request):
		with open('log', 'a') as f:	
			f.write('{0}\t'.format(request.path))
			for name, value in request.forms.iteritems():
				f.write('{0}={1}&'.format(name, value.replace('\r\n', '')))
			f.write('\n\n')
		return super(logHandler, self).handle(request)

	def updateResponse(self, response):
		return super(logHandler, self).updateResponse(response)
		
		
app = Bottle()
handlers = [logHandler()]

@app.route('/<request_path:re:.*>', method='ANY')
def index(request_path='unknown'):
	for h in handlers:
		if h.handle(request):
			h.updateResponse(response)

run(app, host='localhost', port=8080, debug=True)

