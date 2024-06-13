from urllib import request, parse

class HttpAdapter:
	def post(self, url, data):
		data = parse.urlencode(data).encode()
		req =  request.Request(url, data=data) 
		return request.urlopen(req)

	def get(self, url, params):
		return request.urlopen("{:s}?{:s}".format(url, params))
