class Weather:
	def __init__(self, city, json):
		if isinstance(json, dict):
			self.date = json.get("valid_date")
			self.timestamp = json.get("timestamp")
			self.description = json.get("weather").get("description")

			self.temp = json.get("temp")
			self.max_temp = json.get("max_temp")
			self.min_temp = json.get("min_temp")
			
		self.city = city

	def __str__(self):
		return f"City: {self.city}, Date: {self.date}"