from .json_adapter import JsonAdapter
from .weather import Weather
from .file_adapter import FileAdapter
from .weather_api_adapter import WeatherApiAdapter
from .date_adapter import DateAdpter

class WeatherRepository:
	def __init__(self):
		self.fileAdapter = FileAdapter()
		self.weatherApi = WeatherApiAdapter()
		self.jsonAdapter = JsonAdapter()
		self.dateAdapter = DateAdpter()
		self.path = "data"

	def load(self, city, startDate, endDate):
		startStamp = self.dateAdapter.getTimeStamp(startDate)
		endStamp = self.dateAdapter.getTimeStamp(endDate)

		if self.needsRefresh(city):
			self.refreshData(city)

		text = self.fileAdapter.readFile(f"{self.path}/{city}.json")
		dict = self.jsonAdapter.textToDict(text)
		days = dict.get("data") or []

		inRange = []
		for element in days:
			ts = element.get("timestamp")
			if ts >= startStamp and ts <= endStamp:
				inRange.append(Weather(city, element))
		
		return inRange

	def refreshData(self, city):
		print("Refresh")
		sourceText = self.weatherApi.getWeather(city)
		self.save(city, sourceText)

	def save(self, city, dictSource):
		textTarget = self.fileAdapter.readFile(f"{self.path}/{city}.json")
		dictTarget = self.jsonAdapter.textToDict(textTarget)

		daysSource = dictSource.get("data") or []
		daysTarget = dictTarget.get("data") or []

		for element in daysSource:
			timestamp = self.dateAdapter.getTimeStamp(element.get("valid_date"))
			element["timestamp"] = timestamp

			if len(daysTarget) == 0 or timestamp > daysTarget[-1]["timestamp"]:
				daysTarget.append(element)
		
		dictTarget["data"] = daysTarget
		self.fileAdapter.writeToFile(f"{self.path}/{city}.json", self.jsonAdapter.dictToText(dictTarget))

	def needsRefresh(self, city):
		todayP6 = self.dateAdapter.todayPlus6()
		todayP6Stamp = self.dateAdapter.getTimeStamp(todayP6.strftime('%Y-%m-%d'))

		return self.lastTimestamp(city) == None or self.lastTimestamp(city) < todayP6Stamp

	def lastTimestamp(self, city):
		textTarget = self.fileAdapter.readFile(f"{self.path}/{city}.json")
		dictTarget = self.jsonAdapter.textToDict(textTarget)
		days = dictTarget.get("data")

		if len(days) > 0:
			return days[-1].get("timestamp")
		return None