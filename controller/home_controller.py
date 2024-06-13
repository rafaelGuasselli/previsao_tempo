from model.weather_repository import WeatherRepository
class HomeController:
	def __init__(self, view):
		self.view = view
		self.weatherRepo = WeatherRepository()

	def search(self):
		city = self.view.getCity()
		startDate = self.view.getStartDate()
		endDate = self.view.getEndDate()

		weatherList = self.weatherRepo.load(city, startDate, endDate)
		self.view.list.createList(weatherList)

