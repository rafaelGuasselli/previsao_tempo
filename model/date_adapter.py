from datetime import datetime, timedelta
class DateAdpter:
	def getTimeStamp(self, date):
		try: 
			return datetime.strptime(date, "%Y-%m-%d").timestamp()
		except Exception as error:
			print(error)
			return -1

	def todayPlus6(self):
		return datetime.today() + timedelta(days=6)