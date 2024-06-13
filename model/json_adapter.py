import json
class JsonAdapter:
	def textToDict(self, text) -> dict:
		try:
			return json.loads(text)
		except Exception as error:
			print(error)
			return dict()
	
	def dictToText(self, dict) -> str:
		try:
			return json.dumps(dict, indent=4)
		except Exception as error:
			print(error)
			return "{}"