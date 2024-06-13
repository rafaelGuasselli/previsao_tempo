from view.login_view import LoginView
from view.home_view import HomeView

login = LoginView()
login.mainloop()

while not login.loggedIn:
	login = LoginView()
	login.mainloop()

home = HomeView()
home.mainloop()