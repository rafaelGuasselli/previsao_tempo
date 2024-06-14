from model.user_repository import UserRepository
from view.popup import Popup

class LoginViewController:
	def __init__(self, view):
		self.view = view
		self.userRepo = UserRepository()
		self.popup = Popup()

	def login(self):
		name = self.view.getName()
		password = self.view.getPassword()
		self.view.loggedIn = self.userRepo.login(name, password)
		if self.view.loggedIn:
			self.close()
		else:
			self.popup.showinfo("Erro", "Usuário ou senha incorreto!")

	def close(self):
		self.view.quit()
		self.view.destroy()