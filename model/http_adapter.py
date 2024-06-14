from urllib import request, parse

class HttpAdapter:
	def get(self, url, params):
		requestURL = "{:s}?{:s}".format(url, params)
		response = request.urlopen(parse.quote(requestURL, safe=':/?&='))
		return response.read().decode("utf-8")