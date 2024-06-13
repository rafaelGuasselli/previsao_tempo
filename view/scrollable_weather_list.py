import tkinter as Tk
from view.scrollable_container import ScrollableContainer

class ScrollableWeatherList(ScrollableContainer):
	def __init__(self, parent, *args, **kw):
		super().__init__(parent, *args, **kw)

	def createList(self, list=[]):
		self.__clearElements()
		self.container.config(pady=10)
		for index, element in enumerate(list):
			self.__addElement(
				index,
				weather=element
			)

	def __addElement(self, index, weather=None):
		self.container.columnconfigure((0,1,2,3,4), weight=1)
		self.container.columnconfigure(5, weight=3)

		Tk.Label(self.container, text=f"Data: {weather.date}").grid(row=index, column=0, sticky="W", padx=(10,0), pady=(0,10))
		Tk.Label(self.container, text=f"Temperatura minima: {weather.min_temp}").grid(row=index, column=1, sticky="W", pady=(0,10))
		Tk.Label(self.container, text=f"Temperatura maxima: {weather.max_temp}").grid(row=index, column=2, sticky="W", pady=(0,10))
		Tk.Label(self.container, text=f"Temperatura: {weather.temp}").grid(row=index, column=3, sticky="W", pady=(0,10))
		Tk.Label(self.container, text=f"Descrição: {weather.getDescription()}").grid(row=index, column=4, sticky="W", pady=(0,10))

	def __clearElements(self):
		for child in self.container.winfo_children(): 
			child.destroy()
