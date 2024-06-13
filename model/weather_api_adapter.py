from .http_adapter import HttpAdapter
from .json_adapter import JsonAdapter

class WeatherApiAdapter:
	def __init__(self):
		self.api_url = "https://api.weatherbit.io/v2.0/forecast/daily"
		self.api_key = "f155f26a12a743548d351e4e30dd9352"
		self.http = HttpAdapter()
		self.jsonAdapter = JsonAdapter()

	def getWeather(self, city) -> dict:
		try:
			responseText = self.http.get(self.api_url, f"key={self.api_key}&city={city}")
			return self.jsonAdapter.textToDict(responseText)
		except Exception as error:
			print(error)
			return dict()