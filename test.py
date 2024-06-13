from model.weather_repository import WeatherRepository
from model.file_adapter import FileAdapter

repo = WeatherRepository()
file = FileAdapter()

resultado = repo.load("Florianópolis", "2024-06-14","2024-06-16")
for data in resultado:
	print(str(data))