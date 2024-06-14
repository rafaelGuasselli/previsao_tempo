from view.login_view import LoginView
from view.home_view import HomeView

login = LoginView()
login.mainloop()

if login.loggedIn:
	home = HomeView()
	home.mainloop()