class Weather:
	def __init__(self, city, json):
		if isinstance(json, dict):
			self.date = json.get("valid_date")
			self.timestamp = json.get("timestamp")
			self.code = json.get("weather").get("code")

			self.temp = json.get("temp")
			self.max_temp = json.get("max_temp")
			self.min_temp = json.get("min_temp")
			
		self.city = city
		self.descriptionTable = {
			200: "Trovoada com chuva fraca",
			201: "Trovoada com chuva",
			202: "Trovoada com chuva forte",
			230: "Trovoada com garoa leve",
			231: "Trovoada com garoa",
			232: "Trovoada com garoa forte",
			233: "Tempestade com granizo",
			300: "Garoa leve",
			301: "Garoa",
			302: "Garoa forte",
			500: "Chuva fraca",
			501: "Chuva moderada",
			502: "Chuva forte",
			511: "Chuva congelante",
			520: "Aguaceiro leve",
			521: "Aguaceiro",
			522: "Aguaceiro forte",
			600: "Neve fraca",
			601: "Neve",
			602: "Neve forte",
			610: "Chuva e neve",
			611: "Granizo",
			612: "Granizo forte",
			621: "Aguaceiro de neve",
			622: "Aguaceiro de neve forte",
			623: "Rajadas",
			700: "Névoa",
			711: "Neblina",
			721: "Neblina",
			731: "Tempestade de areia",
			741: "Neblina",
			751: "Neblina congelante",
			800: "Céu limpo",
			801: "Poucas nuvens",
			802: "Nuvens dispersas",
			803: "Nuvens quebradas",
			804: "Nuvens nubladas",
			900: "Desconhecido"
		}

	def getDescription(self):
		description = self.descriptionTable.get(self.code)
		return description or self.descriptionTable[900]

	def __str__(self):
		return f"City: {self.city}, Date: {self.date}"