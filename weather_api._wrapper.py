import urllib.request
from http_adapter import HttpAdapter

class WeatherApiWrapper:
	def __init__(self):
		self.api_url = "https://api.weatherbit.io/v2.0/forecast/daily"
		self.http = HttpAdapter()

	def getWeather(self, city):
		self.http.get(self.api_url, f"key={self.api_key}&city={city}")
	