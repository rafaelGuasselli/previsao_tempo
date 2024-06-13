from .file_adapter import FileAdapter
from .json_adapter import JsonAdapter
from .user import User

class UserRepository:
	def __init__(self):
		self.fileAdapter = FileAdapter()
		self.jsonAdapter = JsonAdapter()
		self.path = "user"

	def getUser(self, name):
		fileText = self.fileAdapter.readFile(f"{self.path}/{name}.json")
		userDict = self.jsonAdapter.textToDict(fileText)
		return User(userDict.get("name"))

	def login(self, name, password):
		fileText = self.fileAdapter.readFile(f"{self.path}/{name}.json")
		userDict = self.jsonAdapter.textToDict(fileText)
		return userDict.get("password") == password
	
	