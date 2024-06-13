from urllib import request, parse

class HttpAdapter:
	def post(self, url, data):
		data = parse.urlencode(data).encode()
		req =  request.Request(url, data=data) 
		return request.urlopen(req)

	def get(self, url, params):
		requestURL = "{:s}?{:s}".format(url, params)
		response = request.urlopen(parse.quote(requestURL, safe=':/?&='))
		return response.read().decode("utf-8")